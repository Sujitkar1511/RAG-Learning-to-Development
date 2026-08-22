# This is a sample code to write to a file in Python.

# f=open("demo1.txt", "w")
# f.write("Hello, World!")
# f.close()


# Automatically close the file after writing to it
with open("demo1.txt", "w") as f:   
    f.write("Hello, World!")    
