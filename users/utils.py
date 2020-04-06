import json
import os
from users import json_file, __location__


def get_maximum_user_id():
	users = get_all_users()
	ids = [user["id"] for user in users["accounts"]]
	if len(ids) > 0:
		return max(ids)
	else:
		return 0


def save_user(user):
	users = get_all_users()
	with open(os.path.join(__location__, json_file), "w") as f:
		accounts = users.get("accounts", [])
		accounts.append(user)
		users["accounts"] = accounts
		f.write(json.dumps(users, indent=4))


def get_all_users():
	try:
		with open(os.path.join(__location__, json_file), "r") as f:
			users = json.load(f)
		return users
	except:
		with open(os.path.join(__location__, json_file), "w") as f:
			pass
		return {}
