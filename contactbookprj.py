contacts=[]
list2=[]
def creatingcontact():
    print("Enter contact details:")
    name=input("Name: ")
    phn=input("phone number: ")
    email=input("Email: ")
    address=input("Address: ")
    # i=len(contacts)
    # print(len)
    list2=[name,phn,email,address]
    contacts.append(list2)
    print("contact added successfully")
    return name
def viewcontacts():
    print("your contacts:")
    for i in range(len(contacts)):
            print(f"contact no-{i+1}")
            print(f"Name:{contacts[i][0]}")
            print(f"phone number:{contacts[i][1]}")
            print(f"Email:{contacts[i][2]}")
            print(f"address:{contacts[i][3]}")
def  searchcontact(searchname):
    found=False
    for i in range(len(contacts)):
        for j in range(len(contacts[i])):
            if(searchname in contacts[i][j]):
                found=True
                print("contact found ---details are:")
                print(f"Name:{contacts[i][0]}")
                print(f"phone number:{contacts[i][1]}")
                print(f"Email:{contacts[i][2]}")
                print(f"address:{contacts[i][3]}")
                return i
    if not found:
        print("contact not found...")
        a=(input("do you want to save it:"))
        if a=="yes":
            creatingcontact()
            return len(contacts)+1
        else:
            return 0   
def updatect(updatectno):
    ctno=searchcontact(updatectno)
    print("enter updated details:")
    list1=["name","phone number","email","address"]
    for i in range(4):
        a=input(f"enter {list1[i]}")
        a.lower()
        if(a!=contacts[ctno][i] and a!="no"):
            contacts[ctno][i]=a
    print("updated successfully")
def delct(a):
    ctn=searchcontact(a)
    contacts.pop(ctn)
    print("contact deleted successfully...")
print("welcome to your contact book:")
option=0
while(option!=6):
    print("1.ADD A NEW CONTACT\n2.VIEW CONTACTS \n3.SEARCH CONTACTS \n4.UPDATE CONTACT \n 5.DELETE CONTACT \n 6.EXIT")
    option=int(input("please enter your choice:"))
    if(option==1):
        m=creatingcontact()
        a=input("do you want to view the contact you saved now(0/1):")
        if(a==1):
           searchcontact(m) 
    elif(option==2):
        viewcontacts()
    elif(option==3):
        searchname=input("enter search term(name or phone number:)")
        searchcontact(searchname)
        a=int(input("do you want to perform any operations(1.updation2.deletion)"))
        if(a==1):
            updatect(searchname)
        elif(a==2):
            delct(searchname)
    elif(option==4):
        updatectno=input("enter the name of the contact you want to update:")
        updatect(updatectno)
        
    elif(option==5):
        a=input("enter the contact name you want to delete:")
        delct(a)
    else:
        print("Bye Bye")