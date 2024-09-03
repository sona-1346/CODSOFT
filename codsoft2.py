task=[]
n=int(input("enter a range number:"))
for a in range(n):
    a=input("enter the task:")
    task.append(a)
    print(task)
def add():
    a=input("enter the task to be add:")
    task.append(a)
    return(task)
def update():
    b=input("enter the update task:")
    c=int(input("enter the index no:"))
    task[c]=b
    return(task)
def track():
    d=int(input("enter the task index to mark as done:"))
    e=input("enter task name:")
    if 0<=d<=len(task):
        task[d]=(e+"-Done")
        return("task marked as done")
    else:
        return("invalid choice")
def view():
    print(*task,sep='\n')
while(True):
    print("1.add\n","2.update\n","3.track\n","4.view\n")
    choice=int(input("enter the choice:"))
    if choice==1:
        add()
    elif choice==2:
        update()
    elif choice==3:
        track()
    elif choice==4:
        view()
    else:
        print("choice doesn't exist")
