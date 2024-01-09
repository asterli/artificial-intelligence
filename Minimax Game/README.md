**Instructions for the lab:**

In this assignment, you will design a minimax algorithm for Pacman (player-MAX), who plays a
game with three ghosts (player-MINs). The game tree will have MAX nodes and MIN nodes. In general, MAX
nodes will call a “max” function to collect the largest value from its successors, and MIN nodes will call a
“min” function to collect the minimum value from its successors.

Implement the following function in Class MinimaxAgent, in multiAgents.py

def getAction(self, gameState):<br />
…<br />
this function will<br />
• recursively call a “max” function and a “min” function.<br />
• propagate the “leaf” node values to upper layers, until the root node is reached.<br />
• finally, return the best action for player-max (Pacman) at the root node<br />

**Task: Minimax Agent**<br />
Now you will write an adversarial search agent in the provided MinimaxAgent class stub
in multiAgents.py. Your minimax agent should work with any number of ghosts. In particular, your
minimax tree will have multiple min layers (one for each ghost) for every max layer.
Your code should also expand the game tree to an arbitrary depth. Score the leaves of your minimax
tree with the supplied scoreEvaluationFunction. MinimaxAgent extends MultiAgentSearchAgent,
which gives access to self.depth (the number of search plies of the game tree). A single search ply
(self.depth=1) is considered to be one Pacman move and all the ghosts’ responses, so a search with
self.depth=2 will involve Pacman and each ghost moving two times.
Make sure your minimax code makes reference to variable self.depth where appropriate as this variable is
populated in response to command line options.
