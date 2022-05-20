
"""
fonction isPrime(n:entier) {
    debut 
        si n > 1 alors {
            si i <= n/2 alors {
                retourner n % i != 0 et isPrime(n, i+1)
            }
            fin si 
            }
            retourner n % i != 0
        fin si 
        }
    fin
}
"""


def isPrime(n: int, i: int = 2):
    if n > 1:
        if i <= n/2:
            return n % i != 0 and isPrime(n, i+1)
    return n % i != 0


print(isPrime(int(input())))
