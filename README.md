# Trip Budget Planner

## Student Name
Caroline Herring

## App Description
Trip Budget Planner is a Streamlit app that helps people plan trips that fit their budget and then stick to it. It works in two modes. 
In **"Where can I go?"** mode, the user enters a total budget, trip length, departure city, and optionally a travel month and vibe (beach, city, nature, and so on), and the app suggests destinations that fit, ranked by how well they match. 
In **"What will this cost?"** mode, the user picks a destination and a number of days, and the app estimates the budget broken down by category (flights, lodging, food, activities). Once a trip is chosen, the user can save it and log actual spending against the estimate, so the app works as a budget tracker and not just a calculator.

Data will be stored in a Supabase database with three tables:

| Table | Purpose |
|-------|---------|
| `destinations` | Curated cost data: flight from NYC, hotel per night, food per day, activities per day, best season, vibe |
| `trips` | Saved trips: destination, start date, nights, total budget, travel style |
| `expenses` | Logged spending per trip: category, amount, date, note (linked to `trips`) |

The core estimate is:

```
estimated_cost = flight
               + hotel_per_night × nights × style_multiplier
               + (food_per_day × style_multiplier + activities_per_day) × days
```

## Intended Users
This app is for budget-conscious travelers, such as students, young professionals, and anyone planning a vacation, who have a fixed amount to spend and want to know where that money can take them. It is also for people who have already picked a destination and want a realistic cost estimate before booking, and for travelers who want an easy way to track what they actually spend during a trip.

## Planned Features
- **Find a destination:** budget slider, number of nights, month, and vibe filters that return matching destinations with estimated totals, sorted by how much of the budget they use or by whether it is the destination's best season
- **Estimate a trip:** pick a destination and number of nights to see a cost breakdown by category, with a pie chart
- **Travel style:** choose Budget / Mid-range / Comfort, which multiplies hotel and food costs (0.6× / 1.0× / 1.6×) to make estimates more personal
- **Save trips:** store chosen trips in Supabase and view them on a "My Trips" page showing budget vs. amount spent so far
- **Trip detail and expense tracking:** log expenses for a trip and see a progress bar plus spending by category compared with the estimate

### Scope
- **MVP:** destinations table (20–30 places), "Where can I go?" search, cost estimator, save a trip
- **Nice to have:** expense logging, budget vs. actual chart, travel style, season filter
- **Out of scope:** live price APIs, booking, maps

## Running the App Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
