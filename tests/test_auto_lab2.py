import subprocess
import pytest
import os
import glob

## AI DECLARATION: I used it to generate the compiled code
# --- Temporary fixture to compile parser ---
@pytest.fixture(scope="session", autouse=True)
def compile_parser():
    """Compile all C++ source files in src/ before tests, remove binary after."""
    src_files = glob.glob("src/*.cpp")  # all cpp files in src
    include_dir = "include"
    output_binary = "parser_app"

    compile_command = ["g++", "-std=c++17", "-I", include_dir, "-o", output_binary] + src_files

    result = subprocess.run(compile_command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Compilation failed:")
        print(result.stdout)
        print(result.stderr)
        pytest.exit("Cannot run tests without compiled parser.")

    # Run tests
    yield

    # Cleanup binary
    if os.path.exists(output_binary):
        os.remove(output_binary)
#END AI DECLARATION

def run_parser(full_name, email):
    """Helper function to run the C++ parser with input."""

    # Combine inputs with newlines, as if the user pressed Enter after each
    input_text = f"{full_name}\n{email}\n"

    result = subprocess.run(
        ["./parser_app"],
        input=input_text,
        capture_output=True,
        text=True,
        check=True
    )

    # Parse the output to find the key-value pairs
    output_data = {}
    from pprint import pprint
    pprint(result.stdout.strip().splitlines())
    keys = ("First Name", "Last Name", "Username")
    key_index = 0
    for line in result.stdout.strip().splitlines():
        if ":" in line:
            output_data[keys[key_index]] = line.strip().split()[-1]
            key_index += 1

    return output_data

def test_simple_name_and_email():
    """Tests a standard first and last name."""
    name = "Jane Doe"
    email = "jane.doe@example.com"

    parsed_info = run_parser(name, email)

    assert parsed_info.get("First Name") == "Jane"
    assert parsed_info.get("Last Name") == "Doe"
    assert parsed_info.get("Username") == "jane.doe"

def test_name_with_middle_initial():
    """Tests a name that includes a middle initial."""
    name = "John Doe"
    email = "john.doe@uconn.edu"

    parsed_info = run_parser(name, email)

    assert parsed_info.get("First Name") == "John"
    assert parsed_info.get("Last Name") == "Doe"
    assert parsed_info.get("Username") == "john.doe"
