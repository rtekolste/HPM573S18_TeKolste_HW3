class ChanceNode(Node):
    def __init__(self, name, cost,  probs, future_nodes, utility):
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
