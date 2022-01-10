def repeat (arr:list, x:int,n:int, i:int=0):
    if i == n :
        return 0
    else : 
        if arr[i] == x :
            return 1 + repeat(arr, x, i+1)
        else :
            return repeat(arr, x, i+1 )
arr = [1,1,3,5,6,8,1]

print(repeat(arr, 1,len(arr) ))