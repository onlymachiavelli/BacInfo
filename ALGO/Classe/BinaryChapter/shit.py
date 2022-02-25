def size(minimum: int, maximum: int):
    n = int(input("Enter N"))
    if minimum < n < maximum:
        return n
    return size(minimum, maximum)


def isPrime(n : int , i:int = 2):
    if n > 1 :
        if i <= n//2 :
            return n % i != 0 and isPrime(n , i+1) 
        return True  
    return False


def result () : 
    return 0 