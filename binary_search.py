a = [10,28,31,43,54,61,74,87]
beg = 0
end = len(a) - 1
print(a)    
n = int(input("Enter an element: "))
while (beg <= end):
    mid = (beg + end)//2
    if (a[mid] < n):
        beg = mid + 1
    elif (a[mid] > n):
        end = mid - 1
    else:
        print("The position is: ", mid)
        quit()
else:
    print("Invalid number. Idiot.")
