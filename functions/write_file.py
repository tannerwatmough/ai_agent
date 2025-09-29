import os

def write_file(working_directory, file_path, content):
	try:
		# join working directory and file_path
		file_path = os.path.join(working_directory, file_path)

		# Makes sure it is within the specified working_directory including path traversal
		if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
			return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
		
		# write out content to file
		with open(file_path, "w") as f:
			f.write(content)
		
		return f'Successfully wrote to "{file_path} ({len(content)} characters written)'

	except Exception as e:
		return f"Error: {e}"


