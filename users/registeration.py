import re
from getpass import getpass

from colors.utils import printing_warning, printing_error, printing_success
from users.utils import save_user, get_maximum_user_id


def register():
	email_regex = "^[a-zA-Z][a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
	phone_regex = "^(002)?01[0125][0-9]+"
	while True:
		first_name = input("Please enter your first name: ")
		if first_name and not first_name.lower() == "cancel" and len(first_name) > 2 and first_name.isalpha():
			break
		elif first_name.lower() == "cancel":
			return
		printing_warning("Error: Names can have only characters and has a length of 3 or more!\n")

	while True:
		last_name = input("Please enter your last name: ")
		if last_name and not last_name.lower() == "cancel" and len(last_name) > 2 and last_name.isalpha():
			break
		elif last_name.lower() == "cancel":
			return
		printing_warning("Error: Names can have only characters and have a length of 3 or more!\n")

	while True:
		email = input("Please enter your E-mail Address: ")
		if email and not email.lower() == "cancel" and re.match(email_regex, email):
			break
		elif email.lower() == "cancel":
			return
		printing_warning("Error: Wrong Email Format!\n")

	while True:
		phone = input("Please enter your phone number: ")
		if phone and not phone.lower() == "cancel" and 14 >= len(phone) >= 11 and re.match(phone_regex, phone):
			break
		elif phone.lower() == "cancel":
			return
		printing_warning("Error: Wrong phone number Format\n")

	while True:
		password = getpass("Please enter your password: ")
		if not (password and len(password) > 7):
			printing_warning("Error: password must has at least length of 8 or more\n")
			continue
		confirm_password = getpass("Please enter your confirm password: ")
		if not confirm_password == password:
			printing_error("Error: your passwords didn't match\n")
			continue
		break

	user = dict()
	user["id"] = get_maximum_user_id() + 1
	user["first_name"] = first_name
	user["last_name"] = last_name
	user["email"] = email.lower()
	user["phone"] = phone
	user["password"] = password
	save_user(user)
	printing_success("You have registered successfully")
