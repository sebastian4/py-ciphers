key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


def caesar_shift_result(plaintext, n):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(n, plaintext)
    decrypted = decrypt(n, encrypted)

    print 'caesar shift'
    print 'Rotation: %s' % n
    print 'Plaintext: %s' % plaintext
    print 'Encrypted: %s' % encrypted
    print 'Decrypted: %s' % decrypted
