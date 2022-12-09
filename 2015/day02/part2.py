#! /usr/bin/python3

def compute_length(dims):
    dims.sort()
    return (dims[0] + dims[1])*2 + dims[0]*dims[1]*dims[2]
    

total = 0
with open("input", "r") as f:
    for l in f:
        dims = l.strip().split('x')
        dims = [int(i) for i in dims]
        total += compute_length(dims)
        
    
print(total)


    
    
