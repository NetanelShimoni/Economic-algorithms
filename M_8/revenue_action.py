import doctest




class Uniform:
    low=0
    high=0;


def max_revenue_auction(agent:Uniform,value1:float):
    """ DOC-TEST  !!!
              >>> max_revenue_auction(a,0)
              0

              >>> max_revenue_auction(a,15)
              15.0
              """


    F =(value1-agent.low)/(agent.high-agent.low)
    F_TAG = 1/(agent.high-agent.low)
    R= value1-((1-F)/F_TAG)
    if value1 >= agent.high or value1<=agent.low:
        R=0
        print(R)
        return
    if R>=0:
        print((0+agent.high)/2)


def max_revenue_auction_secendfunc(agent1:Uniform,agent2:Uniform,value1:float,value2:float):
    """ DOC-TEST  !!!
           >>> max_revenue_auction_secendfunc(a,b,1,1)
           No agent wins

           >>> max_revenue_auction_secendfunc(a,b,23,27)
           Agent 1 wins and pays 22
           """

    EPSILON =0.1
    R_agent1=2*value1-agent1.high
    R_agent2=2*value2-agent2.high
    if(R_agent1<0 and R_agent2<0):
        print("No agent wins")
        return
    if(R_agent2>R_agent1):
        sum=R_agent2
        while (R_agent2 > R_agent1):
            value2=value2-EPSILON
            R_agent2=2*value2-agent2.high
        if(value2>(0+agent2.high)/2):
            print("Agent 2 wins and pays ",int(value2)+1)
        else:
            print("Agent 2 wins and pays ",(0+agent2.high)/2)
    else:
        sum = R_agent1
        while (R_agent1 > R_agent2):
            value1=value1-EPSILON
            R_agent1=2*value1-agent1.high
        if(value1>(0+agent1.high)/2):
            print("Agent 1 wins and pays",int(value1)+1)
        else:
            print("Agent 1 wins and pays ",(0+agent1.high)/2)





#####main##
if __name__ == "__main__":
    import doctest


a = Uniform()
a.low=10
a.high=30
b = Uniform()
b.low=20
b.high=40
#max_revenue_auction(a,22)
#max_revenue_auction_secendfunc(a,b,23,27)
doctest.testmod()
