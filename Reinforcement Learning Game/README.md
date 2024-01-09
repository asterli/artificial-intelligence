**Instructions for the lab:**

Task A: Implement a Q-learning agent to walk in the grid world we saw in class. The agent learns by trial and
error from interactions with the environment through its update(state, action, nextState, reward) method. A
stub of a Q-learner is specified in QLearningAgent in qlearningAgents.py, and you can select it with the
option '-a q'.
You will implement the update, computeValueFromQValues, getQValue,
and computeActionFromQValues functions in qlearningAgents.py.
Note: For computeActionFromQValues, you should break ties randomly for better behavior.
The random.choice() function will help. In a particular state, actions that your agent hasn’t seen before still
have a Q-value, specifically a Q-value of zero.
Important: Make sure that in your computeValueFromQValues and computeActionFromQValues functions,
you only access Q values by calling getQValue.
Task A – Experiment 1 With the Q-learning update in place, you can watch your Q-learner learn under
manual control, using the keyboard:
python gridworld.py -a q -k 4 -m --noise 0.0
Note: -k will control the number of episodes your agent gets to learn, -m means you manually control Pacman’s
actions, and --noise 0.0 means there is no randomness (it’s a deterministic game). Please manually steer
Pacman north and then east along the optimal path for four episodes, and you should see the following updated
Q-values:
Hint:
• In computeValueFromQValues and computeActionFromQValues, the available actions shall be
obtained by: self.getLegalActions(state)
• Watch how the agent learns about the state it was just in, not the one it moves to.
Task A – Experiment 2 Run the command:
python autograder.py -q q3
Your code is expected to pass all four test_cases of the above command.
Task B: Keep the modified code in Task A. Now, you will continue to modify the “def getAction(self, state):”
function in the same qlearningAgents.py file. This function computes the action to take in the current state.
There is a parameter self.epsilon, which is a probability. With probability self.epsilon, the agent should take a
random action of all legal actions available in that state. With probability 1- self.epsilon, the agent will take
the best policy action obtained by the computeActionFromQValues function.
Task B – Experiment 1 Run the following command, and observe how the Q-learner updates the Q-state values
for 100 episodes.
python gridworld.py -a q -k 100
Task B – Experiment 2 Run the following command and observe how the crawler bot learns to move to the
right. You can decrease the “Step Delay” to 0.0125 by pressing the top-left “-” button, so that you will see the
displayed results sooner.
python crawler.py