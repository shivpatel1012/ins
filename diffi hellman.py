q = int(input("enter the prime number for q: "))
alpha = int(input("enter the value of alpha: "))

a1 = int(input("enter the value for a1: "))
a2 = int(input("enter the value for a2: "))

y1 = alpha ** a1 % q 
y2 = alpha ** a2 % q 

print("y1: ", y1)
print("y2: ", y2)
#checking
k1 = y2 ** a1 % q 
k2 = y1 ** a2 % q 
print("checking")
print("k1: ", k1)
print("k2: ", k2)