import numpy as np
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

l1 = np.empty((rows, columns),dtype=str)
l2 = np.empty((rows, columns),dtype=str)
l3 = np.empty((rows, columns),dtype=str)

for i in range(rows):
    for j in range(columns):
        l1[i][j] = input()

for i in range (rows):
    for j in range(columns):
        l2[i][j]=l1[j][i]

for i in range (rows):
    for j in range(columns):
        l3[i][j]=l2[j][i]

#n dimentional to single dimention
single_dim_list = [i for sublist in l2 for i in sublist]
single_dim_list1 = [i for sublist in l3 for i in sublist]

single_dim_string = ''.join(single_dim_list)
single_dim_string1 = ''.join(single_dim_list1)

print("encoding: ", single_dim_string)
print("decoding: ", single_dim_string1)