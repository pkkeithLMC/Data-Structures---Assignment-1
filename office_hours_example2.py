"""Office-hours example: match a student with campus activities.

This program practices the same Python and data-structure skills as the
product-recommendation assignment, but uses a different problem and dataset.
"""


# SKILL: Store related records in a list of dictionaries.
# SKILL: Recognize that each dictionary contains a name and a collection of tags.
activities = [
    {"name": "Robotics Club", "features": ["building", "coding", "teamwork"]},
    {"name": "Nature Photography Walk", "features": ["outdoors", "creative", "quiet"]},
    {"name": "Campus Game Night", "features": ["social", "strategy", "indoor"]},
    {"name": "Community Garden", "features": ["outdoors", "hands-on", "teamwork"]},
    {"name": "Creative Writing Circle", "features": ["creative", "writing", "quiet"]},
    {"name": "Intramural Volleyball", "features": ["fitness", "social", "teamwork"]},
    {"name": "Python Study Group", "features": ["coding", "strategy", "social"]},
    {"name": "Meditation Hour", "features": ["quiet", "wellness", "indoor"]},
]


# SKILL: Iterate over a list and inspect dictionary data.
print("Available activities:")
for activity in activities:
    print(f"- {activity['name']}: {', '.join(activity['features'])}")


# SKILL: Create an empty list that will grow as input is collected.
student_interests = []

# SKILL: Use a sentinel-controlled while loop.
# SKILL: Read keyboard input, normalize text, and append values to a list.
answer = "Y"
while answer != "N":
    interest = input("\nEnter an interest: ").strip().lower()

    # SKILL: Use a conditional to avoid storing an empty response.
    if interest:
        student_interests.append(interest)

    answer = input("Add another interest? (Y/N): ").strip().upper()


# SKILL: Convert a list to a set to remove duplicate values.
unique_interests = set(student_interests)


# SKILL: Copy and transform structured data without changing the original data.
# SKILL: Convert tag lists to sets so set operations can be used later.
prepared_activities = []
for activity in activities:
    prepared_activity = {
        "name": activity["name"],
        "features": set(activity["features"]),
    }
    prepared_activities.append(prepared_activity)


# SKILL: Define a reusable function with parameters and a return value.
# SKILL: Use set intersection to find values shared by two sets.
def shared_features(activity_features, interests):
    """Return the set of features shared by an activity and a student."""
    return activity_features.intersection(interests)


# SKILL: Decompose a larger problem by calling one function from another.
# SKILL: Loop through every dictionary and accumulate results in a list.
# SKILL: Use len() to convert a set of matches into a numeric score.
# SKILL: Filter out records with zero matches.
def rank_activities(activity_list, interests):
    """Return matching activities ordered from strongest to weakest match."""
    ranked = []

    for activity in activity_list:
        matches = shared_features(activity["features"], interests)

        if len(matches) > 0:
            # Each result is a list containing:
            # [match count, activity name, set of matching features]
            # Putting the number first allows Python to sort by it first.
            ranked.append([len(matches), activity["name"], matches])

    # SKILL: Sort a list in place from greatest to least.
    # Because the match count is first in each inner list, Python compares it first.
    ranked.sort(reverse=True)
    return ranked


# SKILL: Call a function with the correctly prepared data type.
recommendations = rank_activities(prepared_activities, unique_interests)


# SKILL: Use conditionals to handle both matches and no-match results.
# SKILL: Traverse returned data and format readable output.
print("\nYour activity matches:")
if recommendations:
    for result in recommendations:
        match_count = result[0]
        activity_name = result[1]
        matching_features = result[2]
        match_text = ", ".join(sorted(matching_features))
        print(f"{activity_name}: {match_count} match(es) [{match_text}]")
else:
    print("No activities matched those interests.")


# SKILL: Explain design choices and consider how a solution might scale.
# DISCUSSION QUESTIONS FOR OFFICE HOURS:
# 1. Why collect interests in a list first, but compare them as a set?
# 2. What is the data type returned by shared_features()?
# 3. Why does rank_activities() call shared_features() instead of repeating its code?
# 4. What would break if student_interests were passed to rank_activities()?
# 5. When two activities have the same match count, how does Python break the tie?
# 6. What might change if the program contained thousands of activities?
