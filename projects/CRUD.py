import json

from projects.utils import *
from projects.saving import save_new_project, save_all_projects
from colors.utils import printing_error, printing_warning, printing_success
from printjson import PrinterJSON


def create_project():

	while True:
		title = input("Please enter your project title: ")
		if title and len(title) > 2 and not title.lower() == "cancel":
			break
		elif title.lower() == "cancel":
			return
		printing_error("Error: Title is too short!\n")

	while True:
		details = input("Please enter your project details: ")
		if details and len(details) > 20:
			break
		elif details.lower() == "cancel":
			return
		printing_error("Error: Too short to be details!\n")

	while True:
		target = input("Please enter your project Total target in EGP: ")
		if target.lower() == "cancel":
			return
		try:
			target = int(target)
			if target <= 0:
				printing_error("Error: Target must be greater than Zero\n")
				continue
			break
		except:
			printing_error("Error: Target must has only numbers\n")

	while True:
		while True:
			start_date_input = input("Please enter your project start date in the format yyyy-mm-dd: ")
			start_date = handle_date(start_date_input)
			if start_date:
				break
			elif start_date_input.lower() == "cancel":
				return

		while True:
			end_date_input = input("Please enter your project end date in the format yyyy-mm-dd: ")
			end_date = handle_date(end_date_input)
			if end_date:
				break
			elif end_date_input.lower() == "cancel":
				return

		if start_date < end_date:
			break

		printing_error("Error: start date can't be later than end date!\n")

	created_at = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
	project = create_project_object(
		get_maximum_project_id()+1, title, details, target, start_date, end_date, created_at)
	save_new_project(project)
	printing_success("Congratulations, Your project has been published successfully")


def edit_project(project_id):
	try:
		project_id = int(project_id)
	except ValueError:
		printing_error("Error: ID must be a number!\n")
		return
	project = get_project(project_id)
	if project:
		if not project["publisher_id"] == main.current_user["id"]:
			printing_error("Error: You're not authorized to edit this project!\n")
			return
		printing_error("\n=> Leave the values blank to keep the old ones <=")

		while True:
			title = input("Please enter the new title: ")
			if not title:
				title = project["title"]
				break
			elif title.lower() == "cancel":
				return
			elif len(title) > 2:
				break
			printing_error("Error: Title is too short!\n")

		while True:
			details = input("Please enter the new details: ")
			if not details:
				details = project["details"]
				break
			elif details.lower() == "cancel":
				return
			elif len(details) > 20:
				break
			printing_error("Error: Too short to be details!\n")

		while True:
			target = input("Please enter the new target in EGP: ")
			if target:
				if target.lower() == "cancel":
					return
				try:
					target = int(target)
					if target <= 0:
						printing_error("Error: Target must be greater than Zero\n")
						continue
					break
				except:
					printing_error("Error: Target must has only numbers\n")
			target = project["target"]
			break

		while True:
			while True:
				start_date_input = input("Please enter the new start date in the format yyyy-mm-dd: ")
				if start_date_input:
					start_date = handle_date(start_date_input)
					if start_date:
						break
				elif start_date_input.lower() == "cancel":
					return
				else:
					start_date = project["start_date"]
					break

			while True:
				end_date_input = input("Please enter the new end date in the format yyyy-mm-dd: ")
				if end_date_input:
					end_date = handle_date(end_date_input)
					if end_date:
						break
				elif end_date_input.lower() == "cancel":
					return
				else:
					end_date = project["end_date"]
					break

			if start_date < end_date:
				break

			printing_error("Error: start date can't be later than end date!\n")

		created_at = project["published_at"]
		new_project = create_project_object(
			project["id"], title, details, target, start_date, end_date, created_at)
		remove_project_from_lists(project)
		save_new_project(new_project)
		printing_success("Your project has been updated successfully")
		return

	printing_error("There is No project with this id!")


def delete_project(project_id):
	try:
		project_id = int(project_id)
	except ValueError:
		printing_error("Error: ID must be a number!\n")
		return
	project = get_project(project_id)
	if project:
		if not project["publisher_id"] == main.current_user["id"]:
			printing_error("Error: You're not authorized to delete this project!\n")
			return
		remove_project_from_lists(project)
		save_all_projects()
		printing_success("Your project has been deleted successfully")
		return
	printing_error("There is No project with this id!")


def listing(option):
	load_all_projects()
	p = PrinterJSON()
	if option.lower() == "all":
		p.print_data(main.projects)
	elif option.lower() == "mine":
		p.print_data(main.my_projects)
	else:
		printing_warning("Wrong Command! For more details see the documentation by typing 'help'")
	print()  # empty line for a better format


def get_project(project_id):
	for project in main.projects:
		if project["id"] == project_id:
			return project
	else:
		return None

