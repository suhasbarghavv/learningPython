##All Divisors
import sys

num = int(input ("Enter a number to find all the divisors of the number:"))

divisors = []

loop = 1;

while (loop <= num/2):
 if (num%loop == 0):
   divisors.append(loop)
 loop = loop + 1
divisors.append(num)

for divisor in divisors:
 print (divisor)