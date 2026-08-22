# The following code demonstrates how to append text to an existing file in Python. It opens the file in append mode, writes a new line, and then closes the file.

# f=open("demo1.txt", "a")
# f.write("\nThis is an appended line.")
# f.close()

# Automatically close the file after appending to it
with open("demo1.txt", "a") as f:
    f.write("\nThis is an appended line.")