import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
  try:
    # join working directory and file_path
    file_path_full = os.path.join(working_directory, file_path)

    # Makes sure it is within the specified working_directory including path traversal
    if not os.path.abspath(file_path_full).startswith(os.path.abspath(working_directory)):
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(file_path_full):
      return f'Error: File "{file_path}" not found.'

    if not os.path.abspath(file_path_full).endswith('.py'):
      return f'Error: "{file_path}" is not a Python file.'

    args_string = ""

    for arg in args:
      args_string += arg + " "

    args_string = args_string[:-1]

    if not len(args) == 0:
      completed_process = subprocess.run(["python", file_path_full, args_string], capture_output=True, timeout=30)
    else:
      completed_process = subprocess.run(["python", file_path_full], capture_output=True, timeout=30)
    
    completed_process_string = ""

    if len(completed_process.stdout) != 0 or len(completed_process.stderr) != 0:
      completed_process_string = f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}'

    if completed_process.returncode != 0:
      completed_process_string += f'\nProcess exited with code {completed_process.returncode}'
    
    if len(completed_process_string) == 0:
      return "No output produced."

    return completed_process_string

  except Exception as e:
    return f"Error: executing Python file: {e}"