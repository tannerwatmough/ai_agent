from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
  # TESTS FOR get_files_info
  # print("Result for current directory:\n" + get_files_info("calculator", "."))

  # print("Result for 'pkg' directory:\n" + get_files_info("calculator", "pkg"))

  # print("Result for '/bin' directory:\n" + get_files_info("calculator", "/bin"))

  # print("Result for '../' directory:\n" + get_files_info("calculator", "../"))

  # TESTS FOR get_file_content
  # print("Result for 'lorem.txt':\n" + get_file_content("calculator", "lorem.txt"))

  print("Result for 'main.py':\n" + get_file_content("calculator", "main.py"))

  print("Result for 'pkg/calculator.py' directory:\n" + get_file_content("calculator", "pkg/calculator.py"))

  print("Result for '/bin/cat' directory:\n" + get_file_content("calculator", "/bin/cat"))

  print("Result for 'pkg/does_not_exist.py' directory:\n" + get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()