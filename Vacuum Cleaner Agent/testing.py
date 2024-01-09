# Aster Li
from lab2 import Vacuum
import unittest

class Testlab2(unittest.TestCase):
    def test1(self):
        vac = Vacuum()
        state = ["Dirty", "Dirty", 0]
        expActions = ["Suck", "Right", "Suck"]
        expCost = 3
        while not vac.goal_test(state): # while the goal state has not been reached
            vacAction = vac.action(state)
            state = vac.update_state(state, vacAction)
        self.assertEqual(vac.actions, expActions)
        self.assertEqual(expCost, len(vac.actions))
        print("Test 1: Correct Outputs!")

    def test2(self):
        vac = Vacuum()
        state = ["Dirty", "Dirty", 1]
        expActions = ["Suck", "Left", "Suck"]
        expCost = 3
        while not vac.goal_test(state):
            vacAction = vac.action(state)
            state = vac.update_state(state, vacAction)
        self.assertEqual(vac.actions, expActions)
        self.assertEqual(expCost, len(vac.actions))
        print("Test 2: Correct Outputs!")
    def test3(self):
        vac = Vacuum()
        state = ["Clean", "Dirty", 0]
        expActions = ["Right", "Suck"]
        expCost = 2
        while not vac.goal_test(state):
            vacAction = vac.action(state)
            state = vac.update_state(state, vacAction)
        self.assertEqual(vac.actions, expActions)
        self.assertEqual(expCost, len(vac.actions))
        print("Test 3: Correct Outputs!")
    def test4(self):
        vac = Vacuum()
        state = ["Clean", "Dirty", 1]
        expActions = ["Suck"]
        expCost = 1
        while not vac.goal_test(state):
            vacAction = vac.action(state)
            state = vac.update_state(state, vacAction)
        self.assertEqual(vac.actions, expActions)
        self.assertEqual(expCost, len(vac.actions))
        print("Test 4: Correct Outputs!")
    def test5(self):
        vac = Vacuum()
        state = ["Dirty", "Clean", 0]
        expActions = ["Suck"]
        expCost = 1
        while not vac.goal_test(state):
            vacAction = vac.action(state)
            state = vac.update_state(state, vacAction)
        self.assertEqual(vac.actions, expActions)
        self.assertEqual(expCost, len(vac.actions))
        print("Test 5: Correct Outputs!")
    def test6(self):
        vac = Vacuum()
        state = ["Dirty", "Clean", 1]
        expActions = ["Left", "Suck"]
        expCost = 2
        while not vac.goal_test(state):
            vacAction = vac.action(state)
            state = vac.update_state(state, vacAction)
        self.assertEqual(vac.actions, expActions)
        self.assertEqual(expCost, len(vac.actions))
        print("Test 6: Correct Outputs!")
    def test7(self):
        vac = Vacuum()
        state = ["Clean", "Clean", 0]
        expActions = []
        expCost = 0
        while not vac.goal_test(state):
            vacAction = vac.action(state)
            state = vac.update_state(state, vacAction)
        self.assertEqual(vac.actions, expActions)
        self.assertEqual(expCost, len(vac.actions))
        print("Test 7: Correct Outputs!")
    def test8(self):
         vac = Vacuum()
         state = ["Clean", "Clean", 1]
         expActions = []
         expCost = 0
         while not vac.goal_test(state):
             vacAction = vac.action(state)
             state = vac.update_state(state, vacAction)
         self.assertEqual(vac.actions, expActions)
         self.assertEqual(expCost, len(vac.actions))
         print("Test 8: Correct Outputs!")

if __name__ == '__main__':
    unittest.main()
