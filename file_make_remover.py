import os
import random as rand
string="abcdefghijk"
lst=[i for i in string]
# file=open("test/ext.txt","x")
for i in range(100):
    name=""
    for i in range(6) :
        name= name+rand.choice(lst)
        file_path=f"test/{name}.txt"
    if os.path.isfile(file_path):
        print(f"file: {name}.txt already exists")
    else:
        open(file_path,"x")
import os
for i in os.listdir("test"):
    os.remove(f"test/{i}")

