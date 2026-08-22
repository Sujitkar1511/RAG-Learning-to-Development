with open("demo1.txt", "a+") as f:
    f.write("Hello!")
    f.seek(0)  # Move the cursor to the beginning of the file
    data = f.read()
    print(data)