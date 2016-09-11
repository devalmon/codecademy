def is_int(x):
    if x - round(x) == 0:
    	return True
    else:
        return False

print is_int(4.3)
print is_int(3.0)
print round(4.3)
print round(3.0)
