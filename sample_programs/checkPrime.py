def isprime(num1):
    if num1 <= 1:
        return False
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True


print(isprime(1))
print(isprime(2))
print(isprime(4))
print(isprime(11))
def isprime(num1):
    if num1 <= 1:
        return False
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True


print(isprime(1))
print(isprime(2))
print(isprime(4))
print(isprime(11))
