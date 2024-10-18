c=12345
z=0
while c>0:
    z=(z*10)+c%10
    c=c//10
print(z)