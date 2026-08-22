with open("demo1.txt", "w+") as f:
    f.write("Hello World!")
    f.seek(0)  # Move the cursor to the beginning of the file
    data = f.read()
    print(data)