"""Trip cost calculations.

estimated_cost = flight
               + hotel_per_night × nights × style_multiplier
               + (food_per_day × style_multiplier + activities_per_day) × days

A trip of N nights has N + 1 days (for example, 3 nights = 4 days).
"""

# Travel style scales the costs that depend most on how you like to travel.
STYLE_MULTIPLIERS = {
    "Budget": 0.6,
    "Mid-range": 1.0,
    "Comfort": 1.6,
}

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def estimate_breakdown(destination, nights, style):
    """Return the estimated cost of a trip, split into categories."""
    multiplier = STYLE_MULTIPLIERS[style]
    days = nights + 1
    return {
        "Flight": destination["flight"],
        "Lodging": destination["hotel_per_night"] * nights * multiplier,
        "Food": destination["food_per_day"] * multiplier * days,
        "Activities": destination["activities_per_day"] * days,
    }


def estimate_total(destination, nights, style):
    """Return the total estimated cost of a trip."""
    return sum(estimate_breakdown(destination, nights, style).values())


def is_in_season(destination, month_number):
    """Return True if the month (1-12) is one of the destination's best months."""
    return month_number in destination["best_months"]


def find_destinations(destinations, budget, nights, style, month_number=None, vibes=None):
    """Return the destinations that fit the budget, with their estimated totals.

    month_number: only used to flag whether each trip is in season (None = any month).
    vibes: keep only destinations that match at least one selected vibe.
    """
    matches = []
    for destination in destinations:
        if vibes and not set(vibes) & set(destination["vibes"]):
            continue
        total = estimate_total(destination, nights, style)
        if total > budget:
            continue
        matches.append({
            "destination": destination,
            "total": total,
            "budget_used": total / budget,
            "in_season": month_number is not None and is_in_season(destination, month_number),
        })
    return matches
