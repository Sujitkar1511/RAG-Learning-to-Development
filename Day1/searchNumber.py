numbers=(0,1,2,3,4,5,6,7,8,9)
temp=0
n=(int(input("Enter a number: ")))
i=0
while i<len(numbers):
    if(numbers[i]==n):
       temp=1
        
    i+=1  

if(temp==1):
    print("Number is found")    
else:
    print("Number is not found")
    