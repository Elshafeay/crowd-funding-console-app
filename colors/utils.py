from colors.__Class__ import Colors


def printing_warning(message):
	print(f"{Colors.WARNING}{message}{Colors.ENDC}")


def printing_error(message):
	print(f"{Colors.FAIL}{message}{Colors.ENDC}")


def printing_success(message):
	check_mark = u'\u2713'*2
	print(f"{Colors.OKGREEN}{message} {check_mark}{Colors.ENDC}\n")


def printing_the_hey(message):
	print(f"{Colors.OKBLUE}{message}{Colors.ENDC}")


def printing_bold(*message):
	for msg in message:
		print(f"{Colors.BOLD}{Colors.WARNING}{msg}{Colors.ENDC}")

