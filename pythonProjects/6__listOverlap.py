##List Overlap
import sys

firstList   = [1, 2, 3, 4, 5, 6]
secondList  = [6, 7, 8, 9, 10]
overlapList = []

for element in firstList:
    if element in secondList:
        overlapList.append(element)

for element in overlapList:
    print(element)