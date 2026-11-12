# Assignment 2 Progress Summary

**GitHub repository:** https://github.com/carolineherring-boop/Streamlit_Assignment_1

**Project:** Trip Budget Planner

## Features Added
Since Assignment 1, the app has grown from a title into a working trip budget tool with two modes, organized in tabs:

- **"Where can I go?"**: a budget slider, number-of-nights input, and optional travel month and vibe filters. The app shows every destination that fits the budget in a table with the estimated total, money left over, a "budget used" progress bar, best months, and an in-season flag. Results can be sorted by best use of budget, cheapest first, or best season first, and a summary message highlights the top pick (or suggests changes when nothing fits).
- **"What will this cost?"**: pick a destination and number of nights to see the estimated total, cost per day, best time to visit, and a bar chart and table breaking the cost into flight, lodging, food, and activities. An expandable section shows the calculation step by step.
- **Travel style**: a sidebar dropdown (Budget / Mid-range / Comfort) that multiplies hotel and food costs by 0.6× / 1.0× / 1.6× and updates both modes.
- **Destination data**: 26 destinations with approximate costs, best months, and vibes.
- **Code organization**: the code is split into `app.py` (layout and widgets), `budget.py` (calculations), and `destinations.py` (data).

## What Still Remains
- Move the destination data into a Supabase database and add `trips` and `expenses` tables
- Let users save a trip and view saved trips on a "My Trips" page
- Add expense logging with a progress bar and budget vs. actual spending by category
- Reorganize the app into separate Streamlit pages
- Optionally add a simple login so saved trips stay private

## Challenges
- **Keeping the cost formula consistent:** both modes and the travel style setting needed to use the same calculation, so I put it in one shared module (`budget.py`) instead of repeating it in the app.
- **Nights vs. days:** hotels are paid per night, but food and activities are paid per day. I decided a trip of N nights has N + 1 days and explained this in the app.
- **Collecting realistic cost data:** without live price APIs, I had to choose reasonable average costs for each destination, so the app labels them as planning estimates.
- **Choosing the right chart:** I originally planned a pie chart for the cost breakdown, but a sorted bar chart makes it easier to compare categories, so I used a bar chart plus a table showing each category's share.
- **No results:** some combinations of budget, trip length, and filters match nothing, so the app shows a message with suggestions instead of an empty table.
