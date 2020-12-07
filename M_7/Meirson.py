from _nsis import err
from typing import List
import operator


def algo_1 (values:List[float]) ->List[bool]:
    chack = [False] * len(values)
    values.sort(reverse=True)
    max_Weight = 100
    Sekel_curent = 0
    for i in range(0, len(values)):
        if (Sekel_curent + values[i] <= max_Weight):
            Sekel_curent = Sekel_curent + values[i]
            chack[i] = True;
        else:
            return chack

    return chack

def no_monotonic(values:List[float]) ->List[bool]: ## this algo to take all without ruls
    chack=[False]*len(values)
    max_Weight = 100
    Sekel_curent = 0
    index, value = max(enumerate(values), key=operator.itemgetter(1))
    for i in range(0,len(values)):
         if (Sekel_curent + values[i] <= max_Weight):
            Sekel_curent = Sekel_curent + values[i]
            chack[i] = True;
         else:
            return chack


def choice (values:List[float], fun:int)-> List[bool]:
    chack=[False]*len(values)
    if(fun==1):
     chack=algo_1(values)
     return chack
    else:
        chack=no_monotonic(values)
        return chack

def if_monotonic(values:List[float] , chack:List[bool])->  bool:
    ans=[0]*chack.count(True)
    j=0
    for i in range(0,len(values)):
        if(chack[i]==True):
            for j in range(0,len(values)):
                if(values[i]<values[j] and chack[j]==False):
                    return False
    return True

def payment (values:List[float],how:int)-> List[float]:
    chack = choice(values,how)
    if(if_monotonic(values,chack)==False):
        print("NO MONOTONIC !".format(err))
    else:
     ans=[0]*len(values)
     max2 = -100000
     for i in range(0,len(values)):
         if(chack[i]==True):
            for j in range(0,len(values)):
                 for index in range(0, len(values)):
                     if(chack[index]==False):
                      if(values[index]>=max2):
                       max2=values[index]
                 ans[i]=max2
                 max2=0
    return ans



####main###

print ("example1 - algo_1 is Monotonic - WORKING!")
a=[30,40,20,9,2,2,3,4]
print( "choice: ",choice(a,1))
print("payment: ", payment(a,1))
print()

print ("###################################")
print("example2 - no_Monotonic - NOT WORKING!")
a=[10,10,20,90,20]
print( "choice: ",choice(a,2))
print("payment: ", payment(a,2))