def genPrimes():
    known = []
    curr = 2
    while(True):
        if isPrime(curr, known):
            known.append(curr)
            yield curr
        curr = curr + 1
    
def isPrime(candidate, known):
    for prime in known:
        if candidate % prime == 0:
            return False
    return True


number = genPrimes()
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())