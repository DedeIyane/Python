turns = int(input('Enter the number of prime numbers: '))
primes= []
if turns <= 1:
    print(f'{turns} is not a prime.')

elif turns > 1:
    if len(primes)< turns:
        for i in range(turns):
            for j in range(2, i):
                if j % i == 0:
                    continue
        else:
            primes.append(i)
        i+= 1
print(primes)
    