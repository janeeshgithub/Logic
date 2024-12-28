# List of names to be written to the file
names = [str(chr(i)) for i in range(64,86)]

for i in names:
    file_name = f"0@{i}.py"
    with open(file_name, "w") as file:
        pass
print("Created Master Janeesh")
