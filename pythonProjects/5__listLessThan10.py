##Report value less than 10.
import sys

print ("Populate the list to determine the less than 10 list, when completed press type end.")

less_than_10 = []
end_key = input()
if(end_key.isdigit()):
 less_than_10.append(end_key)

while (end_key != "end"):
 end_key = input()
 if (end_key.isdigit()):
   if (int(end_key) < 10):
     less_than_10.append(end_key)

for num in less_than_10:
 print (num)