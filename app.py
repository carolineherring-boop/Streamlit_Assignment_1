import altair as alt
import pandas as pd
import streamlit as st

from budget import MONTHS, STYLE_MULTIPLIERS, estimate_breakdown, find_destinations, is_in_season
from destinations import DESTINATIONS, VIBES

st.set_page_config(page_title="Trip Budget Planner", page_icon="✈️", layout="wide")


def format_months(month_numbers):
    """Turn [4, 5, 10] into 'Apr, May, Oct'."""
    return ", ".join(MONTHS[number - 1][:3] for number in sorted(month_numbers))


# ---------- Header ----------
st.title("Trip Budget Planner")
st.write(
    "Plan a trip that fits your wallet. Use **Where can I go?** to see which destinations "
    "fit your budget, or **What will this cost?** to get a cost estimate for a place you "
    "already have in mind."
)
st.caption("Prices are approximate planning estimates in US dollars, with round-trip flights from New York City.")

# ---------- Sidebar: travel style ----------
with st.sidebar:
    st.header("Your travel style")
    style = st.selectbox(
        "How do you like to travel?",
        list(STYLE_MULTIPLIERS),
        index=1,
        help="Travel style scales hotel and food costs. Flights and activities stay the same.",
    )
    st.write(
        f"**{style}** multiplies hotel and food costs by **{STYLE_MULTIPLIERS[style]}×**."
    )
    st.markdown(
        "- **Budget (0.6×):** hostels, guesthouses, street food\n"
        "- **Mid-range (1.0×):** standard hotels, casual restaurants\n"
        "- **Comfort (1.6×):** upscale hotels, sit-down dining"
    )

find_tab, estimate_tab = st.tabs(["Where can I go?", "What will this cost?"])

# ---------- Mode 1: Where can I go? ----------
with find_tab:
    st.subheader("Where can I go?")
    st.write("Set your budget and trip length to see every destination that fits.")

    col1, col2 = st.columns(2)
    with col1:
        budget = st.slider("Total budget (USD)", min_value=500, max_value=10000, value=2500, step=100)
        nights = st.number_input("Number of nights", min_value=1, max_value=21, value=5, step=1)
    with col2:
        month_choice = st.selectbox("Travel month (optional)", ["Any month"] + MONTHS)
        chosen_vibes = st.multiselect(
            "Vibe (optional)", VIBES, placeholder="Any vibe", help="Show places that match at least one vibe."
        )

    sort_choice = st.radio(
        "Sort results by",
        ["Best use of budget", "Cheapest first", "Best season first"],
        horizontal=True,
        help="'Best use of budget' shows the trips that use the most of your budget without going over.",
    )

    month_number = None if month_choice == "Any month" else MONTHS.index(month_choice) + 1
    matches = find_destinations(DESTINATIONS, budget, nights, style, month_number, chosen_vibes)

    if sort_choice == "Best use of budget":
        matches.sort(key=lambda match: match["budget_used"], reverse=True)
    elif sort_choice == "Cheapest first":
        matches.sort(key=lambda match: match["total"])
    else:
        matches.sort(key=lambda match: (not match["in_season"], -match["budget_used"]))

    if not matches:
        st.warning(
            f"No destinations fit ${budget:,} for {nights} nights with a {style} travel style. "
            "Try raising your budget, shortening the trip, choosing a cheaper travel style, or removing vibe filters."
        )
    else:
        top = matches[0]
        st.success(
            f"**{len(matches)}** of {len(DESTINATIONS)} destinations fit your budget. "
            f"Top pick: **{top['destination']['name']}, {top['destination']['country']}** "
            f"at about **${top['total']:,.0f}** (${budget - top['total']:,.0f} left over)."
        )

        rows = [
            {
                "Destination": match["destination"]["name"],
                "Country": match["destination"]["country"],
                "Estimated total": match["total"],
                "Left over": budget - match["total"],
                "Budget used": match["budget_used"],
                "Best months": format_months(match["destination"]["best_months"]),
                "In season": "Yes" if match["in_season"] else ("No" if month_number else "—"),
                "Vibes": ", ".join(match["destination"]["vibes"]),
            }
            for match in matches
        ]
        st.dataframe(
            pd.DataFrame(rows),
            hide_index=True,
            width="stretch",
            column_config={
                "Estimated total": st.column_config.NumberColumn(format="$%.0f"),
                "Left over": st.column_config.NumberColumn(format="$%.0f"),
                "Budget used": st.column_config.ProgressColumn(format="percent", min_value=0, max_value=1),
            },
        )

# ---------- Mode 2: What will this cost? ----------
with estimate_tab:
    st.subheader("What will this cost?")
    st.write("Pick a destination and trip length to see an estimated budget by category.")

    col1, col2 = st.columns(2)
    with col1:
        labels = {f"{d['name']}, {d['country']}": d for d in DESTINATIONS}
        chosen_label = st.selectbox("Destination", sorted(labels))
        destination = labels[chosen_label]
    with col2:
        trip_nights = st.slider("Number of nights", min_value=1, max_value=21, value=5, key="estimate_nights")

    breakdown = estimate_breakdown(destination, trip_nights, style)
    total = sum(breakdown.values())
    days = trip_nights + 1

    metric1, metric2, metric3 = st.columns(3)
    metric1.metric("Estimated total", f"${total:,.0f}")
    metric2.metric("Per day", f"${total / days:,.0f}", help=f"{trip_nights} nights = {days} days")
    metric3.metric("Travel style", style)

    best = format_months(destination["best_months"])
    st.info(f"Best time to visit {destination['name']}: **{best}**.")

    breakdown_df = pd.DataFrame(
        {"Category": list(breakdown), "Cost": list(breakdown.values())}
    )
    breakdown_df["Share of total"] = breakdown_df["Cost"] / total

    chart_col, table_col = st.columns([3, 2])
    with chart_col:
        st.markdown("**Cost by category**")
        bars = (
            alt.Chart(breakdown_df)
            .mark_bar(color="#2a78d6", cornerRadiusEnd=4, height=28)
            .encode(
                x=alt.X("Cost:Q", title="Estimated cost (USD)", axis=alt.Axis(format="$,.0f", grid=False)),
                y=alt.Y("Category:N", sort="-x", title=None),
                tooltip=[
                    alt.Tooltip("Category:N"),
                    alt.Tooltip("Cost:Q", format="$,.0f"),
                    alt.Tooltip("Share of total:Q", format=".0%"),
                ],
            )
        )
        labels_layer = bars.mark_text(align="left", dx=6).encode(
            text=alt.Text("Cost:Q", format="$,.0f"), color=alt.value("gray")
        )
        st.altair_chart((bars + labels_layer).properties(height=220), width="stretch")
    with table_col:
        st.markdown("**Breakdown**")
        st.dataframe(
            breakdown_df.sort_values("Cost", ascending=False),
            hide_index=True,
            width="stretch",
            column_config={
                "Cost": st.column_config.NumberColumn(format="$%.0f"),
                "Share of total": st.column_config.NumberColumn(format="percent"),
            },
        )

    multiplier = STYLE_MULTIPLIERS[style]
    with st.expander("How is this calculated?"):
        st.markdown(
            f"""
- **Flight:** round trip from NYC = ${destination['flight']:,}
- **Lodging:** ${destination['hotel_per_night']} per night × {trip_nights} nights × {multiplier} ({style}) = ${breakdown['Lodging']:,.0f}
- **Food:** ${destination['food_per_day']} per day × {multiplier} ({style}) × {days} days = ${breakdown['Food']:,.0f}
- **Activities:** ${destination['activities_per_day']} per day × {days} days = ${breakdown['Activities']:,.0f}
"""
        )
