def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        # Read the contents of the file
        content = file.read()
        # Print the content
        return content
