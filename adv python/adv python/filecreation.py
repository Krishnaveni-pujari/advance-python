file = open("filename.txt", "mode")

# perform operation

file.close()
# Create a file
file = open("student.txt", "w")

# Write data
file.write("Name: Krishnaveni\n")
file.write("Course: BE\n")
file.write("Branch: Information Science")

# Close the file
file.close()

print("File created successfully!")
file = open("student.txt", "r")

data = file.read()

print(data)

file.close()