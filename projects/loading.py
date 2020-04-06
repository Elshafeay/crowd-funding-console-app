import json
import os
import main


def load_all_projects():
	json_file = "projects.json"
	__full_path__ = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__)))
	try:
		with open(os.path.join(__full_path__, json_file), "r") as f:
			projects_dict = json.load(f)
			projects = projects_dict.get("projects", [])
			main.projects = projects
	except FileNotFoundError:
		with open(os.path.join(__full_path__, json_file), "w") as f:
			f.write(json.dumps({"projects": []}, indent=4))
			pass
	except Exception as ex:
		print(ex)


def load_my_projects():
	for project in main.projects:
		if project["publisher_id"] == main.current_user["id"]:
			main.my_projects.append(project)
