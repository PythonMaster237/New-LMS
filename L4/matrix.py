matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

main = 1
secondary = 1

for row in range(3):
	for column in range(3):
		if row == column:
			element = matrix[row][column]
			main *= element

		if row + column == 2:
			element = matrix[row][column]
			secondary *= element

det = main - secondary
#print(det)

transponed = []

for column in range(3):
	temp_row = []
	for row in matrix:
		temp_row.append(row[column])
	transponed.append(temp_row)

#for row in transponed:
#	for element in row:
#		print(element, end=' ')
#	print('')



alice = [89, 78, 90]
bob = [94, 93, 77]
joe = [76, 90, 72]

tests = list(zip(alice, bob, joe))
for test in tests:
	print(sum(test)/len(test))