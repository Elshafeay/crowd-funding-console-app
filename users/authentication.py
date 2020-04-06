import main
from colors.utils import printing_error, printing_success, printing_the_hey
from projects.loading import load_my_projects
from getpass import getpass
from users.utils import get_all_users


def login():
	while True:
		email = input("Please enter your E-mail Address: ")
		if email.lower() == "cancel":
			return
		password = getpass("Please enter your password: ")
		users = get_all_users()
		for user in users.get("accounts", []):
			if user["email"] == email.lower():
				break
		else:
			printing_error("Error: User Not Found!\n")
			continue

		if user["password"] == password:
			printing_success("You have successfully logged in")
			printing_the_hey(f"Hello {user['first_name']} {user['last_name']}, Welcome here")
			main.current_user = user
			load_my_projects()
			break
		printing_error("Error: Wrong Password!\n")


def logout():
	main.current_user = {"email": ""}
	printing_success("You have successfully logged out")


def check_logged_in():
	if not main.current_user["email"]:
		printing_error("Error: You can't perform this action until you login!\n")
		return False
	return True
