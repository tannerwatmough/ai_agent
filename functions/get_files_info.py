import os

def get_files_info(working_directory, directory="."):
	try:
		# join working directory and directory
		directory = os.path.join(working_directory, directory)

		# Makes sure it is within the specified working_directory including path traversal
		if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

		# if not a directory, give error
		if not os.path.isdir(directory):
			return f'Error: "{directory}" is not a directory'
		
		string = ""

		# prints out the item name, size, and if its a direcotry for each item in a directory
		for item in (os.listdir(directory)):
			abs_path_dir = os.path.abspath(directory)
			item_path = abs_path_dir + "/" + item
			item_size = os.path.getsize(item_path)
			is_dir = os.path.isdir(item_path)
			string += f"- {item}: file_size={item_size} bytes, is_dir={is_dir}\n"

		# return string with last newline character removed
		return string[:-1]
	except Exception as e:
		return f"Error: {e}"
