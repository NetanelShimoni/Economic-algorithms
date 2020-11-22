from typing import List
import networkx as np
import matplotlib.pyplot as plt


class Agent:
    array1 = []

    def item_value(self, item_index: int) -> float:
        return self.array1[item_index]


def envy_graph(agents: List[Agent], bundles: List[int]) -> np.Graph:
    G = np.DiGraph()
    k = 0
    for i in agents:
        G.add_node(k)
        k = k + 1
    for i in bundles:
        temp = agents[i];
        num = 0
        for a in agents:
            if (temp.item_value(i) < a.item_value(i)):
                G.add_edge(num, i)
            num = num + 1
        print("\n")
    #  for agent in agents:

    np.draw(G, with_labels=1)
    return G


#########main#########
a = Agent()
b = Agent()
c = Agent()

####example 1
a.array1 = [1, 2, 3]
b.array1 = [3, 1, 2]
c.array1 = [2, 3, 1]
my_agent = []
my_agent.append(a)
my_agent.append(b)
my_agent.append(c)
bund = [0, 1, 2]

# envy_graph(my_agent,bund);


##example 2

d = Agent()
e = Agent()
f = Agent()

a.array1 = [2, 2, 2, 2, 2, 2]
b.array1 = [2, 2, 2, 2, 2, 2]
c.array1 = [2, 2, 2, 2, 2, 2]
d.array1 = [2, 2, 2, 2, 2, 2]
e.array1 = [2, 2, 2, 2, 2, 2]
f.array1 = [2, 2, 2, 2, 2, 2]
my_agent = []
my_agent.append(a)
my_agent.append(b)
my_agent.append(c)
my_agent.append(d)
my_agent.append(e)
my_agent.append(f)
bund = [0, 1, 2, 3, 4, 5]
print(a.array1, "\n", b.array1, "\n", c.array1, "\n", d.array1, "\n", e.array1, "\n", f.array1)
# envy_graph(my_agent,bund);

##example 3
a.array1 = [1, 2, 3, 4]
b.array1 = [5, 6, 7, 8]
c.array1 = [9, 10, 11, 12]
d.array1 = [13, 14, 15, 16]
my_agent = []

my_agent.append(a)
my_agent.append(b)
my_agent.append(c)
my_agent.append(d)
bund = [0, 1, 2, 3]

# envy_graph(my_agent,bund);

##example 4
a.array1 = [1, 2, 3]
b.array1 = [2, 2, 2]
c.array1 = [1, 3, 2]
my_agent = []

my_agent.append(a)
my_agent.append(b)
my_agent.append(c)
bund = [0, 1, 2]

envy_graph(my_agent, bund)

