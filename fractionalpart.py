def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
	if denominator:
	  res = numerator/denominator
	else:
	  res = 0
	res = res - int(res)
# keep just the fractional part of the quotient
	return res

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
