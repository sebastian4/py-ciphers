import sys
import os
from itertools import chain, islice

def chunks(iterable, n):
   "chunks(ABCDE,2) => AB CD E"
   iterable = iter(iterable)
   while True:
       # store one line in memory,
       # chain it to an iterator on the rest of the chunk
       yield chain([next(iterable)], islice(iterable, n-1))

def open_file():
	file_name, file_extension = os.path.splitext(file_large)
	with open(file_large) as bigfile:
	    for i, lines in enumerate(chunks(bigfile, l)):
	        file_split = '{}.{}{}'.format(file_name, i, file_extension)
	        with open(file_split, 'w') as f:
	            f.writelines(lines)

####
# 1 ~ 50kb
# 2 ~ 100kb
# 4 ~ 200kb
# 8 ~ 400kb
# 16 ~ 800kb

####

# print 'Number of arguments:', len(sys.argv), 'arguments.'
l = 30*10**6
print 'Argument List:', str(sys.argv)
file_large = sys.argv[1]
print 'file: '+file_large
if len(sys.argv) > 2:
	l = int(sys.argv[2])*10**3
print 'size: '+str(l)
open_file()
