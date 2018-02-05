#Rebecca TeKolste
#Problem 2

class Node:
    def __init__(self, name, cost, utility):
        self.name = name
        self.cost = cost
        self.utility = utility
    def get_expected_cost(self):
        pass

    def get_expected_utility(self):
        pass

class ChanceNode(Node):
    def __init__(self, name, cost, probs, future_nodes, utility):
        Node.__init__(self, name, cost, utility)
        self.probs = probs
        self.future_nodes = future_nodes

    def get_expected_cost(self):
        exp_cost = self.cost #start by the known quantity: the cost of visiting this node here.
        i = 0 #just an index
        for thisNode in self.future_nodes:
            exp_cost+= self.probs[i] * thisNode.get_expected_cost()
            i+=1
        return exp_cost
    def get_expected_utility(self):
        exp_utility=0
        i=0
        for thisNode in self.future_nodes:
            exp_utility+= self.probs[i] * thisNode.get_expected_utility()
            i+=1
        return exp_utility

class TerminalNode(Node):
    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)
    def get_expected_cost(self):
        return self.cost
    def get_expected_utility(self):
        return self.utility

class DecisionNode(Node):
    def __init__(self, name, cost, future_nodes, utility):
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes # list of future node objects
    def get_expected_cost(self):
        #This is the expected cost of the attached future nodes
        """"return the expected cost of the associated future nodes"""
        outcomes = dict( )
        for thisNode in self.futureNodes:
            outcomes[thisNode.name] = thisNode.get_expected_cost()
        return outcomes
    def get_expected_utility(self):
        #This is the expected utility of the attached future nodes
        """"return the expected utility of the associated future nodes"""
        utilities = dict( )
        for thisNode in self.futureNodes:
            utilities[thisNode.name] = thisNode.get_expected_utilty()
        return utilities


##creating a terminal node T1
T1 = TerminalNode("T1", cost = 10, utility=0.9)
T2 = TerminalNode("T2", cost = 20, utility=0.8)
T3 = TerminalNode("T3", cost = 30, utility=0.7)
T4 = TerminalNode("T4", cost = 40, utility=0.6)
T5 = TerminalNode("T5", cost = 50, utility=0.5)


C2 = ChanceNode("C2", cost = 35, probs=[0.7, 0.3], future_nodes=[T1, T2], utility=0)
C1 = ChanceNode("C1", cost = 25, probs=[0.2, 0.8], future_nodes=[C2, T3], utility=0)
C3 = ChanceNode("C3", cost = 45, probs=[0.1, 0.9], future_nodes=[T4, T5], utility=0)
D1 = DecisionNode("D1", 0, [C1,C3], utility=0)

print(C1.get_expected_cost())
print(C3.get_expected_cost())
print(C1.get_expected_utility())
print(C3.get_expected_utility())
