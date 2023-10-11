# l1 = [1,1,1]
# for i in range(10):
#     a1 = l1[i]
#     a2 = l1[i+1]
#     a3 = l1[i+2]

#     total = a1 + a2 + a3
#     l1.append(total)

# print(l1)
####################
# l1 = [10,2,7,5]
# l1.sort()
# sum = l1[0] + l1[1]
# print(sum)
###################

# p0 = 1000
# pr = 0.02
# aug = 50
# a = 0
# total  = 0
# while(total <= 1200):
#     total = p0 + (p0 * pr) +aug
#     p0 = total
#     a = a+1
# print(a)
# #############################
# def nb_year(p0, percent, aug, p):
#     total = 0
#     a = 0
#     percent1 = percent/100
#     while(total < p):
#         total = p0 + (p0 * percent1) +aug
#         p0 = int(total)
#         a = a+1
#         print(p0)
#     return a

###################################
# def create_phone_number(n):
#     a1 = n[0]*100
#     a2 = n[1]*10
#     a3 = n[2]

#     totala = str(a1+a2+a3)

#     a1 = n[3]*100
#     a2 = n[4]*10
#     a3 = n[5]

#     totalb = str(a1+a2+a3)

#     a1 = n[6]*1000
#     a2 = n[7]*100
#     a3 = n[8]*10
#     a4 = n[9]

#     totalc = str(a1+a2+a3+a4)

#     print("("+totala+")" ,totalb + "-"+totalc)

# create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])


# def convert(s):

#     l1 = []
#     l2 = []
#     l3 = []
#     for i in range(3):
#         l1.append(s[i])
#     for i in range(3):
#         l2.append(s[i + 4])
#     for i in range(4):
#         l3.append(s[i + 7])

#     new1 = ""
#     new2 = ""
#     new3 = ""

#     new1.join(l1)

#     print(new1)
# # l1 = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]
# # l2 = map(str , l1)
# s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
# print(convert(s))

# def convert(s):


#     l1 = []
#     l2 = []
#     l3 = []
#     for i in range(3):
#         l1.append(s[i])
#     for i in range(3):
#         l2.append(s[i + 4])
#     for i in range(4):
#         l3.append(s[i + 6])
#     l1 = map(str,l1)
#     l2 = map(str,l2)
#     l3 = map(str,l3)
#     a1 = ("".join(l1))
#     a2 = ("".join(l2))
#     a3 = ("".join(l3))

#     return "("+ a1 +") " + " "+ a2 +"-"+ a3

# print(convert([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

########################################

# def narcissistic(value):
#     length = len(str(value))
#     l1 = list(str(value))
#     l2 = list(map(int, l1))
#     l3 = []
#     for i in range(length):
#         num = l2[i]**length
#         l3.append(num)
#         num1 = 0
#     for i in range(length):
#         num1 = num1 + l3[i]

#     if num1 == value:
#         return True
#     else:
#         return False


# print(narcissistic(153))

# def alphabet_position(text):
#     l1 = list(text)
#     l2 = []
#     for i in range(len(text)):
#         if  (l1[i] == 'a' or l1[i] == 'A'):
#             l2.append(1)
#         elif(l1[i] == 'b' or l1[i] == 'B'):
#             l2.append(2)
#         elif(l1[i] == 'c' or l1[i] == 'C'):
#             l2.append(3)
#         elif(l1[i] == 'd' or l1[i] == 'D'):
#             l2.append(4)
#         elif(l1[i] == 'e' or l1[i] == 'E'):
#             l2.append(5)
#         elif(l1[i] == 'f' or l1[i] == 'F'):
#             l2.append(6)
#         elif(l1[i] == 'g' or l1[i] == 'G'):
#             l2.append(7)
#         elif(l1[i] == 'h' or l1[i] == 'H'):
#             l2.append(8)
#         elif(l1[i] == 'i' or l1[i] == 'I'):
#             l2.append(9)
#         elif(l1[i] == 'j' or l1[i] == 'J'):
#             l2.append(10)
#         elif(l1[i] == 'k' or l1[i] == 'K'):
#             l2.append(11)
#         elif(l1[i] == 'l' or l1[i] == 'L'):
#             l2.append(12)
#         elif(l1[i] == 'm' or l1[i] == 'M'):
#             l2.append(13)
#         elif(l1[i] == 'n' or l1[i] == 'N'):
#             l2.append(14)
#         elif(l1[i] == 'o' or l1[i] == 'O'):
#             l2.append(15)
#         elif(l1[i] == 'p' or l1[i] == 'P'):
#             l2.append(16)
#         elif(l1[i] == 'q' or l1[i] == 'Q'):
#             l2.append(17)
#         elif(l1[i] == 'r' or l1[i] == 'R'):
#             l2.append(18)
#         elif(l1[i] == 's' or l1[i] == 'S'):
#             l2.append(19)
#         elif(l1[i] == 't' or l1[i] == 'T'):
#             l2.append(20)
#         elif(l1[i] == 'u' or l1[i] == 'U'):
#             l2.append(21)
#         elif(l1[i] == 'v' or l1[i] == 'V'):
#             l2.append(22)
#         elif(l1[i] == 'w' or l1[i] == 'W'):
#             l2.append(23)
#         elif(l1[i] == 'x' or l1[i] == 'X'):
#             l2.append(24)
#         elif(l1[i] == 'y' or l1[i] == 'Y'):
#             l2.append(25)
#         elif(l1[i] == 'z' or l1[i] == 'Z'):
#             l2.append(26)
#     l2 = list(map(str,l2))
#     str1 = ""
#     a2 = 0
#     for i in l2:
#         str1 += i
#         a2 += 1
#         if a2 < len(l2) :
#             str1 +=" "
#         else:
#             a = 1

#     return str1

# print(alphabet_position("pycinEvMjBLGWfYQawHdBBuDDVMBYVeLgeKBmAyiUEntCYyvQwOTulFvYXqZzswZCCTxNqUDvmilFXSmrqojzzDrPqkmYdUojXxq"))

# def odd_or_even(arr):
#     if (sum(arr) % 2) == 0:
#         return "even"
#     else:
#         return "odd"

# print(odd_or_even([-43, 55, 81, -40, -13, -20, -98]))

# def make_readable(seconds):
#     a1 = int(seconds / 60)
#     a2 = seconds % 60
#     a3 = int(a1 / 60)
#     a4 = a1 % 60

#     return '{:02d}:{:02d}:{:02d}'.format(a3, a4, a2)


# print(make_readable(339))

# def digital_root(n):

#     while len(str(n)) > 1:
#         l1 = list(str(n))
#         l1 = map(int,l1)
#         n = sum(l1)

#     return n

# print(digital_root(493193))

# from itertools import count
# from turtle import goto

# from numpy import True_


# def zeros(n):
#     ans = 1
#     for i in range(1,n+1):
#         ans = ans * (i)
#     ans = list(str(ans))
#     ans = ans[::-1]
#     count = 0
#     for i in range(len(ans)):
#         if ans[i] == '0':
#             count += 1
#         else:
#             return count

# print(zeros(10))

# def solution(s):
#     l1 = list(s)
#     print(l1)
#     str1 = ""
#     for i in l1:
#         if (ord(i) < 123 and ord(i) > 96):
#             pass
#         else:
#             str1 += " "
#         str1 += i
#     return str1

# def valid_parentheses(string):
#     string = list(string)
#     for i in range(len(string)):
#         for j in range(i,len(string)):
#             if string[i] != string[j]:
#                 a = 1
#             else:
#                 pass
#     if a == 1:
#         return True
#     else:
#         return False
# print(valid_parentheses(")(()))"))

# def tribonacci(signature, n):
#     l1=[]
#     l1 = signature
#     if(n == 0):
#         return []
#     elif(n == 1):
#         return [l1[0]]
#     elif(n == 2):
#         return [l1[0],l1[1]]

#     for i in range(2,n-1):

#         total = signature[i] + signature[i-1] + signature[i-2]
#         l1.append(total)

#     return l1
# print(tribonacci([1, 1, 1], 2))

# def sum_pairs(ints, s):
#     a = 1
#     for i in range(len(ints)):
#         for j in range((i+1),len(ints)):
#             if(ints[i] + ints[j] == s):
#                 a = 1
#                 return [ints[i],ints[j]]
#     if(a!=1):
#         return "none"

# print(sum_pairs([10, 5, 2, 3, 7, 5],10))

# spacial number

# import math
# def spacial_num(num):
#     b = str(num)
#     c = []
#     d=[]
#     for digit in b:
#         c.append(int(digit))
#     for i in range(0,len(c)):
#         d.append(math.factorial(c[i]))
#     print(sum(d))
# spacial_num(145)

# def bigger(n):

#     num = list(map(int, str(n)))
#     num2 = []
#     for i in range(0, len(num)):
#         a1 = max(num)
#         num2.append(a1)
#         num.remove(a1)
#     s = [str(i) for i in num2]
#     res = int("".join(s))
#     return res

# bigger(12)

# list_a = [1, 2, 3, 3, 4, 5]
# list_b = [ 4, 6]

# result = [element for element in list_a if element not in list_b]
# print(result)

# def filter_list(l):
#     l1 = []
#     for i in range(len(l)):
#         if (type(l[i]) == type("b")):
#             # l.remove(l[i])
#             z = 1
#         else:
#             l1.append(l[i])
#     return l1
# print(filter_list([1,2,'a','b']))

# def hex_to_decimal_matrix(hex_matrix):
#     decimal_matrix = []

#     for row in hex_matrix:
#         decimal_row = []
#         for hex_value in row:
#             decimal_value = (hex_value)
#             decimal_row.append(decimal_value)
#         decimal_matrix.append(decimal_row)

#     return decimal_matrix


# hex_matrix = [[0xF1, 0x02, 0x03, 0x04],
#                 [0x05, 0x06, 0x07, 0x08],
#                 [0x09, 0x0a, 0x0b, 0x0c],
#                 [0x0e, 0x0f, 0x01, 0x00]]

# decimal_matrix = hex_to_decimal_matrix(hex_matrix)
# print(decimal_matrix)

#Ben Ryan
#AES Key Expansion
#Program uses provided key as input, outputs the corresponding keywords w0 - w43 as given in table to cmd

sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
		0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
		0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
		0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
		0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
		0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
		0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
		0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
		0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
		0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
		0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
		0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
		0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
		0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
		0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
		0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

Rcon = [0x00000000, 0x01000000, 0x02000000,
		0x04000000, 0x08000000, 0x10000000, 
		0x20000000, 0x40000000, 0x80000000, 
		0x1b000000, 0x36000000]
		
def keyExpansion(key):
	w = [()]*44
	
	for i in range(4):
		w[i] = (key[4*i], key[4*i+1], key[4*i+2], key[4*i+3])
		
	for i in range(4, 44):
		temp = w[i-1]
		word = w[i-4]

		if i % 4 == 0:
			x = RotWord(temp)
			y = SubWord(x)
			rcon = Rcon[int(i/4)]

			temp = hexor(y, hex(rcon)[2:]) 
			
		word = ''.join(word)
		temp = ''.join(temp)
		
		xord = hexor(word, temp)
		w[i] = (xord[:2], xord[2:4], xord[4:6], xord[6:8])
		
	return w
	
def hexor(hex1, hex2):
	bin1 = hex2binary(hex1)
	bin2 = hex2binary(hex2)
	
	xord = int(bin1, 2) ^ int(bin2, 2)
	
	hexed = hex(xord)[2:]
	
	if len(hexed) != 8:
		hexed = '0' + hexed
		
	return hexed
	
def hex2binary(hex):
	return bin(int(str(hex), 16))

	
def RotWord(word):
	return word[1:] + word[:1]
		
		
def SubWord(word):
	sWord = ()
	
	for i in range(4):
		
		if word[i][0].isdigit() == False:
			row = ord(word[i][0]) - 86
		else:
			row = int(word[i][0])+1

		if word[i][1].isdigit() == False:
			col = ord(word[i][1]) - 86
		else:
			col = int(word[i][1])+1
		
		sBoxIndex = (row*16) - (17-col)
		
		piece = hex(sbox[sBoxIndex])[2:]
		
		if len(piece) != 2:
			piece = '0' + piece
		
		sWord = (*sWord, piece)
		
	return ''.join(sWord)

key = ["0f", "15", "71", "c9", "47", "d9", "e8", "59", "0c", "b7", "ad", "d6", "af", "7f", "67", "98"]
w = keyExpansion(key)
key_matrix = [[0 for _ in range(4)] for _ in range(4)]
key_count  = 4
for i in range(4):
    for j in range(4):
          key_matrix[i][j] = int(w[key_count + i][j],16)
print(key_matrix)