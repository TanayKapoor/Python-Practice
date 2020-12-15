def format_name(first_name, last_name):
	# code goes here
	string = "Name: "
	if first_name != "" and last_name != "":
	  string += last_name + ", " + first_name
	elif first_name != "" and last_name == "":
	  string += first_name
	elif first_name == "" and last_name != "":
	  string += last_name
	else:
	  string = ""
	return string

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""
