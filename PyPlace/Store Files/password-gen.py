# Really simple password generator by dante_nl
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_password = None

for letter in range(1, nr_letters + 1):
	random_letter = random.choice(letters)
	if letter_password != None:
		letter_password = random_letter + letter_password
	else:
		letter_password = random_letter

number_password = None

for number in range(1, nr_numbers + 1):
	random_number = random.choice(numbers)
	if number_password != None:
		number_password = random_number + number_password
	else:
		number_password = random_number

symbol_password = None

for number in range(1, nr_symbols + 1):
	random_symbol = random.choice(symbols)
	if symbol_password != None:
		symbol_password = random_symbol + symbol_password
	else:
		symbol_password = random_symbol


password = letter_password + number_password + symbol_password
print(f"The generated password is: {password}")

def Convert(string):
	list1 = []
	list1[:0] = string
	return list1

print(random.shuffle(Convert(password)))
