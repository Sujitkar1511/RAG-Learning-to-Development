# The following code demonstrates how to read from and write to a file in Python.
#  It opens the file in read and write mode,
# reads the existing content, prints it, appends a new line, and then reads the updated content.
with open("demo1.txt", "r+") as f:
    data=f.read()
    print(data)
    f.write("\nI am sujit kar")

print("\nAfter writing to the file:")

#The following code demonstrates how to read the updated content of the file after writing to it.
with open("demo1.txt", "r") as f:
    data=f.read()
    print(data)