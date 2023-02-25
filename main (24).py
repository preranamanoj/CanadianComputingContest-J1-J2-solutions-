#You have two teams, Bananas and Apples
#3 point shot, 2 point field goal,  1 point free throw
#apples first then bananas. A, B or T 
x = int(input()) #number of 3 point for Apples
y = int(input()) #number of 2 point for Apples
z = int(input()) #number of 1 point for Apples
a = int(input()) #number of 3 point for Bananas
b = int(input()) #number of 2 point for Bananas
c = int(input()) #number of 1 point for Bananas
A = x*3 + y*2 + z*1
B = a*3 + b*2 + c*1

if A>B:
  print("A")
elif B>A:
  print("B")
elif B ==A:
    print("T")

