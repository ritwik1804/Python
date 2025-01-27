#import pandas
#pandas. read_csv

#import math
#result = math.sqrt(9)
#print(result)

#from math import *
#result = math.sqrt(9) * pi
#print(result)

#from math import sqrt as s
#result = s(9)

def welcome():
    print("Hii How are you")
    print(__name__)
if __name__ == "__main__":# if you want to import which is not recgonized then we can use this
    welcome()

#Modules in python
import os

#if(not os.path.exists("data")):
# os.mkdir("data")
#for i in range(0,6):
#    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")

folders = os.listdir("data")
print(folders)

print(os.getcwd())
os.chdir("/.vscode")#change directory 
print(os.getcwd())

#for folder in folders:
#    print(folder)
#    print(os.listdir(f"data{folders}"))