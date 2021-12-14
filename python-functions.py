#Solutuion.1

def sum_to(n):
    return sum(range(n+1))
print(sum_to(6))
print(sum_to(10))

#Solution.2

def largest(n):
    return max(n)
print (largest([1,2,3,4,0]))
print (largest([10, 4, 2, 231, 91, 54]))

#Solution.3

def occurances(a, b):
    return a.count(b)
print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

#Solution.4

def product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

#Solution.5

def product(*args):
    product = 1
    for a in args:
        product *= a
    return product
print(product(2,-5,-5))