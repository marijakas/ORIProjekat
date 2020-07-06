# myAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from game import Agent, Directions
from searchProblems import PositionSearchProblem
import math
import util
import time
import search
import random
from util import manhattanDistance
"""
IMPORTANT
`agent` defines which agent you will use. By default, it is set to ClosestDotAgent,
but when you're ready to test your own agent, replace it with MyAgent
"""


def createAgents(num_pacmen, agent='MyAgent'):
    return [eval(agent)(index=i) for i in range(num_pacmen)]


class MyAgent(Agent):
    """
    Implementation of your agent.
    """


    rezervisanaHrana = []

    def initialize(self):
        """
        Intialize anything you want to here. This function is called
        when the agent is first created. If you don't need to use it, then
        leave it blank
        """

        "*** YOUR CODE HERE"

        self.svePojedeno = False
        self.actions = []


    def getAction(self, state):
        """
        Returns the next action the agent will take
        """

        # problem = MyFoodSearchProblem(state, self.index)

        if self.svePojedeno:
            return Directions.STOP
        else:

            if not self.actions:
                # actions = search.aStarSearch(problem)
                # print(actions)
                actions = search.astar(MyAgentFoodSearchProblem(state, self.index))  # implementirani a* iz search.py koji dobija taj nas food problem kao param
                self.actions = actions

            if self.actions:
                nextAction = self.actions[0]
                self.actions.remove(nextAction)
                return nextAction

            else:
                self.svePojedeno = True
                return Directions.STOP
"""
Put any other SearchProblems or search methods below. You may also import classes/methods in
search.py and searchProblems.py. (ClosestDotAgent as an example below)
"""

class MyAgentFoodSearchProblem(PositionSearchProblem):

    def __init__(self, gameState, agentIndex):
        "Stores information from the gameState.  You don't need to change this."
        # Store the food for later reference
        self.foodPositions = gameState.getFood().asList()

        # Store info for the PositionSearchProblem (no need to change this)
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition(agentIndex)
        self.costFn = lambda x: 1

        self._visited, self._visitedlist, self._expanded = {}, [], 0  # DO NOT CHANGE
        visina = gameState.getHeight()
        sirina = gameState.getWidth()
        self.dijagonala = math.sqrt(visina*visina + sirina*sirina)

        self.brojAgenata = gameState.getNumPacmanAgents()
        self.agentIndex = agentIndex

        prosecnaHrana = int(len(self.foodPositions) / self.brojAgenata) #Koliko bi svaki agent u proseku trebao da pojede hrane od preostale hrane na mapi
        #print(prosecnaHrana)
        # print(len(self.foodPositions))
        #print(self.foodPositions) #lista svih taplova sa lokacijama hrane na mapi
        self.podelaHrane = slice(agentIndex * prosecnaHrana, (agentIndex + 1) * prosecnaHrana) #podela hrane po agentima
        self.hranaPoAgentu = self.foodPositions[self.podelaHrane] #lista hrane koju ce on da jede, i to ide do indeksa hrane koja je predvidjena za sledeceg agenta. Ne uzimajuci u obriz tu hranu koja pripada sledecem.
        #print(self.foodByAgent)
        # print( agentIndex * prosecnaHrana)
        # print((agentIndex + 1) * prosecnaHrana)
    def isGoalState(self, state):
        """
            The state is Pacman's position. Fill this in with a goal test that will
            complete the problem definition.
        """
        if len(self.foodPositions) <= self.brojAgenata:
            return state in self.foodPositions
        if state in self.foodPositions:
            #dodeljen je trenutnom agentu i ni jedan drugi agent tu hranu nije postavio za svoj trenutni cilj
            if (state in self.hranaPoAgentu) and (state not in MyAgent.rezervisanaHrana):
                MyAgent.rezervisanaHrana.append(state)
                return True
            #blizu mi je hrana i ni jedan drugi agent tu hranu nije postavio za svoj trenutni cilj
            elif (manhattanDistance(state, self.startState) <= (1 + self.agentIndex) * (1 + self.agentIndex)) and (state not in MyAgent.rezervisanaHrana):
                # print("start" , self.startState) #pozicija pakmena
                # print("state" ,  state) #pozicija najblize hrane
                MyAgent.rezervisanaHrana.append(state)
                return True
            else:
                return state in self.hranaPoAgentu
        else:
            return False


class ClosestDotAgent(Agent):

    def findPathToClosestDot(self, gameState):
        """
        Returns a path (a list of actions) to the closest dot, starting from
        gameState.
        """
        # Here are some useful elements of the startState
        startPosition = gameState.getPacmanPosition(self.index)
        food = gameState.getFood()
        walls = gameState.getWalls()
        problem = AnyFoodSearchProblem(gameState, self.index)


        "*** YOUR CODE HERE ***"
        fringe = util.Queue()
        visited = []  # List of already visited nodes
        action_list = []  # List of actions taken to get to the current node
        total_cost = 0  # Cost to get to the current node
        initial = problem.getStartState()  # Starting state of the problem

        fringe.push((initial, action_list))

        while fringe:
            node, actions = fringe.pop()
            if not node in visited:
                visited.append(node)
                if problem.isGoalState(node):
                    return actions
                successors = problem.getSuccessors(node)
                for successor in successors:
                    coordinate, direction, cost = successor
                    fringe.push((coordinate, actions + [direction]))

    def getAction(self, state):
        return self.findPathToClosestDot(state)[0]
class AnyFoodSearchProblem(PositionSearchProblem):
    """
    A search problem for finding a path to any food.

    This search problem is just like the PositionSearchProblem, but has a
    different goal test, which you need to fill in below.  The state space and
    successor function do not need to be changed.

    The class definition above, AnyFoodSearchProblem(PositionSearchProblem),
    inherits the methods of the PositionSearchProblem.

    You can use this search problem to help you fill in the findPathToClosestDot
    method.
    """

    def __init__(self, gameState, agentIndex):
        "Stores information from the gameState.  You don't need to change this."
        # Store the food for later reference
        self.food = gameState.getFood()

        # Store info for the PositionSearchProblem (no need to change this)
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition(agentIndex)
        self.goal=gameState.getPacmanPosition(agentIndex)
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

        self.agentIndex=agentIndex
        self.foodPositions = self.food.asList()
    def isGoalState(self, state):
        """
        The state is Pacman's position. Fill this in with a goal test that will
        complete the problem definition.
        """
        x,y = state


        #foodPositions = self.food.asList()


        return (x, y) in self.foodPositions