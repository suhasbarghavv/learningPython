##Character Input
import sys
import datetime

name = input("Enter your name:")
age  = input("Enter your age:")

date = datetime.datetime.now()
year = date.year
year_100 = 100 - int(age) + year

print ("Hello, ", name, ". You will be 100 by the ", year_100)