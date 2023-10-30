n1=int(input("Enter 1st 4 digit number:"))
n2=int(input("Enter 2nd 4 digit number:"))
def is_perfect_square(n):
    return n**0.5%1==0
def all_even_digit(n):
    return all(int(digit)%2==0 for digit in str(n))
perfect_even_square=[i for i in range(n1,n2+1)if is_perfect_square(i) and i%2==0 and all_even_digit(i)]
print(f"Perfect even digit with all even digit between {n1} and {n2} are:{perfect_even_square}")
