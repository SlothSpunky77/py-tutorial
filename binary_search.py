
beg = 0;
end = 7;
mid = int((beg + end)/2)
a = [1,2,3,4,5,6,7,8]
print(a)    
n = int(input("Enter a number from 1 to 8: "))
p = n - 1
c = 1000
if (p >= 0 and p <= 7):
    while (c != mid):
        if (p < mid):
            end = mid;
        elif (p > mid):
            beg = mid;
        else:
            c = mid;
else:
    print("Invalid number. Idiot.")
print("The position is: ", c)
