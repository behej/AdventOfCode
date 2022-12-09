#! /usr/bin/python3

from hashlib import md5

secret = 'bgvyzdsv'
h = 'aaaa'
i = 0
while not h.startswith('00000'):
    i += 1
    h = md5(bytes('{}{}'.format(secret, i), 'ascii')).hexdigest()
    
print("Part 1: {}".format(i))


h = 'aaaa'
i = 0
while not h.startswith('000000'):
    i += 1
    h = md5(bytes('{}{}'.format(secret, i), 'ascii')).hexdigest()
    
print("Part 2: {}".format(i))
