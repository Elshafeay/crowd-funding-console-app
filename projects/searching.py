import json

from printjson import PrinterJSON

import main
from colors.utils import printing_warning, printing_error, printing_bold
from projects.CRUD import listing
from projects.utils import handle_date


def search():
	while True:
		print("\nThere are multiple options for search: ")
		printing_bold("1-Using Title", "2-Using Date", "3-Using Target")
		searching_way = input("Enter your choice number: ")
		if searching_way == "1":
			search_using_title()
		elif searching_way == "2":
			search_using_date()
		elif searching_way == "3":
			search_using_target()
		elif searching_way.lower() == "cancel":
			return
		else:
			printing_warning("Wrong Option!")
			continue
		break


def search_using_title():
	title = input("Enter the title of the project you wanna search for: ")
	if title and not title.lower() == "cancel":
		query_result = list()
		p = PrinterJSON()
		for project in main.projects:
			if title.lower() in project["title"].lower():
				query_result.append(project)
		p.print_data(query_result)
		print()  # empty line for a better format
		return
	elif title.lower() == "cancel":
		return
	listing('all')


def search_using_target():
	p = PrinterJSON()
	while True:
		print("\n=> Leave the values blank for an open range <=")
		min_target = input("Enter the minimum target of your range: ")
		if min_target.lower() == "cancel":
			return
		max_target = input("Enter the maximum target of your range: ")
		if max_target.lower() == "cancel":
			return
		try:
			min_target = int(min_target) if min_target else 0
			max_target = int(max_target) if max_target else 0
			if (min_target < 0) or (max_target < 0):
				printing_warning("Error: Target must be a greater than Zero\n")
				continue
		except ValueError:
			printing_warning("Error: targets must have digits only!\n")
			continue

		if min_target and max_target:
			query_result = list()
			for project in main.projects:
				if max_target >= project["target"] >= min_target:
					query_result.append(project)
			p.print_data(query_result)
			return
		if min_target:
			query_result = list()
			for project in main.projects:
				if project["target"] >= min_target:
					query_result.append(project)
			p.print_data(query_result)
			return
		if max_target:
			query_result = list()
			for project in main.projects:
				if max_target >= project["target"]:
					query_result.append(project)
			p.print_data(query_result)
			print()  # empty line for a better format
			return
		listing('all')
		break


def search_using_date():
	while True:
		print("Do you wanna search by start date or end date?")
		printing_bold("1-Start date", "2-End date")
		chosen_key = input("Enter your choice number: ")
		if chosen_key == "1":
			chosen_key = "start_date"
		elif chosen_key == "2":
			chosen_key = "end_date"
		elif chosen_key.lower() == "cancel":
			return
		else:
			printing_warning("Error: Wrong Option!\n")
			continue

		print("Do you wanna search by the exact date or range of dates?")
		printing_bold("1-Exact date", "2-Range of dates")
		chosen_way = input("Enter your choice number: ")
		if chosen_way == "1":
			search_exact_date(chosen_key)
		elif chosen_way == "2":
			search_range_date(chosen_key)
		elif chosen_key.lower() == "cancel":
			return
		else:
			printing_warning("Error: Wrong Option!\n")


def search_exact_date(date_option):
	query_result = list()
	p = PrinterJSON()
	while True:
		date_input = input("Please enter the date to be used in search [yyyy-mm-dd]: ")
		date = handle_date(date_input)
		if date:
			break
		elif date_input.lower() == "cancel":
			return
	for project in main.projects:
		if str(date) == project[date_option]:
			query_result.append(project)
	p.print_data(query_result)
	print()  # empty line for a better format
	return


def search_range_date(date_option):
	query_result = list()
	p = PrinterJSON()
	while True:
		while True:
			start_date_input = input("Please enter the start date of the range [yyyy-mm-dd]: ")
			start_date = handle_date(start_date_input)
			if start_date:
				break
			elif start_date_input.lower() == "cancel":
				return

		while True:
			end_date_input = input("Please enter the end date of the range [yyyy-mm-dd]: ")
			end_date = handle_date(end_date_input)
			if end_date:
				break
			elif end_date_input.lower() == "cancel":
				return

		if start_date < end_date:
			break
		printing_error("Error: start date can't be later than end date!\n")

	for project in main.projects:
		if str(end_date) >= project[date_option] >= str(start_date):
			query_result.append(project)
	p.print_data(query_result)
	print()  # empty line for a better format
	return
