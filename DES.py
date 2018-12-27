import textwrap 

rotation = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]
PC1 = [ 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]
PC2 = [ 14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]
EP = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

PF  = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25 ]

IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
def permutation(Input, permutationTable):
    Output = ""
    for i in range(len(permutationTable)):
        Output += Input[permutationTable[i] - 1]
    #print(Output)
    return Output

def leftZeros(Input, inputSize):
	add = ""
	if(len(Input)<inputSize):
		add = "0" * (inputSize - len(Input))
	Input = add + Input
	return Input

def xor (a, b):
    value = bin(int(a, 2) ^ int(b, 2))[2:]
    size = len(a)
    if(len(b) > len(a)):
   		size = len(b)
    value = leftZeros(value, size)
    return value

def hex_to_binary(Input, length):
	Input = bin(int(Input, 16))[2:]
	#print(len(Input))
	Input = leftZeros(Input, length)
	return	Input

def circular_left(text, rotate):
	return text[rotate::] + text[:rotate:]
def left_shifted(key):
	keyOne = key[0:28]
	keyTwo = key[28:]
	keys_shifted = [None] * 16
	for i in range(len(rotation)):
		keyOne = circular_left(keyOne, rotation[i])
		keyTwo = circular_left(keyTwo, rotation[i])
		keys_shifted[i] = keyOne + keyTwo
		keys_shifted[i] = leftZeros(keys_shifted[i], 48)
	return keys_shifted

def Key_Generation(key):
	key = hex_to_binary(key, 64)
	#print(key)
	key = permutation(key, PC1)
	keys_shifted = left_shifted(key)
	keys_permutated = [None] * 16
	for i in range(len(keys_shifted)):
		keys_permutated[i] = permutation(keys_shifted[i], PC2)
		#keys_permutated[i] = hex(int(keys_permutated[i], 2))[2:].upper()
		keys_permutated[i] = leftZeros(keys_permutated[i], 48)
	return keys_permutated

def S_box(Input):
    Input = textwrap.wrap(Input, 6) # binary to array of 8 elements, each is 6 in size
    S = [
    [

    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],

    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],

    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],

    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    ],

    [

    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],

    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],

    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],

    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    ],

    [

    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],

    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],

    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],

    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    ],

    [

    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],

    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],

    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],

    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    ],

    [

    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],

    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],

    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],

    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    ],

    [

    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],

    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],

    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],

    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    ],

    [

    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],

    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],

    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],

    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    ],

    [

    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],

    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],

    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],

    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],

    ]

    ]
    Output = [None] * 8
    for i in range(8):
            row = Input[i][0] + Input[i][5]
            row = int(row, 2)
            col = Input[i][1] + Input[i][2] + Input[i][3] + Input[i][4]
            col = int(col, 2)
            Output[i] = bin(S[i][row][col])[2:]
            Output[i] = leftZeros(Output[i], 4)
            #print (Output[i])
    Output = "".join(Output)
    return Output

def F_Function(Input, key):
	#Input = hex_to_binary(Input, 32)
	#key = hex_to_binary(key, 48)
	step = permutation(Input, EP)
	#print("expansion: ", step)
	step = xor(step, key)
	#print("xor: ",step)
	step = S_box(step)
	#print("s box: ",step)
	step = permutation(step, PF)
	#print("straight: ",step)
	# step = hex(int(step, 2))[2:].upper()
	return step

def Encryption(plain, keys):
	plain = hex_to_binary(plain, 64)
	plain = permutation(plain, IP)
	plainOne = plain[:32]
	plainTwo = plain[32:]
	#print(plainOne, plainTwo)
	for i in range(16):
		right = xor(plainOne, F_Function(plainTwo,keys[i]))
		left = plainTwo
		plainOne = left
		plainTwo = right
		#print(plainOne, plainTwo, i)
	temp = plainTwo
	plainTwo = plainOne
	plainOne = temp
	result = plainOne + plainTwo
	#print(hex(int(result, 2))[2:].upper())
	result = permutation(result, IP_1)
	#print(result)
	result = hex(int(result, 2))[2:].upper()
	result = leftZeros(result, 16)
	return result


#** Program **#
key = input("Plese enter your key as 16 Hex characters: ")
plain = input("Plese enter your plain text as 16 Hex characters: ")
numOfIterations = int(input("please enter the number of encryptions you want to perform on the plan text: "))
keys = Key_Generation(key)
#print(keys)
cipher = plain
for i in range(numOfIterations):
	cipher = Encryption(cipher, keys)
print("cipher: ", cipher)
