# List of names to be written to the file
names = [i for i in range(10)]

for i in names:
    file_name = (f"0{i}.py")
    with open(file_name, "w") as file:
        pass
print("Created Master Janeesh")
