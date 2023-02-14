x = input() #enter a list of integers w spaces 
y = input()
z = input()
k = input()
int_list = list(map(int, x.split()))
y_list = list(map(int, y.split()))
z_list = list(map(int, z.split()))
k_list = list(map(int, k.split()))
m = (int_list[0] + int_list[1] + int_list[2] + int_list[3])
n = (y_list[0] + y_list[1] + y_list[2] + y_list[3])
o = (z_list[0] + z_list[1] + z_list[2] + z_list[3])
p = (k_list[0] + k_list[1] + k_list[2] + k_list[3])

if m ==n and n ==o and o ==p:
    print("magic")
else:
    print("not magic")






