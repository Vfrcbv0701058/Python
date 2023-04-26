' ' ' I N id_44 Sortowanie merge ' ' '

from random import randint 
from time import time 

A  =  [randint (1,10**5)  for  i_44  in  range (2*10**5)]
B  =  sorted (A.copy () )

def merge (A,p,q,r) :
    L  = A [p:q] 
    P  =  A [q:r]
    i,j  =  0,0 
    k  =  p 
    while  i  <  len (L)  and  j  <  len (P) : 
         if  L [i]  <  P [j] :
                A [k]  =  L [i]
                i  +=  1
         else :  A [k]  =  P [j] ;  j  +=  1 
         k  +=  1
    A [k:r]  =  L [i:] + P [j:]
    return  A
#A – [ 2, 5, 7, 12, 3, 4, 5, 7 ]
#print (merge (A, 0, 4, 8) )

def  mSort (A, p=0, r=len (A) ) :
    if  p  ==  r-1  :  return  A
    q  =  (p+r) // 2
    mSort (A, p, q)
    mSort (A, q, r)
    return  merge (A, p, q, r)