# Assignment 1 Submission

**GitHub repository:** https://github.com/carolineherring-boop/Streamlit_Assignment_1

## Project Title
Trip Budget Planner

## App Description
Trip Budget Planner is a Streamlit app that helps travelers find trips that fit their budget and then track their spending once the trip is booked. In "Where can I go?" mode, the user enters a total budget, the number of nights, a departure city, and optionally a travel month and vibe, and the app suggests destinations whose estimated cost fits the budget, ranked by how well they match. In "What will this cost?" mode, the user picks a destination and trip length and gets an estimated budget broken down into flights, lodging, food, and activities, shown as a pie chart. A "travel style" setting (Budget, Mid-range, or Comfort) scales hotel and food costs so estimates match how the user likes to travel. Users can save a trip to a Supabase database and log real expenses against it, comparing actual spending with the estimate by category.

## Intended Users
Budget-conscious travelers, such as students, young professionals, and anyone planning a vacation, who have a set amount to spend and want to know where it can take them, get a realistic estimate before booking, and track what they actually spend during the trip.

## Planned Features
1. **Find a destination:** budget slider, nights, month, and vibe filters that return matching destinations with estimated totals
2. **Estimate a trip:** cost breakdown by category with a pie chart for any destination and trip length
3. **Travel style:** Budget / Mid-range / Comfort multipliers (0.6× / 1.0× / 1.6×) on hotel and food costs
4. **Save trips and track expenses:** save trips, log expenses, and view budget vs. spent with a progress bar and category breakdown
