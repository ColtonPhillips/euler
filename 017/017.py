# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters 
#used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
#(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def tens_digit_to_string(digit):
    options = {     0 : ""
                    1 : ""
                    2 : "twenty"
                    3 : "thirty"
                    4 : "forty"
                    5 : "fifty"
                    6 : "sixty"
                    7 : "seventy"
                    8 : "eighty"
                    9 : "ninety"
    
    }
    
def digit_to_string(digit):

    options ={      0 : "zero",
                    1 : "one",
                    2 : "two",
                    3 : "three",
                    4 : "four",
                    5 : "five",
                    6 : "six",
                    7 : "seven",
                    8 : "eight",
                    9 : "nine"
    } 
    
    return options[digit]
    
def main():
    pass
    
if __name__ == "__main__":
    main()