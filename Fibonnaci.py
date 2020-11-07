# Counts the immortal Fibbonnaci Rabbits with the basic usage of Dynamic programming

l = [1, 1]
o = 2 # nr of offsprings that each pair produces in pairs
m = 3 # nr. of months a rabbit lives
# n =

def fib(n):
    d = 0
    if n > len(l) - 1:
        d = fib(n - 1) + o*(fib(n - 2)) #- fib(n - m)
        l.append(d)
    print(n - 1)
    print(d)
    print(l)
    return l[n]

#fib(29) # = 357913941, [1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, 87381, 174763, 349525, 699051, 1398101, 2796203, 5592405, 11184811, 22369621, 44739243, 89478485, 178956971, 357913941]
fib(6)
