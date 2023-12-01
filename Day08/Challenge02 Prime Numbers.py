#Write your code below this line 👇

def prime_checker(number):
    if n == 1:
        print("It's not a prime number.")
    else:
        for prime_checker_number in range(2, number):
            if number % prime_checker_number == 0:
                print("It's not a prime number.")
                exit()

        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
