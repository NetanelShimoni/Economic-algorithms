from typing import List
import doctest




class Agent:
    array1 = [] # num of option

    def item_value(self, item_index: int) -> float:
        return self.array1[item_index]





def vcg(agents: List[Agent], num_options:int):
    """ DOC-TEST  !!!
       >>> vcg(my_agent1, 3)
       The chosen option is  1
       Agent # 0 pays 0
       Agent # 1 pays 2
       Agent # 2 pays 1

       >>> vcg(my_agent2,3)
       The chosen option is  1
       Agent # 0 pays 0
       Agent # 1 pays 7
       Agent # 2 pays 0

       """
    sufi = 0
    maxi = -1100000
    index = 0
    size=len(agents)
    for i in range(0,num_options):  #find a max hamdani
        sufi = 0
        for a in agents:
            sufi = sufi + a.item_value(i)
        if(sufi>maxi):
            maxi=sufi
            index =i
    sum = 0
    num = 0
    max_end = -100000
    pay = 0
    print("The chosen option is ", (index))
    for k in range(0,size): # Calculate for each the amount without him
     for i in range(0,num_options):
        sum = 0
        for j in range(0,size):
               sum= sum + agents[j].item_value(i)
        sum= sum - agents[num].item_value(i) # without agent[num]
        if (index==i):
         pay=sum
        if(sum>max_end):
            max_end=sum
     print("Agent #",k ,"pays",(max_end-pay)) #Subtract the amounts
     max_end=-100000
     num=num+1








if __name__ == "__main__":
    import doctest

a = Agent()
b = Agent()
c = Agent()
d = Agent()
e = Agent()
f = Agent()
my_agent1 = []
my_agent2 = []

#TEST 1
a.array1 = [8,4,3]
b.array1 = [5,8,1]
c.array1 = [3,5,3]
my_agent1.append(a)
my_agent1.append(b)
my_agent1.append(c)


#TEST 2
d.array1=[7,0,0,0]
e.array1=[0,8,0,0]
f.array1=[0,0,4,0]
my_agent2.append(d)
my_agent2.append(e)
my_agent2.append(f)



#DOC-TEST
doctest.testmod()








