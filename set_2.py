def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        return letter
    else:
        number = alphabet.index(letter)
        new = (number + shift) % 26
        return alphabet[new]


def caesar_cipher(message, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newmessage = ""

    for letter in message:
        if letter == " ":
            newmessage = newmessage + " "
        else:
            old = alphabet.index(letter)
            new = (old + shift) % 26
            newmessage = newmessage + alphabet[new]

    return newmessage
        
            
def shift_by_letter(letter, letter_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        return letter
    else:
        index1 = alphabet.index(letter)
        indexletter= alphabet.index(letter_shift)
        index2 = (index1 + indexletter) % 26
        finalfinal = alphabet[index2]
        return finalfinal


def vigenere_cipher(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_message = []

    message_indices = []
    for msg_char in message:
        if msg_char == " ":
            message_indices.append(" ")
        else:
            msg_pos = alphabet.index(msg_char)
            message_indices.append(msg_pos)

    extended_key = []
    key_length = len(key)
    current_key_index = 0
    for msg_char in message:
        extended_key.append(key[current_key_index % key_length])
        current_key_index += 1

    key_indices = []
    for key_char in extended_key:
        key_pos = alphabet.index(key_char)
        key_indices.append(key_pos)

    for i in range(len(message_indices)):
        if message_indices[i] == " ":
            encrypted_message.append(" ")
        else:
            shifted_pos = (message_indices[i] + key_indices[i]) % 26
            encrypted_char = alphabet[shifted_pos]
            encrypted_message.append(encrypted_char)

    return "".join(encrypted_message)


def scytale_cipher(text, offset):

    text_len = len(text)

    while text_len % offset != 0:
        text = text + "_"
        text_len = len(text)

    result = ""
    cols = text_len // offset

    for i in range(text_len):
        pos = (i // offset) + cols * (i % offset)
        result = result + text[pos]

    return result


def scytale_decipher(ciphertext, offset):
    total_len = len(ciphertext)
    
    if offset == 0:
        return ciphertext
    
    num_columns = (total_len + offset - 1) // offset
    rows = []
    
    for r in range(offset):
        start = r
        current_row = []
        
        for c in range(num_columns):
            pos = start + c * offset
            if pos < total_len:
                current_row.append(ciphertext[pos])
            else:
                current_row.append('')
        rows.append(''.join(current_row))
    
    decoded = []
    
    for r in rows:
        decoded.append(r)
    
    return ''.join(decoded)