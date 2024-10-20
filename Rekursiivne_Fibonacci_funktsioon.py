def fibonacci(n):

     if n == 0:  # Baasjuhtum: F(0) = 0
        return 0
     elif n == 1:  # Baasjuhtum: F(1) = 1
        return 1
     else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Rekursiivne kutse
    

# Kutsume välja n-nda Fibonacci numbri
n = 2
print(f"{n}-nda Fibonacci numbri väärtus on: {fibonacci(n)}")  # Väljund: 1
