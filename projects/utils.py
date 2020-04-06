import datetime
import re
import main
from colors.utils import printing_warning
from projects.loading import load_all_projects


def create_project_object(project_id, title, details, target, start_date, end_date, created_at):
	project = dict()
	project["id"] = project_id
	project["title"] = title
	project["details"] = details
	project["target"] = target
	project["start_date"] = str(start_date)
	project["end_date"] = str(end_date)
	project["publisher_id"] = main.current_user["id"]
	project["published_at"] = created_at
	return project


def remove_project_from_lists(project):
	main.projects.remove(project)
	main.my_projects.remove(project)


def get_maximum_project_id():
	load_all_projects()
	ids = [project["id"] for project in main.projects]
	if len(ids) > 0:
		return max(ids)
	else:
		return 0


def handle_date(date):
	date_regex = "^2[0-9]{3}-[0-9]{1,2}-[0-9]{1,2}$"
	if re.match(date_regex, date):
		year, month, day = [int(i) for i in date.split("-")]
		if (13 > month > 0) and (32 > day > 0):
			date = datetime.date(year, month, day)
			return date
	printing_warning("Error: Wrong Date Format!\n")
	return None
