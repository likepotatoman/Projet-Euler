fib_answers = {}
def fib(n):
    global fib_answer 
    if n in fib_answers.keys():
        return fib_answers[n]
    
    if n == 1 or n == 2:
        return 1

    fib_answer = fib(n - 1) + fib(n - 2)
    fib_answers[n] = fib_answer
    return fib_answer

i = 1
while len(str(fib(i))) != 1000:
    i += 1
print(i)
