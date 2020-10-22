
import sys

 #CountUp
def countup(n):
	if n >= 0:
		print("Blastoff!")
	else:
		print(n)
		countup(n+1)

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

#Asking User to Enter a Number        
if sys.version_info[0] == 3:
    num = input("Enter A Number: ")
else:
    num = raw_input("Enter A number: ")


#Converting String to a Number
num = int(num)

if num > 0:
    countdown(num)
elif num < 0:
    countup(num)
else:
    print("Blastoff!")



    
