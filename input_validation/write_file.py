def write_file(filename, data):
    with open(filename, 'x') as f:
        f.write(data)

while True:
    filename = input("Enter a filename: ")
    if filename == "":
        break

    data = input("Enter some content for the file: ")
    write_file(filename, data)
