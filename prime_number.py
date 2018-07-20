a=int(input('please enter the last number of your range ( : ? ) : '))
b=int(input('please enter the first number of your range ( ? : ) : '))
prime_number = []
for i in range(b,a+1):
    prime_number.append(i)
    for j in range(2,i):
        if i%j == 0:
            prime_number.remove(i)  
            break

print(prime_number)