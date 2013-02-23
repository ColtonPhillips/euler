# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

def sum_of_digits(number):
    string_num = str(number)
    sum = 0
    for character in string_num:
        sum = sum + int(character)
    
    return sum

def main():
    number = pow(2,1000)
    print sum_of_digits(number)

if __name__ == "__main__":
    main()