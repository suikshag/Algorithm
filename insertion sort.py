def insertion(arr,n):
    for i in range(1,n):
        min=arr[i]
        for j in range(0,i):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[15,8,95,4,123,453,64,89,52]
n=len(arr)
result=insertion(arr,n)
print(result)
