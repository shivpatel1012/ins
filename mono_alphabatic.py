def char_to_int(text):
    l1 = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                l1.append(ord(char) - 65)
            else:
                l1.append(ord(char) - 97)
    return l1

def encoding_mono_alphabetic(text, key):
    string_list = []
    for i in string:
        string_list.append(i)

    encoding_mono = []
    int_sting_list = char_to_int(string_list)
    for i in int_sting_list:
        encoding_mono.append(key[i])

    single_encode_list = [i for sublist in encoding_mono for i in sublist]
    join_encoding_string = ''.join((single_encode_list))

    return join_encoding_string

def decoding_mono_alphabetic(text):
    l1 = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in text:
        l1.append(i)
    l2 = char_to_int(l1)
    decoded_string = []
    for i in text:

        index1 = key.index(i)
        decoded_string.append(alphabet[index1])

    single_decode_list = [i for sublist in decoded_string for i in sublist]
    join_decoding_string = ''.join((single_decode_list))

    return join_decoding_string


string = input("enter the string :")
key = []
key_string = input("enter the key :")
for i in key_string:
    key.append(i)

print("Encoded message :", encoding_mono_alphabetic(string, key))
print("decoded message :", decoding_mono_alphabetic(encoding_mono_alphabetic(string, key)))


