from typing import List
import doctest

class Agent:
    def __init__(self, name):
        self.name = name
        self.array1 = []


class Dipartment:
  def __init__(self, name):
    self.name = name
    self.array1 = []
    self.is_siduc=False
    self.get_student = []



def matching(students:List[Agent], department:List[Dipartment]):
    """ DOC-TEST  !!!
        >>> matching(List_S,List_D)
        Aviva
        Rafi
        Batya
        Slomo
        Galia
        Tomer

        >>> matching(List_text2_S,List_text2_D)
        SOL
        NIR
        ORI
        AVIAD

        """



    list_all=students
    while(len(list_all)>0):
     list_notar=[]

     flag = False
     for i in students:
         flag=False
         for j in i.array1:
          if(flag==False):
             for d in department:
                 if(d.name==j):
                     if(i not in d.get_student):
                      d.get_student.append(i)
                     flag=True
                     break
     count_siduc=0
     for i in department:
          if(len(i.get_student)==1):
              count_siduc=count_siduc+1

     if(count_siduc==len(department)):
         for u in department:
             print(u.name)
             for k in u.get_student:
                 print(k.name)
         return

     for i in department:
         count =0
         for j in i.array1:
             if count==0:
              temp=j
              count=count+1
              for k in i.get_student:
                 if(k.name!=temp):
                     list_notar.append(k)
                     for o in students:
                         if(o.name==k.name):
                          o.array1.remove(i.name)
                     i.get_student.remove(k)

     list_all=list_notar






if __name__ == "__main__":
    Aviva =Dipartment("Aviva")
    Aviva.array1=["Rafi","Slomo","Tomer"]

    Batya =Dipartment("Batya")
    Batya.array1=["Slomo","Rafi","Tomer"]

    Galia=Dipartment("Galia")
    Galia.array1=["Slomo","Tomer","Rafi"]


    List_D=[]
    List_D.append(Aviva)
    List_D.append(Batya)
    List_D.append(Galia)


    Tomer =Agent("Tomer")
    Tomer.array1=["Batya","Galia","Aviva"]

    Slomo =Agent("Slomo")
    Slomo.array1=["Aviva","Batya","Galia"]

    Rafi =Agent("Rafi")
    Rafi.array1=["Aviva","Galia","Batya"]

    List_S=[]
    List_S.append(Tomer)
    List_S.append(Slomo)
    List_S.append(Rafi)






    ###########TEST 2##########


    nir = Agent("NIR")
    nir.array1=["SOL","ORI"]

    aviad = Agent("AVIAD")
    aviad.array1=["SOL","ORI"]

    sol = Dipartment("SOL")
    sol.array1=["NIR","AVIAD"]

    ori = Dipartment("ORI")
    sol.array1=["NIR","AVIAD"]

    List_text2_S=[]
    List_text2_S.append(nir)
    List_text2_S.append(aviad)
    List_text2_D=[]
    List_text2_D.append(sol)
    List_text2_D.append(ori)
    doctest.testmod()









