# Trip Budget Planner

## Student Name
Caroline Herring

## App Description
Trip Budget Planner is a Streamlit app that helps travelers find trips that fit their budget and understand what a trip will really cost. It has two modes:

- **"Where can I go?"** The user sets a total budget and number of nights, and can optionally choose a travel month and one or more vibes (Beach, City, Food, Nature, and so on). The app lists every destination whose estimated cost fits the budget, showing how much of the budget each trip uses, how much is left over, and whether the chosen month is in the destination's best season.
- **"What will this cost?"** The user picks a destination and number of nights, and the app estimates the total cost, the cost per day, and a breakdown by category (flight, lodging, food, activities) with a bar chart and a table.

A **travel style** setting (Budget / Mid-range / Comfort) applies to both modes and scales hotel and food costs, so estimates match how the user likes to travel.

Every estimate uses one formula, where a trip of N nights has N + 1 days:

```
estimated_cost = flight
               + hotel_per_night × nights × style_multiplier
               + (food_per_day × style_multiplier + activities_per_day) × days
```

The app currently uses a built-in table of 26 destinations with approximate costs (round-trip flights from New York City). In the final version, this data will move to a Supabase database, and users will be able to save trips and track actual spending against the estimate.

## Intended Users
This app is for budget-conscious travelers, such as students, young professionals, and anyone planning a vacation, who have a fixed amount to spend and want to know where that money can take them. It is also for people who have already picked a destination and want a realistic cost estimate before booking, and for travelers who want an easy way to track what they actually spend during a trip.

## Current Features (Implemented)
- **Find a destination ("Where can I go?")**: budget slider, number-of-nights input, optional travel month and vibe filters
- **Ranked results table**: matching destinations with estimated total, money left over, a "budget used" progress bar, best months, and an in-season flag
- **Sorting options**: best use of budget, cheapest first, or best season first
- **Top pick summary**: a message showing how many destinations fit and the best match, or tips for adjusting the search when nothing fits
- **Estimate a trip ("What will this cost?")**: pick a destination and number of nights to see the total cost, cost per day, and best time to visit
- **Cost breakdown chart and table**: estimated cost by category (flight, lodging, food, activities) with each category's share of the total
- **Travel style**: Budget / Mid-range / Comfort dropdown in the sidebar that multiplies hotel and food costs by 0.6× / 1.0× / 1.6×
- **"How is this calculated?" section**: shows the formula step by step with the actual numbers for the selected trip
- **Destination data**: 26 curated destinations with flight, hotel, food, and activity costs, best months, and vibes

## Planned Features (Final Version)
- **Supabase database**: move destination data into a `destinations` table and add `trips` and `expenses` tables
- **Save a trip**: save a destination, start date, nights, budget, and travel style from either mode
- **My Trips page**: list saved trips with budget vs. amount spent so far
- **Trip detail and expense tracking**: log expenses (category, amount, date, note) and see a progress bar plus spending by category compared with the estimate
- **Budget vs. actual chart**: compare estimated and actual spending for each category
- **Multi-page layout**: separate Streamlit pages for Find a Destination, Estimate a Trip, My Trips, and Trip Detail
- **Optional login**: simple Supabase Auth so saved trips stay private

### Planned database tables

| Table | Purpose |
|-------|---------|
| `destinations` | Curated cost data: flight from NYC, hotel per night, food per day, activities per day, best season, vibe |
| `trips` | Saved trips: destination, start date, nights, total budget, travel style |
| `expenses` | Logged spending per trip: category, amount, date, note (linked to `trips`) |

### Out of scope
Live price APIs, booking, and maps.

## Project Structure
| File | Purpose |
|------|---------|
| `app.py` | The Streamlit app: layout, input widgets, and outputs |
| `budget.py` | Cost calculations: travel style multipliers, cost breakdown, and destination search |
| `destinations.py` | The curated destination cost data |
| `requirements.txt` | Python packages needed to run the app |

## Running the App Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
