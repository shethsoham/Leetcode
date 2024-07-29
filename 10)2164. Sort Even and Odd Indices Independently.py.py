arr = [3,2,1,4,6,7,9]
n=len(arr)
new_arr = []
for i in range(0,n):
    if arr[i]%2 == 0 :
        new_arr.insert(0,arr[i])
    else :
        new_arr.append(arr[i])

print(new_arr)