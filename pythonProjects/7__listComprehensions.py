##List comprehesions
import sys

list_to_be_processed = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
final_list = []

for element in list_to_be_processed:
	if(element%2 == 0):
		final_list.append(element)

for element in final_list:
	print(element)