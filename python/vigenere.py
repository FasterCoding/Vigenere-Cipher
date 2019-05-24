import string

chars = string.ascii_uppercase + string.ascii_lowercase

def encrypt(text, key):

    mappedText = [chars.find(i) for i in text]
    mappedKey = [chars.find(i) for i in key]

    keyLength = len(key)
    textLength = len(text)

    cipher = ""

    for n in range(textLength):
        letter = (mappedText[n] + mappedKey[n % keyLength]) % len(chars)
        cipher += chars[letter]

    return cipher

def decrypt(cipher, key):
    
    mappedCipher = [chars.find(i) for i in cipher]
    mappedKey = [chars.find(i) for i in key]

    keyLength = len(key)
    cipherLength = len(cipher)

    plainText = ""

    for n in range(cipherLength):
        letter = (mappedCipher[n] - mappedKey[n % keyLength]) % len(chars)
        plainText += chars[letter]

    return plainText


if __name__ == "__main__":
    
    text = input('Text: ')
    key = input('Key: ')

    cipher = encrypt(text, key)
    plainText = decrypt(cipher, key)

    print('=======================')
    print('Text: ', text)
    print('Key: ', key)
    print('Cipher: ', cipher)
    print('Plain Text: ', plainText)