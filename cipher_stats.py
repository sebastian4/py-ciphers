
def stats(cipher_string):
	cipher_uniques = ''.join(set(cipher_string))
	print 'cipher string: %s' % cipher_string
	print 'cipher string count: %i' % len(cipher_string)
	print 'cipher uniques: %s' % cipher_uniques
	print 'cipher uniques count: %i' % len(cipher_uniques)