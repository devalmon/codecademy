def digit_sum(n):
	numbersToString = str(n)
	sum = 0
	for i in numbersToString:
		temp = int(i)
		sum += temp
	return sum

print digit_sum(1234)
