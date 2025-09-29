from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
  # TESTS FOR get_files_info
  # print("Result for current directory:\n" + get_files_info("calculator", "."))

  # print("Result for 'pkg' directory:\n" + get_files_info("calculator", "pkg"))

  # print("Result for '/bin' directory:\n" + get_files_info("calculator", "/bin"))

  # print("Result for '../' directory:\n" + get_files_info("calculator", "../"))

  # TESTS FOR get_file_content
  # print("Result for 'lorem.txt':\n" + get_file_content("calculator", "lorem.txt"))

  # print("Result for 'main.py':\n" + get_file_content("calculator", "main.py"))

  # print("Result for 'pkg/calculator.py' directory:\n" + get_file_content("calculator", "pkg/calculator.py"))

  # print("Result for '/bin/cat' directory:\n" + get_file_content("calculator", "/bin/cat"))

  # print("Result for 'pkg/does_not_exist.py' directory:\n" + get_file_content("calculator", "pkg/does_not_exist.py"))

  # TESTS FOR write_file
  # print("Result for 'lorem.txt':\n" + write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

  # print("Result for 'pkg/morelorem.txt':\n" + write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

  # print("Result for '/tmp/temp.txt':\n" + write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

  # TESTS FOR run_python_file
  print("Result for 'main.py':\n" + run_python_file("calculator", "main.py"))

  print("Result for 'main.py' with args '3 + 5':\n" + run_python_file("calculator", "main.py", ["3 + 5"]))

  print("Result for 'tests.py':\n" + run_python_file("calculator", "tests.py"))

  print("Result for '../main.py':\n" + run_python_file("calculator", "../main.py"))

  print("Result for 'nonexistent.py':\n" + run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    main()