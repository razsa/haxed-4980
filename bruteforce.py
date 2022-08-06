import hashlib

shaOne = input("Please input the hash.\n> ")

with open('10-million-password-list-top-1000000.txt') as pwlist:
	new_pwlist = [passwordGuess[:-1] for passwordGuess in pwlist]

attempt = 0
i = 0

while i < len(new_pwlist):
	passwordGuess = new_pwlist[i]

	hashedGuess = hashlib.sha1(bytes(passwordGuess, 'utf-8')).hexdigest()

	if hashedGuess == shaOne:
		print(f'The password is {passwordGuess} took {attempt} attempts.')
		exit(0)
	else:
		print(f'Password: {passwordGuess}, does not match, trying next...')
		i += 1
		attempt += 1

print('Password not found!')
