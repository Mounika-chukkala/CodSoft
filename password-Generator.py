import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','|','/',':']
numbers=[1,2,3,4,5,6,7,8,9]
l=int(input("enter how many letter do you want to have?"))
s=int(input("enter how many symbols do you want to have?"))
n=int(input("enter how many numbers you want?"))
num_letters=random.choices(letters,k=l)            
num_symbols=random.choices(symbols,k=s)
num_numbers=random.choices(numbers,k=n)
password=num_letters+num_symbols+num_numbers
random.shuffle(password)
for i in password:
    print(i,end="")
print()
