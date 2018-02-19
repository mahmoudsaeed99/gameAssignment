
x=[21,34,25,57,77,60]
m=0
i=0
while(m<=6):
    if(m<=5):
        y=0
        print("max number is",x[m]) 
        w=x[m]/2
        l=x[m]
        while(w>0):
              print(" first player enter int number bigger than 0")
              n=int(input())
              if(n>=l):
                  print(" you should write no less than max no.... play again")
                  break;
              if((n<=0) or(n>w*2)):
                 print("wrong....put number again from 1 to",w*2)
                 w=w-x[m]
                 n=int(input())
                 x[m]=x[m]-n
              else:
                 x[m]=x[m]-n
              if(x[m]<=0):
                 print(" first player win ")
                 w=0
                 break;
              else:
                  q=(n*2)-i
                  print(q)
                  if(i==n):
                      i=1
                      x[m]=x[m]-q
                      if(x[m]==0):
                         print(" you lose")
                      else:
                         w=(q+w)-w
                  else:
                     i+=1   
                     x[m]=x[m]-q
                     if(x[m]==0):
                         print(" you lose")
                     else:
                         w=(q+w)-w 
                   
                   
        m=m+1           
    else:
        m=m-6

