import string

# Cesar code with "tanslate" methode from standard library.
def cesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num :] + letters[: shift_num]
    transtab = str.maketrans(letters, mask)
    return plain_text.translate(transtab)

# Cesar code without "translate" methode but with "ord" and "chr" and "while" loop to fix the letter in the lowercase number range of the ASCII code.
def shift_n(letter, position):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + position
    while new_letter > ord("z"):
        new_letter -= 26
    while new_letter < ord("a"):
        new_letter += 26
    return chr(new_letter)

def cesar2(message, position):
    enc_list = [shift_n(letter, position) for letter in message]
    return "".join(enc_list)

# Cesar code with an imitation of the "translate" methode and a better way to fix the letter in the lowercase number range of the ASCII code.
def shift_n2(letter, table):
    try:
        index = string.ascii_lowercase.index(letter)
        return table[index]
    except ValueError:
        return letter

def cesar3(message, position):
    position = position % 26
    table = string.ascii_lowercase[position :] + string.ascii_lowercase[: position]
    enc_list = [shift_n2(letter, table) for letter in message]
    return "".join(enc_list)
