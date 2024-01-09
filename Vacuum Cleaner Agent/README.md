Instructions for the lab:

Implement a Vacuum Cleaner Agent, according to the following figure:
<img width="631" alt="Screenshot 2024-01-09 at 12 46 17 PM" src="https://github.com/asterli/artificial-intelligence/assets/93052992/5a88c971-4b57-4572-b37a-d2ff8c4e554e">

Requirements:

• Define the “state” as a list of three elements: the 1st element specifies the status of the left square (“Clean” or “Dirty”), the 2nd element specifies the status of the right square (“Clean” or “Dirty”), and the 3rd element specifies the current location of the agent (0 for left square, 1 for right square).
• The candidate actions are “Suck”, “Left” (moving to the left square), “Right” (moving to the right square). Each action costs 1 point.
• The agent will take an action based on the current state. The agent program can update the state immediately after an action is taken. The program terminates when both squares are clean.
• Create a test case to verify your code. The test case takes two inputs: the current state, and an empty list that will store the actions; then it will generate two outputs: the sequence of actions taken by the agent to achieve the goal state, and the corresponding total cost.
• Your test case should be able to take any possible inputs, generate the corresponding outputs, and verify whether the outputs are correct or not. For example, if the outputs are correct, then your test code can print a message: “Correct Outputs!” Otherwise, it can print: “Wrong Outputs!”
• Explain in detail how your code works (for example, what each function does, and how the test case works).
