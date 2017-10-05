#Problem statement : https://www.codechef.com/ZCOPRAC/problems/ZCO12001 
n=int(input())
brackets=[int(q) for q in input().split()]
counter=0
maxcounter=0
pos1=0
depth=0
maxdepth=0
pos2=0
for i in range(n):
  if brackets[i]==1:
    counter=counter+1
  elif brackets[i]==2:
    counter=counter-1
  if counter>maxcounter:
    maxcounter=counter
    pos1=i+1
  
print(maxcounter,end=' ')
print(pos1,end=' ')

for i in range(n):
  if brackets[i]==1:
    counter=counter+1
  elif brackets[i]==2:
    counter=counter-1
  
  if counter!=0:
    depth=depth+1
  elif counter==0:
    depth=0
    
  if depth>maxdepth:
    maxdepth=depth
    pos2=i-maxdepth
    
  
print(maxdepth+1,end=' ')
print(pos2+2,end='')
print()
    
