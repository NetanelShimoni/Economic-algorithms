from typing import List
import networkx as np
import matplotlib.pyplot as plt
class Agent:
    array1 = []

    def item_value(self, item_index: int) -> float:
        return self.array1[item_index]


def envy_graph(agents: List[Agent], bundles:List[int]) -> np.Graph:
    G = np.DiGraph()
    k=0
    for i in agents:
        G.add_node(k)
        k=k+1
    for i in bundles:
        temp=agents[i];
        for a in agents:
            if(temp.item_value(i)<a.item_value(i)):
              G.add_edge(num,i)
            num=num+1
        num =0
        print("\n")
  #  for agent in agents:

    print(G.nodes)
    print(G.edges)

    np.draw(G,with_labels=0)
    return G




#########main#########
a = Agent()
b = Agent()
c = Agent()
a.array1 = [1, 2, 3]
b.array1 = [3, 1, 2]
c.array1 = [2, 3, 1]
my_agent = []
my_agent.append(a)
my_agent.append(b)
my_agent.append(c)
bund =[0,1,2]

envy_graph(my_agent,bund);
