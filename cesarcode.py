import string

# Cesar code with "tanslate" from standard library.
def cesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num :] + letters[: shift_num]
    transtab = str.maketrans(letters, mask)
    return plain_text.translate(transtab)
