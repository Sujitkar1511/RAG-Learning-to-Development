#simple file handling in python

# f=open("demo.txt", "r")

# data=f.read()

# print(data)

# f.close()

#automatically close the file after reading it

with open("demo.txt", "r") as f:
    data=f.read()
    print(data)
