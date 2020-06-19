# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def generalSearch(problem, data_structure):
    visited = []
    path = list()
    data_structure.push([(problem.getStartState(), "Stop", 0)])

    print
    "Start: ", problem.getStartState()

    while not data_structure.isEmpty():
        path = data_structure.pop()
        current_state = path[-1][0]
        print
        "Going direction ", path[-1][1]
        print
        "State is ", current_state

        if problem.isGoalState(current_state):
            return [state[1] for state in path][1:]

        if current_state not in visited:
            visited.append(current_state)

            for successor in problem.getSuccessors(current_state):
                if successor[0] not in visited:
                    successorPath = path[:]
                    successorPath.append(successor)
                    data_structure.push(successorPath)
    return []

def depthFirstSearch(problem):
    """
    Najpre pretrazuje najdublje cvorove u stablu.

    Isprobajte i koristite sledece:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    stack = util.Stack()
    return generalSearch(problem, stack)

def breadthFirstSearch(problem):
    """Najpre pretrazuje najplice cvorove u stablu."""
    queue = util.Queue()
    return generalSearch(problem, queue)

def nullHeuristic(state, problem=None):
    """
    Heuristicka funkcija procenjuje cenu od trenutnog stanja do najblizeg sledeceg stanja u prostoru pretrage.
    Ova heuristika je trivijalna.
    """
    return 0
def uniformCostSearch(problem):
    "Search the node of least total cost first. "

    # Running UCS is the same as running A* Search with a null heuristic,
    # so simplify the calls by just using aStarSearch.
    return aStarSearch(problem)

def aStarSearch(problem, heuristic=nullHeuristic):
    """Najpre pretrazuje cvor koji ima najnizu kombinovanu cenu i heuristiku."""

    cost = lambda path: problem.getCostOfActions([state[1] for state in path][1:]) + heuristic(path[-1][0], problem)

    priorityQueue = util.PriorityQueueWithFunction(cost)
    return generalSearch(problem, priorityQueue)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
