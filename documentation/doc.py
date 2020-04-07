import main
from colors.utils import printing_bold


def show_help():
	with open("documentation/help.txt", "r") as f:
		for line in f:
			print(line.strip())


def show_menu():
	if main.current_user["email"]:
		printing_bold(
			"* Create project",
			"* Edit your projects",
			"* Delete your projects",
			"* list projects",
			"* search for projects",
		)
		return
	printing_bold("* Login", "* Register")

