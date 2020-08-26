# Shahriyar Mammadli
# LeetCode problem '412. Fizz Buzz' solution

def fizzBuzz(n):
    fizzBuzz = list(range(1,n+1))
    return list(map(lambda i: "FizzBuzz" if i % 15==0 else("Buzz" if i % 5==0 else("Fizz" if i % 3 == 0 else str(i))), fizzBuzz))
print(fizzBuzz(15))