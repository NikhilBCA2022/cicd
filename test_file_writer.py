import os
from file_writter import write_to_file

def test_write_to_file(tmp_path):
    
    test_text = "Hello, pytest!"
    test_file = tmp_path / "test_output.txt"

    write_to_file(test_text, filename=str(test_file))

    with open(test_file, "r") as f:
        content = f.read()
    assert content == test_text
