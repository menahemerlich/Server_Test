from functions import caesar_encryption, caesar_decryption, fence_encryption, fence_decryption
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/test")
def test():
    return {"msg": "hi from test"}

@app.get("/test/{name}")
def test_name(name):
    with open(".names.txt", "a") as f:
        f.write(f"name: {name}\n")
    return { "msg": f"saved user, {name}"}

class CaesarCipher(BaseModel):
    text: str
    offset: int
    mode: str

@app.post("/caesar")
def caesar_cipher(cipher: CaesarCipher):
    if cipher.mode == "encrypt":
        encrypted_text = caesar_encryption(cipher.text, cipher.offset)
        return { "encrypted_text": encrypted_text }
    elif cipher.mode == "decrypt":
        decrypted_text = caesar_decryption(cipher.text, cipher.offset)
        return { "decrypted_text": decrypted_text }
    else:
        raise "Typo error"

@app.get("/fence/encrypt")
def fence_encrypt(text: str):
    encrypted_text = fence_encryption(text)
    return { "encrypted_text": encrypted_text }

class FenceCipher(BaseModel):
    text: str

@app.post("/fence/decrypt")
def fence_decrypt(cipher: FenceCipher):
    decrypted_text = fence_decryption(cipher.text)
    return { "decrypted": decrypted_text }





