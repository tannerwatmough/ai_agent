import os
from functions.config import MAX_CHAR_LIMIT

def get_file_content(working_directory, file_path):
	try:
		# join working directory and file_path
		file_path = os.path.join(working_directory, file_path)

		# Makes sure it is within the specified working_directory including path traversal
		if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
			return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

		# if not a file, give error
		if not os.path.isfile(file_path):
			return f'Error: File not found or is not a regular file: "{file_path}"'
		
		string = ""

		# read out MAX_CHAR_LIMIT of file to string
		with open(file_path, "r") as f:
			string = f.read(MAX_CHAR_LIMIT)
		
		if len(string) + 1 > MAX_CHAR_LIMIT:
			string += f' [...File "{file_path}" truncated at 10000 characters]"]'
		
		return string

	except Exception as e:
		return f"Error: {e}"
