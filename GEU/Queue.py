MAX=int(input("\t Enter the max size of queue\n"))
queue=[]


def insert(queue,MAX,z,front,rear):
    if front==-1 and rear==-1:
        front=0
        rear=0

    queue.append(z)
    rear+=1
    
    return queue,front,rear

def delete(queue,front,rear):

    front+=1
    return front

def display(queue,front,rear):
    for i in range(front,rear):
        print(queue[i]," ")


ch=0
z=0
front=-1
rear=-1
while ch!=4:
    ch=int(input("\t Enter 1 to insert into the queue \n\t Enter 2 to delete an element from the queue \n\t Enter 3 to display \n\t Enter 4 to exit \n"))

    if ch==1:
        if rear< MAX:
            z=int(input("\t Enter the element \n"))
            queue,front,rear=insert(queue,MAX,z,front,rear)
        else:
            print("\t Queue Overflow \n")
    
    elif ch==2:
        if front==rear:
            print("\t Queue Underflow \n")
        else:
            front=delete(queue,front,rear)

    elif ch==3:
        display(queue,front,rear)

    elif ch==4:
        break

    else:
        print("\t INVALID CHOICE \n")

    
