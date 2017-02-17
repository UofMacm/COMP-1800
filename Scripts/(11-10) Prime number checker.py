# This program lists all the prime numbers between 2 and 1000.

n = 2       # n ranges from 2 to 1000 - for each n, we determine
            #  if it's prime and print it out if so
while n <= 1000:
    
    # check all the possible factors of n from 2 to n-1, inclusive
    factorFound = False
    f = 2
    while f < n:
        if n % f == 0:  # for f to be a factor of n, there must be no remainder from n/f
            factorFound = True        
            break   # no need to continue checking factors, so leave the loop
        f = f + 1

    # if a factor hasn't been found, n must be prime
    if not factorFound:
        print(n)

    n = n + 1
