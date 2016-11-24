def array_left_rotation(a, n, k):
    #a is array
    #n is the size of the array
    #k is number of times we will do the operation
    #x will be the actual number of iterations needed
    x = k % n
    a = a[x:] + a[:x]
    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
