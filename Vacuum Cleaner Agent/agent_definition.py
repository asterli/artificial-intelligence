# Aster Li
class Vacuum:

    def __init__(self):
        self.actions = []
    
    def goal_test(self, state):
        if state[0] == "Clean" and state[1] == "Clean": # both rooms are clean
            return True
        else:
            return False
        
    def action(self, state):
        if state[state[2]] == "Dirty": # the current room the agent is in is dirty
            return "Suck"
        elif state[2] == 1: # the agent is in the right room and its clean
            return "Left"
        else: # the agent is in the left room and its clean
            return "Right"
        
    def update_state(self, state, action):
        if action == "Suck": # change the room status to "clean" if the robot just sucked
            state[state[2]] = "Clean"
        elif action == "Left": # change the position status of the robot to room 0
            state[2] = 0
        else: # change the position status of the robot to room 1
            state[2] = 1
        self.actions.append(action) # keep the array of actions that the robot performed
        return state