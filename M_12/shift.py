from typing import List
#
# for i, outer in enumerate(arr):
#     for j, value in enumerate(outer):
#         print(j)

def find_max_matches(compatible: List[List[bool]]):
 length=0
 index_1=""
 index_2=""
 index_3=""
 size_row=len(compatible)
 size_col=len(compatible[0])


 for i, outer in enumerate(compatible):
     for j, value in enumerate(outer):
      if(value==True):
        if(i!= j and j<size_row and i<size_col):
          #if(i<j):
           if(compatible[j][i]==True):
              index_1=i;
              index_2=j;
              length=2
              flag_i=False
              flag_j=False
              temp=i+1
              for k in range(j,size_row):
                if (flag_j==True):
                    temp=0
                for t in range(temp,size_col):
                 if(t==(size_col-1)):
                    flag_j=True
                 if(compatible[k][t]==True):
                            if(t==index_1):
                                length=3
                                index_3=k
                                print("Length " + str(length) + " cycle: " + str(index_1) + "->" + str(
                                      +index_2) + " and " + str(index_2) + "->" + str(index_3) + " and " + str(
                                      index_3) + "->" + str(index_1))
                                return

 if( length==2):
     if(index_1>index_2):
         temp = index_1
         index_1=index_2
         index_2=temp
     print("Length "+str(length)+" cycle: "+ str(index_1)+"->"+str(+index_2)+ " and "+str(index_2)+"->"+str(index_1))
 else:
  print("non")

### main ##


######Length 3 cycle######
arr = [[False,True,True]
      ,[True,False,False]
      ,[True,True,True]
      ,[True,False,False]]
find_max_matches(arr)


######Length 2 cycle######
barr = [[False,True,True]
      ,[True,False,False]
      ,[False,False,True]
      ,[False,False,False]]
find_max_matches(barr)


######non######
barr = [[False,True,True]
      ,[False,False,False]
      ,[False,True,True]
      ,[False,False,False]]
find_max_matches(barr)