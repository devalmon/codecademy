def purify(numbers):
	filteredList = []
	for i in numbers:
		if i % 2 == 0 :
			filteredList.append(i)
	return filteredList
print purify([1,2,3,3,4,5,6])
print purify([4, 5, 5, 4])