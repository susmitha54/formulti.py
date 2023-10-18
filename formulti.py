'''
1. Print the following using for loop
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5

'''

i=int(input("Enter the number:"))
print("The multiplication table of:",i)
for num in range(1,6):
    print(i,"*",num,"=",i*num)