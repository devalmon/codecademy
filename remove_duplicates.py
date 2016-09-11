def remove_duplicates(input_list):
	listWithOutDuplicates = []
	for i in input_list:
		if i not in listWithOutDuplicates:
			listWithOutDuplicates.append(i)
	return listWithOutDuplicates

print remove_duplicates([1,1,2,2])