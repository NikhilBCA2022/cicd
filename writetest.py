from file_writter import write_to_file

def test_write_to_file():
    
    write_to_file("test.txt", "Hello, World!")
    with open("test.txt", "r") as file:
        content = file.read()
    assert content == "Hello, World!"

    
    write_to_file("test.txt", "This is a test.")
    with open("test.txt", "r") as file:
        content = file.read()
    assert content == "Hello, World!This is a test."

   