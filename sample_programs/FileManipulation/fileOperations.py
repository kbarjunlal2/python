
try:
    with open("sample_programs/FileManipulation/sample.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError as e:
    print(f"Error {e}")

with open("sample_programs/FileManipulation/sample.txt", "r") as file:
    for line in file:
        print(line)

# with open("sample_programs/FileManipulation/sample.txt", "a") as file:
#     file.write("New Log Event Occured")
