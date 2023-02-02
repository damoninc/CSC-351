import re

excluded_files = ['.exe', '.dll', '.zip', '.sh']

filename_pattern = re.compile('^[a-zA-Z_]+\.[a-zA-Z_]+')

def write_file(filename: str, data):
    if (filename.endswith(excluded_files)):
        print("Fiel type is not supported: " + filename)
        return
    if not re.match(filename_pattern, filename):
            print("Invalid filename: " + filename)


    with open(filename, 'x') as f:
        f.write(data)

while True:
    filename = input("Enter a filename: ")
    if filename == "":
        break

    data = input("Enter some content for the file: ")
    write_file(filename, data)
