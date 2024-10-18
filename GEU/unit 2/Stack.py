a=0
b=[]
while a!=3 :
    a=int(input("\t Enter 1 to push \n\t Enter 2 to pop \n\t Enter 3 to display \n")) 
    if(a==1):
        b.append(int(input("Enter \n")))
    elif(a==2):
        b.pop()
    elif(a==3):
        print(b)
    else:
        print("wrong choice")