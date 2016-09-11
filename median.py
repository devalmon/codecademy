def median(value_list):
	sorted_list = sorted(value_list)
	quantity = len(sorted_list)
	if quantity % 2 == 0:
		middle = quantity / 2
		return (sorted_list[middle] + sorted_list[middle - 1])/2.0
	else:
		middle = quantity / 2
		return sorted_list[middle]
print 'median([7,12,3,1,6]) is', median([7,12,3,1,6])
print 'median([7,3,1,4,6,6]) is', median([7,3,1,4,6,6])