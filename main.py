#! python

from documentation.doc import *
from projects.CRUD \
	import listing, create_project, edit_project, delete_project
from projects.loading import load_all_projects
from projects.searching import search
from users.authentication import login, check_logged_in, logout
from colors.utils import printing_warning, printing_error, printing_the_hey
from users.registeration import register

current_user = {"email": ""}
projects = []
my_projects = []


def start():
	printing_the_hey("\n\t+====================================================+")
	printing_the_hey("\t|            Welcome to our application!             |")
	printing_the_hey("\t+====================================================+")
	printing_warning("\nFor any details you can checkout out the documentation by typing 'help'")
	load_all_projects()
	while True:
		try:
			input_array = input(">> ")
		except (EOFError, KeyboardInterrupt):
			printing_the_hey("\nHave a nice day! :)")
			break

		command = input_array.split(" ")
		if command[0].lower() == "help" and len(command) == 1:
			show_help()
		elif command[0].lower() == "exit" and len(command) == 1:
			printing_the_hey("Have a nice day! :)")
			break
		elif command[0].lower() == "menu" and len(command) == 1:
			show_menu()
		elif command[0].lower() == "login" and len(command) == 1:
			if current_user["email"]:
				printing_error("Error: You already logged in!\n")
				continue
			login()
		elif command[0].lower() == "logout" and len(command) == 1:
			if not check_logged_in():
				continue
			logout()
			printing_the_hey("Hope to see you soon! ;)")
		elif command[0].lower() == "register" and len(command) == 1:
			if current_user["email"]:
				printing_error("Error: You already using an account!\n")
				continue
			register()
		elif command[0].lower() == "create" and len(command) == 2:
			if command[1].lower() == "project":
				if check_logged_in():
					create_project()
				continue
			printing_warning("Wrong Command! For more details see the documentation by typing 'help'")
		elif command[0].lower() == "list" and len(command) == 2:
			if check_logged_in():
				listing(command[1])
		elif command[0].lower() == "edit" and len(command) == 2:
			if check_logged_in():
				edit_project(command[1])
		elif command[0].lower() == "delete" and len(command) == 2:
			if check_logged_in():
				delete_project(command[1])
		elif command[0].lower() == "search" and len(command) == 1:
			if check_logged_in():
				search()
		elif input_array:
			printing_warning("Wrong Command! For more details see the documentation by typing 'help'")


if __name__ == "__main__":
	start()
