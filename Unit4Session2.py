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