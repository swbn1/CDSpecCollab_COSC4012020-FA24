import os
from pathlib import Path  #The Python Pathlib package offers a number of classes that describe file system paths with semantics suitable for many operating systems.
from typing import Sequence #importing important libraries that will be needed for the code


import pytest

ROOT_DIR_PATH = Path(__file__).parent.resolve()
PRODUCTION_DOTENVS_DIR_PATH = ROOT_DIR_PATH / ".envs" / ".production"
PRODUCTION_DOTENV_FILE_PATHS = [
    PRODUCTION_DOTENVS_DIR_PATH / ".django",
    PRODUCTION_DOTENVS_DIR_PATH / ".postgres",
]
DOTENV_FILE_PATH = ROOT_DIR_PATH / ".env" #Dotenv is a zero-dependency module that loads environment variables from a .env file


def merge(
    output_file_path: str, merged_file_paths: Sequence[str], append_linesep: bool = True
) -> None:
    with open(output_file_path, "w") as output_file:  #Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.
        for merged_file_path in merged_file_paths:
            with open(merged_file_path, "r") as merged_file:
                merged_file_content = merged_file.read()
                output_file.write(merged_file_content) #The write() method writes a specified text to the file.
                if append_linesep:
                    output_file.write(os.linesep) 


def main():
    merge(DOTENV_FILE_PATH, PRODUCTION_DOTENV_FILE_PATHS)


@pytest.mark.parametrize("merged_file_count", range(3)) #The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function. 
@pytest.mark.parametrize("append_linesep", [True, False])
def test_merge(tmpdir_factory, merged_file_count: int, append_linesep: bool):
    tmp_dir_path = Path(str(tmpdir_factory.getbasetemp())) #The tmpdir and tmpdir_factory fixtures are similar to tmp_path and tmp_path_factory, but use/return legacy py.path.local objects rather than standard pathlib.Path objects.

    output_file_path = tmp_dir_path / ".env"

    expected_output_file_content = "" #the output will be stored here
    merged_file_paths = [] #used for storing the merged files
    for i in range(merged_file_count):
        merged_file_ord = i + 1

        merged_filename = ".service{}".format(merged_file_ord)
        merged_file_path = tmp_dir_path / merged_filename

        merged_file_content = merged_filename * merged_file_ord

        with open(merged_file_path, "w+") as file:
            file.write(merged_file_content)

        expected_output_file_content += merged_file_content
        if append_linesep: #here we are checking the conditions
            expected_output_file_content += os.linesep #if condition is true

        merged_file_paths.append(merged_file_path) #else

    merge(output_file_path, merged_file_paths, append_linesep)

    with open(output_file_path, "r") as output_file:
        actual_output_file_content = output_file.read()

    assert actual_output_file_content == expected_output_file_content


if __name__ == "__main__":
    main()
