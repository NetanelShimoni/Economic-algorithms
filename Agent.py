from typing import List


class Agent:
    array1 = []

    def value(self, option: int) -> float:
        return self.array1[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    j = 0
    for i in agents:
        print(i.array1)
        if i.value(option1) > i.value(option2):
            return False

    return True
def isParetoOptimal(agents:List[Agent], option:int,  allOptions:List[int])->bool:
    for i in agents:
        for j in allOptions:
         if  i.value(option)> i.value(j):
            return False
    return True


a = Agent()
b = Agent()
a.array1 = [20, 3, 80, 96]
b.array1 = [40, 13, 90, 65]
my_agent = []
list_int=[0,1,3]
my_agent.append(a)
my_agent.append(b)

print(isParetoImprovement(my_agent, 1, 2))
print("#############################")
print(isParetoOptimal(my_agent,1,list_int))

