#Question 1: If large boxes = 8, small boxes = 3 and everyone must get 1 each (28 students). Determine left over cupcakes if everyone must get 1 cupcake; input should be number of cupcakes
R = int(input("Enter the number of large boxes"))
S = int(input("Enter the number of small boxes"))
if 8*R + 3*S < 28:
  print("invalid input")
else:
  print(R*8+S*3 - 28)

  
