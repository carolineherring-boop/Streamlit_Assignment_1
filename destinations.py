"""Curated cost data for each destination.

All prices are approximate, in US dollars, for a mid-range traveler:
- flight: round-trip economy flight from New York City
- hotel_per_night: a mid-range hotel or private rental for one night
- food_per_day: three meals a day
- activities_per_day: tours, museums, transport, and other daily costs
- best_months: months (1 = January ... 12 = December) with the best weather
- vibes: the kinds of trip the destination is good for

These are planning estimates, not live prices. In the final version this data
will live in a Supabase `destinations` table.
"""

DESTINATIONS = [
    {"name": "Cancún", "country": "Mexico", "flight": 450, "hotel_per_night": 140, "food_per_day": 50, "activities_per_day": 45, "best_months": [12, 1, 2, 3, 4], "vibes": ["Beach", "Relaxation"]},
    {"name": "Mexico City", "country": "Mexico", "flight": 400, "hotel_per_night": 90, "food_per_day": 35, "activities_per_day": 30, "best_months": [3, 4, 5, 10, 11], "vibes": ["City", "Food", "Culture"]},
    {"name": "San Juan", "country": "Puerto Rico", "flight": 350, "hotel_per_night": 170, "food_per_day": 60, "activities_per_day": 40, "best_months": [12, 1, 2, 3, 4], "vibes": ["Beach", "Culture"]},
    {"name": "Montreal", "country": "Canada", "flight": 300, "hotel_per_night": 150, "food_per_day": 60, "activities_per_day": 35, "best_months": [6, 7, 8, 9], "vibes": ["City", "Food"]},
    {"name": "Miami", "country": "USA", "flight": 250, "hotel_per_night": 220, "food_per_day": 75, "activities_per_day": 50, "best_months": [12, 1, 2, 3, 4], "vibes": ["Beach", "Nightlife"]},
    {"name": "New Orleans", "country": "USA", "flight": 300, "hotel_per_night": 170, "food_per_day": 65, "activities_per_day": 40, "best_months": [2, 3, 4, 10, 11], "vibes": ["Food", "Nightlife", "Culture"]},
    {"name": "Denver", "country": "USA", "flight": 320, "hotel_per_night": 160, "food_per_day": 60, "activities_per_day": 45, "best_months": [6, 7, 8, 9], "vibes": ["Nature", "Adventure"]},
    {"name": "San Francisco", "country": "USA", "flight": 400, "hotel_per_night": 250, "food_per_day": 80, "activities_per_day": 50, "best_months": [9, 10], "vibes": ["City", "Food"]},
    {"name": "Honolulu", "country": "USA", "flight": 800, "hotel_per_night": 260, "food_per_day": 80, "activities_per_day": 60, "best_months": [4, 5, 9, 10], "vibes": ["Beach", "Nature", "Relaxation"]},
    {"name": "Punta Cana", "country": "Dominican Republic", "flight": 450, "hotel_per_night": 160, "food_per_day": 55, "activities_per_day": 40, "best_months": [12, 1, 2, 3, 4], "vibes": ["Beach", "Relaxation"]},
    {"name": "San José", "country": "Costa Rica", "flight": 550, "hotel_per_night": 100, "food_per_day": 35, "activities_per_day": 50, "best_months": [12, 1, 2, 3, 4], "vibes": ["Nature", "Adventure"]},
    {"name": "Cartagena", "country": "Colombia", "flight": 500, "hotel_per_night": 110, "food_per_day": 35, "activities_per_day": 35, "best_months": [12, 1, 2, 3], "vibes": ["Beach", "Culture"]},
    {"name": "Lima", "country": "Peru", "flight": 700, "hotel_per_night": 85, "food_per_day": 35, "activities_per_day": 40, "best_months": [5, 6, 7, 8, 9], "vibes": ["Food", "Culture", "Adventure"]},
    {"name": "Buenos Aires", "country": "Argentina", "flight": 1000, "hotel_per_night": 80, "food_per_day": 35, "activities_per_day": 30, "best_months": [3, 4, 5, 9, 10, 11], "vibes": ["City", "Food", "Nightlife"]},
    {"name": "Reykjavík", "country": "Iceland", "flight": 550, "hotel_per_night": 200, "food_per_day": 80, "activities_per_day": 70, "best_months": [6, 7, 8], "vibes": ["Nature", "Adventure"]},
    {"name": "London", "country": "United Kingdom", "flight": 700, "hotel_per_night": 220, "food_per_day": 70, "activities_per_day": 50, "best_months": [5, 6, 7, 8, 9], "vibes": ["City", "Culture"]},
    {"name": "Paris", "country": "France", "flight": 750, "hotel_per_night": 210, "food_per_day": 75, "activities_per_day": 50, "best_months": [4, 5, 6, 9, 10], "vibes": ["City", "Food", "Culture"]},
    {"name": "Barcelona", "country": "Spain", "flight": 750, "hotel_per_night": 160, "food_per_day": 55, "activities_per_day": 40, "best_months": [5, 6, 9, 10], "vibes": ["Beach", "City", "Nightlife"]},
    {"name": "Lisbon", "country": "Portugal", "flight": 650, "hotel_per_night": 130, "food_per_day": 45, "activities_per_day": 35, "best_months": [4, 5, 6, 9, 10], "vibes": ["City", "Food", "Culture"]},
    {"name": "Rome", "country": "Italy", "flight": 800, "hotel_per_night": 170, "food_per_day": 60, "activities_per_day": 45, "best_months": [4, 5, 6, 9, 10], "vibes": ["City", "Food", "Culture"]},
    {"name": "Athens", "country": "Greece", "flight": 850, "hotel_per_night": 120, "food_per_day": 45, "activities_per_day": 40, "best_months": [4, 5, 6, 9, 10], "vibes": ["Beach", "Culture"]},
    {"name": "Prague", "country": "Czech Republic", "flight": 800, "hotel_per_night": 100, "food_per_day": 40, "activities_per_day": 30, "best_months": [5, 6, 9], "vibes": ["City", "Culture", "Nightlife"]},
    {"name": "Marrakech", "country": "Morocco", "flight": 850, "hotel_per_night": 80, "food_per_day": 30, "activities_per_day": 35, "best_months": [3, 4, 5, 10, 11], "vibes": ["Culture", "Adventure"]},
    {"name": "Tokyo", "country": "Japan", "flight": 1300, "hotel_per_night": 160, "food_per_day": 50, "activities_per_day": 45, "best_months": [3, 4, 10, 11], "vibes": ["City", "Food", "Culture"]},
    {"name": "Bangkok", "country": "Thailand", "flight": 1200, "hotel_per_night": 60, "food_per_day": 25, "activities_per_day": 30, "best_months": [11, 12, 1, 2], "vibes": ["City", "Food", "Nightlife"]},
    {"name": "Bali", "country": "Indonesia", "flight": 1400, "hotel_per_night": 70, "food_per_day": 25, "activities_per_day": 35, "best_months": [5, 6, 7, 8, 9], "vibes": ["Beach", "Nature", "Relaxation"]},
]

VIBES = sorted({vibe for destination in DESTINATIONS for vibe in destination["vibes"]})
