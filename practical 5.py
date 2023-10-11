def multiply_lists(two_d_list, one_d_list):
    result = [[two_d_list[i][j] * one_d_list[j]
               for j in range(len(one_d_list))] for i in range(len(two_d_list))]
    return result

def char_to_int(text):
    l1 = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                l1.append(ord(char) - 65)
            else:
                l1.append(ord(char) - 97)
    return l1

def int_to_chat(number_list):
    l1 = []
    for integer in number_list:
        l1.append(chr(integer + 97))
    return l1

def encoding_hill_cipher(text):
    single_encode_list = char_to_int(text)
    encode = []
    key = [[3, 1], [5, 2]]
    for i in range(0, 4, 2):
        l2 = []
        l2.append(single_encode_list[i])
        l2.append(single_encode_list[i + 1])

        x1 = multiply_lists(key, l2)
    
        x2 = []
        i = 0
        x2.append(x1[i][i] + x1[i][i + 1])
        x2.append(x1[i + 1][i] + x1[i + 1][i + 1])

        x3 = []
        x3.append(x2[i] % 26)
        x3.append(x2[i + 1] % 26)
        encode.append(x3)

    single_encode_list = [i for sublist in encode for i in sublist]
    join_encoding_string = ''.join(int_to_chat(single_encode_list))

    return join_encoding_string

def decoding_hill_cipher(text):
    single_decode_list = char_to_int(text)
    decoding_key = [[2, -1], [-5, 3]]
    decode = []

    for i in range(0, 4, 2):
        l2 = []
        l2.append(single_decode_list[i])
        l2.append(single_decode_list[i + 1])

        x1 = multiply_lists(decoding_key, l2)

        x2 = []
        i = 0
        x2.append(x1[i][i] + x1[i][i + 1])
        x2.append(x1[i + 1][i] + x1[i + 1][i + 1])

        x3 = []
        x3.append(x2[i] % 26)
        x3.append(x2[i + 1] % 26)
        decode.append(x3)

    single_decode_list = [i for sublist in decode for i in sublist]
    join_decoding_string = ''.join(int_to_chat(single_decode_list))

    return join_decoding_string

print("encoded message :",encoding_hill_cipher("Meet"))
print("decoded message :",decoding_hill_cipher(encoding_hill_cipher("Meet")))

