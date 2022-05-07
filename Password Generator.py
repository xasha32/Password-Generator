import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("#Password Generator Project")
let_input = int(input("How many letters would you like in your password?\n"))

let_output = ''
for l in range(1, let_input+1):
    random_char = random.choice(letters)
    let_output += random_char
print(let_output)

num_input = int(input(f"How many numbers would you like?\n"))
num_output = ''
for n in range(1, num_input+1):
    random_num = random.choice(numbers)
    num_output += random_num
print(num_output)

sym_input = int(input(f"How many symbols would you like?\n"))

sym_output = ''
for s in range(1, sym_input+1):
    random_sym = random.choice(symbols)
    sym_output += random_sym
print(sym_output)

password = str(let_output) + str(num_output) + str(sym_output)

print(f"Your final password is : {password}")

# ########### To create a more strong password we can shuffle the string.

print("To make this password more stronger we have done this extra thing.")
password_list = []
password_list[:0] = password
print(password_list)

random.shuffle(password_list)
print(password_list)

password2 = ''
for p in password_list:
    password2 += p
print(f"Your final and more strong password is : {password2}")







