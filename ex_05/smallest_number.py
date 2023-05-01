
smallest = None
print('Before')

for i in [53,75,75,5,43343,6,-5, -4] :
	if smallest is None :
		smallest = i
	elif i < smallest :
		smallest = i 
	print("smallest", smallest)

print("After", smallest)
	