n = int(input())
arr = (int, input().split())

if(arr[0] > arr[1]):
    x = arr[0]
    y = arr[1]

else:
    x = arr[1]
    y = arr[0]

    for m in arr:
        if m > y:
            if m > x:
                y = x
                x = m
            
            else:
                y = m
        
    print (y)






