import random
userint = input("Enter c for coding/d for decoding ")
userint =userint.lower()
def reverse(e):
    n=""
    for i in range(len(e)):
        n= n+ e[len(e)-i-1]
    return n
def reverse_splitter(i):
    list = i.split()
    list.reverse()
    i = " ".join(list)
    print(i)
def rand():
    m =""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(3):
        m = m + random.choice(alphabet)
    return m

if userint == "c":
    a = input("enter the word:")
    a = a.strip()
    # if more than one word
    if  a.count(" ") in (1,2):
        reverse_splitter(a)
        exit()     
    elif a.count(" ") >2:
        list = a.split(" ")
        for i in list:
            list[list.index(f"{i}")] = rand()+  i[1:] + i[0] + rand()
        a = " ".join(list)
        print(a)
        exit()
    if len(a)<3:
        print(reverse(a))
    else:  
        a = rand() + a[1:]+ a[0] + rand() 
        print(a)    
elif userint == "d":
    a = input("Enter the word:")
    a.strip()
    if a.count(" ") in (1,2) :
        reverse_splitter(a)
    elif a.count(" ") >2:
        list = a.split(" ")
        for i in list:
            list[list.index(f"{i}")] = i[len(i)-4] + i[3:len(i)-4]
        a = " ".join(list)
        print(a)
        exit()
    if len(a) < 3:      
        print(reverse(a))
    else:
        a = a[len(a)-4] +a[3:len(a)-4] 
        print(a)
else:
    print("invalid input")