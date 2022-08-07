number=int(input("Enter a positive number: "))
print("\n")                 
print(f"Prime numbers below {number} are")
def print_prime():
    sum_of_prime_numbers=0
    number_of_prime_numbers=0
    for i in range(2,number):
            for j in range (2,i):        
                if i%j==0:
                    break
            else:
                print(i)
                number_of_prime_numbers+=1
                sum_of_prime_numbers+=i
    average=sum_of_prime_numbers/number_of_prime_numbers
    print("\n")
    print(f"Number of prime numbers printed below {number} are",number_of_prime_numbers)
    print("\n")
    print("The sum of the prime numbers printed is",sum_of_prime_numbers)
    print("\n")
    print("The average of the prime numbers is",average)
print_prime()
    
        
    
                
        
                
                
