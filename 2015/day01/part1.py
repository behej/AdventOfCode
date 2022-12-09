#! /usr/bin/python3

l = open("input", "r").readline()    
print(l.count('(') - l.count(')'))
