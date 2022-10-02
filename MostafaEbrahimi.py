#MITS 5500G - Assignment1 - Question III - Mostafa Ebrahimi(100807509)

#Using DES from Crypto.Cipher and token_bytes from secrets library!
from Crypto.Cipher import DES
from secrets import token_bytes

print("\t\t\tCaution!!! \n First of all enter your text in a file named \"plain.txt\".")
input("\nIf you did so, press any key to continue.\n\n")

#encryptPlain is a function that opens a file, reads the data of the file and encrypt the data!
def encryptPlain(DESkey, FileName):
    #reads data from file named "plain.txt" and move it to encData.
    with open('plain.txt') as fe:
         encData = fe.read()

    #Object cipher is created with two lements, key and DES.MODE
    cipher = DES.new(DESkey, DES.MODE_EAX)
    #nonce is a variable inside the cipher object
    #nonce stores tandom bites that used along with the "key" to decrypt the encData.
    nonce = cipher.nonce
    #We give our encData as byte(ascii type) to cipher.encrypt_and_digest() for encrypting encData. 
    #tag is used to verify our message is not corrupted.
    cipheredText, tag = cipher.encrypt_and_digest(encData.encode('ascii'))
    fe.close()
    return nonce, cipheredText, tag

#decryptCipher is a function that dencrypt the data and returns a plain text.
def decryptCipher( nonce, decData, tag):
    #plain object creates and then we use it to decrypt our text with it.
    plain = DES.new(DESkey, DES.MODE_EAX, nonce)
    plaintext = plain.decrypt(decData)
    
    #We have to verify the message, if it is authentic or manipulate?!
    try:
        plain.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

#A key with the lenghth of 8 bytes creates here by using token_bytes.
DESkey = token_bytes(8)
#The generated key stores in "mykey.key" file.
with open ('mykey.key','wb') as decrypt_file:
     decrypt_file.write(DESkey)
print("The key is generated and stored in \"mykey.key\" file. \n")

#encryptPlain function returns three values: "nonce", "text" and "tag"
nonce, cypheredtext, tag = encryptPlain(DESkey, "plain.txt")
print("The encrypted text message (strored in \"cipher.txt\" too) is:\n")
print(cypheredtext)
with open('cipher.txt', 'wb') as fd:
    fd.write(cypheredtext)

#We check the plain text here. First we decrypt cypheredtext and put the result in plain variable.
plain=decryptCipher(nonce,cypheredtext,tag)
if not plain:
   print ("\n\tText is croppted!!!")
else:
   print(f'\nPlain text:\n {plain}')
   print("\nThe plain message is located in \"plain.txt\" file too.\n")
