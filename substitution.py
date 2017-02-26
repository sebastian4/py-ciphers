import random

# chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
#         'abcdefghijklmnopqrstuvwxyz' + \
#         '0123456789' + \
#         ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

chars = 'abcdefghijklmnopqrstuvwxyz .'

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)

def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    flipped = {v: k for k, v in key.items()}
    return ''.join(flipped[l] for l in ciphertext)

def substitution_result(plaintext):
    """Generate a resulting cipher with elements shown"""
    key = generate_key()
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print 'substitution'
    print 'Key: %s' % key
    print 'Key list: %s' % ''.join(key.values())
    print 'Plaintext: %s' % plaintext
    print 'Encrypted: %s' % encrypted
    print 'Decrypted: %s' % decrypted
