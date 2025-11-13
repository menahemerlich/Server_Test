
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




