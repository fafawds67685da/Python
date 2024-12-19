a=int(input("\t Enter the size of the stack \n"))
el=[]
ch=0
while ch!=4:
    c="""\tEnter 1 to push an element into the stack
         Enter 2 pop an element from the stack
         Enter 3 to display the stack
         Enter 4 to exit
         """
    ch=int(input(c))
    if ch==1:
        if len(el)<a:
            el.append(int(input("\t Enter the element \n")))
        else:
            print("\t stack overflow!")
    elif ch==2:
        if len(el)==0:
            print("\t Stack underflow \n")
        else:
            z=el.pop()
            print(z)
    elif ch==3:
        for i in range(len(el)):
            print(el[i])
    elif ch==4:
        break
    else:
        print("\t Invalid choice \n")
