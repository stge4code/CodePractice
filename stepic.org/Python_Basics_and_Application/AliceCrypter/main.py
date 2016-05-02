import simplecrypt
with open("encrypted.bin", "rb") as inp_m:
    message = inp_m.read()
with open("passwords.txt", "rb") as inp_p:
    for password in inp_p:
        try:
            print(simplecrypt.decrypt(password.strip(), message))
        except simplecrypt.DecryptionException:
            pass
