# Project euler problem 42

ASCII_OFFSET = 64

datafile = open("42.txt", "r")

words = datafile.readline().strip('"').split('\",\"')

numbers = []

for word in words:
	temp = []
	for letter in word:
		temp.append(ord(letter) - ASCII_OFFSET)
	numbers.append(temp)

triangle_numbers = []
for n in range(1, 300):
	triangle_numbers.append((n/2)*(n+1))

count = 0
not_count = 0
for word in numbers:
	word_sum = 0
	for number in word:
		word_sum += number
	if word_sum in triangle_numbers:
		count += 1
	else:
		not_count += 1

print(count)
