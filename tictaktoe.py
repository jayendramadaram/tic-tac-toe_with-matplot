cdimport matplotlib.pyplot as plt

def reprs(nd):
    lis1=[]
    lis2=[]
    for i in range(3):
        for k in range(3):
            if nd[i][k]=='x':
                lis1.append(k+0.5)
                lis2.append(abs(i-3)+0.5)
    
    lis3=[]
    lis4=[]
    for i in range(3):
        for k in range(3):
            if nd[i][k]=='O':
                lis3.append(k+0.5)
                lis4.append(abs(i-3)+0.5)
    
                
    plt.axis([-0.5, 4, 0.5, 4.5])
    plt.plot(lis1,lis2,'rx',
             lis3,lis4,'ko',
             [0,1,3],[1,1,1],'k',
             [0,1,3],[4,4,4],'k',
             [0,0],[1,4],'k',
             [3,3],[1,4],'k',
             [0,3],[3,3],'k',
             [0,3],[2,2],'k',
             [0,3],[4,4],'k',
             [1,1],[1,4],'k',
             [2,2],[1,4],'k',markersize=40)
    plt.axis('off')
    plt.show()
                

import numpy as np
import random

def chosenpos(a,b,ndarr):
    ndarr[a,b]='x'
def comppos(f,g,ndarr):
    ndarr[f,g]='O'
def win(arr,fin):
    flag=0
    
    for i in arr[:3,:]==['x','x','x']:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
            
            
    for i in arr[:3,:].T==['x','x','x']:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
    for i in [arr.diagonal()==['x','x','x']]:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
    for i in [np.fliplr(arr).diagonal()==['x','x','x']]:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
    if any(fin)==True:        
        print('HEY USER CONGRATS YOU WON')
        reprs(jay)
        quit()
        
    for i in arr[:3,:]==['O','O','O']:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
            
            
    for i in arr[:3,:].T==['O','O','O']:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
    for i in [arr.diagonal()==['O','O','O']]:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
    for i in [np.fliplr(arr).diagonal()==['O','O','O']]:
        if i.all()==False:
            fin.append(False)
        else:
            fin.append(True)
        
    if any(fin)==True:        
        print('LOL I WON, BETTER LUCK NEXT TIME')
        reprs(jay)
        quit()


if __name__ == "__main__":
    arth=[[(0,0),(0,1),(0,2)],
          [(1,0),(1,1),(1,2)],
          [(2,0),(2,1),(2,2)]]
    for i in arth:
      print(i)
    print("HEY BUDDY: HERE ARE SOME INSTRUCTINS :) \n ASSUME MATRIX POSSITIONS LIKE 0,0 REPRESENTS FIRST POSITION IN MATRIX \n 0,1 REPRSENTS 2nd ELEMNT IN FIRST ROW \n \n \n")
    print(' rules: \n enter 2 values with comma(,) in between \nEXAMPLE:0,0 OR 1,1 OR 1,0 OR 2,2 etc')

    lis=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    jay=np.empty((3,3),dtype='str')
    fin=[]
    for i in range(5):

        
        a,b=tuple(map(int,input().split(',')))
        chosenpos(a,b,jay)
        lis.remove((a,b))
        f,g=random.choice(lis)
        comppos(f,g,jay)
        lis.remove((f,g))
        print(jay)
        result=win(jay,fin)







'''

jay=np.arange(9).reshape(3,3)
print
print(jay.diagonal())
print(np.fliplr(jay).diagonal())
    
'''
