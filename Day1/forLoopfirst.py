list=[10,20,30,50,60,0,2]

for i in list:
    print(i)

#search for a number in the list
n=(int(input("Enter a number: ")))

for el in list:
    if(el==n):
        print("Number is found",list.index(el))
        break   