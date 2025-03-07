# Advanced Problem Set Version 1 - Problem 3: Track Scene Transitions
def track_scene_transitions(scenes):
    """
    U - Understand
    - print out the transitions from the current scene to the next

    M - Match
    - queue

    P - Plan
    iterate once over the array
    process 2 adjacent elements at a time

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n) where n is the size of scenes
    - SC: O(1)
    """

    n = len(scenes)
    for i in range(n - 1):
        curr, next = scenes[i], scenes[i + 1]
        print("Transition from", curr, "to", next)
    
scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)

# Advanced Problem Set Version 2 - Problem 2: Find Most Wasted Food Item
def find_most_wasted_food_item(waste_records):
    """
    U - Understand
    - identify the food items that was wasted the most
    - no lists will be empty

    M - Match
    - arrays

    P - Plan
    variables:
    - res (most wasted current food)

    loop through the records
        get the total for the current food
        update res if necessary
    
    return res

    I - Implement
    - see code below

    R - Review
    - see test cases

    E - Evaluate
    """

    res = "" # most wasted food to return
    max_waste = 0 # amount of most wasted food
    for food, amounts in waste_records.items():
        total = sum(amounts)
        if total > max_waste:
            res = food
            max_waste = total

    return res

waste_records1 = {
    "Apples": [200, 150, 50],
    "Bananas": [100, 200, 50],
    "Carrots": [150, 100, 200],
    "Tomatoes": [50, 50, 50]
}
result = find_most_wasted_food_item(waste_records1)
# print(result)
assert result == "Carrots"

waste_records2 = {
    "Bread": [300, 400],
    "Milk": [200, 150],
    "Cheese": [100, 200, 100],
    "Fruits": [400, 100]
}
result = find_most_wasted_food_item(waste_records2)
assert result == "Bread"