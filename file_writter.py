def write_to_file(text, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(text)

if __name__ == "__main__":
    text = input("Enter the text to write to the file: ")
    write_to_file(text)
    print("Text written to output.txt successfully.")
