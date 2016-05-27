from simplecrypt import encrypt, decrypt
import create

password = create.passwordman()

ciphertext = encrypt('password', password)