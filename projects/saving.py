import main
import os
import json
from projects import json_file, __full_path__


def save_all_projects():
	with open(os.path.join(__full_path__, json_file), "w") as f:
		obj = dict()
		obj["projects"] = main.projects
		f.write(json.dumps(obj, indent=4))


def save_new_project(project):
	main.projects.append(project)
	main.my_projects.append(project)

	# sorting by id
	main.projects = sorted(main.projects, key=lambda prj: prj["id"])
	main.my_projects = sorted(main.my_projects, key=lambda prj: prj["id"])
	save_all_projects()
