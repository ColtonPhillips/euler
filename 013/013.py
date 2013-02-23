# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (input.txt).

def main():
    file = open('input.txt', 'r')
    sum = 0
    for line in file:
        sum = sum + int(line)
        
    print sum    

if __name__ == "__main__":
    main()