def kalki():  #how to use function
    print("my name is nanda")#function declaration
    print("iam from kadapa")
    print("iam studing b.tech")
kalki()#callin a function
kalki()
kalki()
def fun(a,b):#passing parameters to a funtions
    print(a+b)
    print(a-b)
    print(a*b)
fun(10,20)#arguments
fun(20,30)
def fun(name):
    print("my name is:",name)
fun("nanda")
def add():#no use return
    a=1
    b=3
    c=a+b
    print(c)
print(add())
def add():#use return
    a=1
    b=3
    c=a+b
    return c
print(add())
def add():# use return
    return "my name nanda"
print(add())
def add():#no use return
    print( "my name nanda")
print(add())
def pos(name,rollno):#position arguments
    print("my name is:",name)
    print("my rollno is:",rollno)
pos("nanda",100)
def key(name,rollno):#keyword arguments
    print("my name is:",name)
    print("my rollno is:",rollno)
key(rollno=22,name="sandula")
def fun(name="nanda",rollno=122):#default argument
    print("my name is:",name)
    print("my rollno is:",rollno)
fun()
def gun(*names):#arbitary position argumenta
    print(names)
    print(len(names))
    print(type(names))
gun("nanda","kumar","reddy","sandula")
