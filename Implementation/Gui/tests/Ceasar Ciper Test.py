def change_password(password, shift):
	password = password.lower()
	encrypted_password = ""
	for c in password:
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			if num > ord("z"):
				num -= 26
			elif num < ord("a"):
				num += 26
			encrypted_password += chr(num)
		else:
			encrypted_password += c
	return encrypted_password
