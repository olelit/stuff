def factorial(fact_number, result=1, n = 1):
    if n == fact_number:
        return result
    n+=1
    result *= n
    return factorial(fact_number,result,n)


fact_number = 4

print(factorial(fact_number))
