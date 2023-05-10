print("Welcome Student !")



def show_fun():
    print("1=student info")
    print("2=fees info")
    print("3=leave")
    print("4=exit")
    print("5=enroll")

def student():
    f=open("student.txt","r")
    y=f.read()
    print(y)
 
def student_1():
    f = open("student_1.txt","r")
    q=f.read()
    print(q)

def fees():
    f=open("fees.txt","r")
    z=f.read()
    print(z)

def fees1():
    f=open("fees1.txt","r")
    p=f.read()
    print(p)

def leave():
   print("thnankyou")
   f=open("student.txt","w")
   f.write("no data found")
   f.close()
    
def leave_1():
    print("thankyou")
    f=open("student_1","w")
    f.write("no data found")
    f.close()

def exit():
    print("Thankyou for enroll")

def roll_no():
    f=open("rollno.txt","r")
    b=f.read()
    print(b)
    t=int(b)
    print(t)
   
      
def roll_no_1():
    f=open("rollno1.txt","r")
    g=f.read()
#     print(g)
    h=int(g)
    print(h)

rollno = int(input("enter your roll number"))  
while True:     
        
    show_fun()
    choice = int(input("enter your choice 1 2 3 4 5"))


    #  first student info
    if rollno == 1234 :
        print("welcome sonali")

        if choice==1:
                    
            print("welcome in Information cell")
            student()
                    
        elif choice==2:
            print("submit your fees")
            fees()
        elif choice == 3:
            leave()
                    
                    
        elif choice ==4:
            print("exit this page")
            exit()
            
            
                        # second stuent info   


    elif rollno==5678:
        print("welcome deep")


    elif choice==1:
            print("welcome in addmision cell")
            student_1()
    
    elif choice==2:
            fees1()
    
    elif choice==3:
            leave_1()
    
    elif choice==4:
            exit()
    else:
            print("exit")



