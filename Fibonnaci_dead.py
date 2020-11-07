# Counts the immortal Fibbonnaci Rabbits with the basic usage of Dynamic programming

l = [1, 1]
offsprings = 1 # nr of offsprings that each pair produces in pairs
months = 3 # nr. of months a rabbit lives
# n =

#def fib(n):
#    d = 0
#    if n > len(l) - 1:
#        print(n)
#        d = fib(n - 2) + o*(fib(n - 3)) #- fib(n - m)
#        print(d)
#        l.append(d)
        #print(str(d) + '!')
        #print(str(n) + '!')
    #print(n)
    #print(d)
#    print(l)
#    print(l[n])
#    return l[n]

#fib(29) # = 357913941, [1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, 87381, 174763, 349525, 699051, 1398101, 2796203, 5592405, 11184811, 22369621, 44739243, 89478485, 178956971, 357913941]
#fib(4)

#For m = 2, q = 1
#For m = inf, q= Fn-1 + Fn-2
#between?

#Intuitive version for m = 3.

def fibdthree(n):
    q = 0
    while q < n:
        l.append(l[q] + l[q+1])
        print(l)
        q += 1

def fibd(n, o, m):
    q = 0
    while q <= n:
        while q < m:
            l.append(l[q] + o*l[q+1])
            q += 1
            print(l,'!')
        l.append(l[q] + o*l[q+1] - l[q-(m+1)])
        q += 1
        print(l)


#fibdthree(6)
fibd(3,1,3)