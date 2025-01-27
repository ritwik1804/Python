import time

t = time.strftime('%H: %M: %S')
hour = int(time.strftime('%H'))
hour = int(input("Enter the time"))
print(hour)

if(hour >= 0 and hour < 12):
    print("Good Morning sir")
elif(hour >= 12 and hour < 18):
    print("Good Afternoon sir")
if(hour>= 18 and hour < 0 ):
    print("Good Night sir")
