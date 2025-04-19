text = str(input("Enter the text to write to the file: "))
def write_to_file(text):
    with open("output.txt", "w") as file:
        file.write(text)
write_to_file(text)
print("Text written to output.txt successfully.")