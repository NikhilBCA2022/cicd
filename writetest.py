from file_writter import write_to_file

def test_write_to_file():
    write_to_file("Hello, World!")
    with open("output.txt", "r") as file:
        content = file.read()
    assert content == "Hello, World!"

          
    write_to_file("This is a test.")
    with open("output.txt", "r") as file:
        content = file.read()
    assert content == "Hello, World!This is a test."


    
 

   