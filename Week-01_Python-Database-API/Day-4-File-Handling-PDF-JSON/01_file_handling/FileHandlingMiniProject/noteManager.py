#read 
def read_file():
    with open("note.txt", "r") as f:
        data = f.read()
        print(data)

# write
def write_file(sentence):
    with open("note.txt", "w") as f:
        f.write(sentence + "\n")

# append
def append_file(sentence):
    with open("note.txt", "a") as f:
        f.write(sentence + "\n")

#clear
def clear_file():
    with open("note.txt", "w") as f:   
        f.write("")


while True:
    print("1. Add Note")
    print("2. View Notes")
    print("3. Add More Notes")
    print("4. Clear All Notes")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sentence = input("Enter the sentence to write: ")
        write_file(sentence)
    elif choice == "2":
       read_file()
    elif choice == "3":
        sentence = input("Enter the sentence to append: ")
        append_file(sentence)
    elif choice == "4":
        clear_file()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
