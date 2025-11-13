
def caesar_encryption(text: str, offset: int):
    l_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    encrypted_text = ""
    for ch in text:
        if ch not in l_list:
            encrypted_text += ch
        else:
            for i in range(len(l_list)):
                if ch == l_list[i]:
                    encrypted_text += l_list[(i + offset) % 26]
    return encrypted_text

def caesar_decryption(text: str, offset: int):
    l_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    decrypted_text = ""
    for ch in text:
        if ch not in l_list:
            decrypted_text += ch
        else:
            for i in range(len(l_list)):
                if ch == l_list[i]:
                    decrypted_text += l_list[(i - offset) % 26]
    return decrypted_text

def fence_encryption(text: str):
    encrypted_text = ""
    l_list = []
    for ch in text:
        if ch != " ":
            l_list.append(ch)
    for i in range(len(l_list)):
        if i % 2 == 0:
            encrypted_text += l_list[i]
    for i in range(len(l_list)):
        if i % 2 != 0:
            encrypted_text += l_list[i]
    return encrypted_text

def fence_decryption(text: str):
    decrypted_text = ""
    l_list = []
    for ch in text:
        l_list.append(ch)
    if len(l_list) % 2 == 0:
        middle = len(l_list) // 2
    else:
        middle = (len(l_list) // 2) + 1
    l_list_1 = l_list[:middle]
    l_list_2 = l_list[middle:]
    for i in range(len(l_list) // 2):
        decrypted_text += l_list_1[i]
        decrypted_text += l_list_2[i]
    return decrypted_text



