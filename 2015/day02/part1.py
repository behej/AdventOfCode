#! /usr/bin/python3

def compute_surface(w, l, h):
    s1 = w * l
    s2 = w * h
    s3 = l * h    
    return 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)


total = 0
with open("input", "r") as f:
    for l in f:
        dims = l.strip().split('x')
        dims = [int(i) for i in dims]
        total += compute_surface(dims[0], dims[1], dims[2])
            
print(total)
