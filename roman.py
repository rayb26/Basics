# By: Jelson and Rayhan Biju
# Emails: Jelson9854@vt.edu and rayhanbiju@vt.edu

#dict to remember values
r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

#Converts numbers to roman numerals - Max number is 3999
#Code by Jelson
#Navigator by Rayhan
def int_to_roman(num):
    #our roman numeral
    val = ""
    #loop to iterate through the roman numeral until solved
    while num > 0:
        #adds M's for each thousand
        if(num >= 1000):
            val = val + "M"
            num = num - 1000
            
        #adds CM for each nine hundred
        if(num >= 900):
            val = val + "CM"
            num = num - 900
            
        #adds D for each five hundred
        if(num >= 500):
            val = val + "D"
            num = num - 500
            
        #adds CD for each four hundred
        if(num >= 400):
            val = val + "CD"
            num = num - 400
            
        #adds C's for each hundred
        if(num >= 100):
            val = val + "C"
            num = num - 100
        
        #adds XC for each ninety
        if(num >= 90):
            val = val + "XC"
            num = num - 90
            
        #adds L for each fifty
        if(num >= 50):
            val = val + "L"
            num = num - 50
            
        #adds XL for each fourty
        if(num >= 40):
            val = val + "XL"
            num = num - 40
            
        #adds X's for each ten
        if(num >= 10):
            val = val + "X"
            num = num - 10
            
        #adds IX's for each nine
        if(num >= 9):
            val = val + "IX"
            num = num - 9
            
        #adds V for each five
        elif(num >= 5):
            val = val + "V"
            num = num - 5
            
        #adds IV for each four
        if(num >= 4):
            val = val + "IV"
            num = num - 4
            
        #adds I's for each ones
        if(num >= 1):
            val = val + "I"
            num = num - 1

    return val

# Code by Rayhan, Navigator by Jelson 
# The following function converts a roman numeral to an integer. The function
# works by adding or subtracting integer values based on comparing adjacent roman numerals respectively. 
# Visual Studio Code was used as the text editor for this function. 
def convert_roman_to_integer(roman_numeral): 

    # Dict to hold denominations
    roman_numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    complete_integer = 0  

    # Iterate through Roman Numeral string 
    for i in range(len(roman_numeral)-1): 

        # Checking if current roman numeral is smaller than the adjacent one 
        if roman_numerals[roman_numeral[i]] < roman_numerals[roman_numeral[(i+1)]]: 
            # Subtract roman numeral value 
            complete_integer -= roman_numerals[roman_numeral[i]]
        else: 
            # Else add current value of numeral 
            complete_integer += roman_numerals[roman_numeral[i]]
    
    # For the last numeral add the value to the result 
    return complete_integer + roman_numerals[roman_numeral[-1]]



# Test Cases Below

#returns the values of roman_to_int
print(int_to_roman(3))
print(int_to_roman(58))
print(int_to_roman(1994))

#Should return the values from int_to_roman
print(convert_roman_to_integer("III"))
print(convert_roman_to_integer("LVIII"))
print(convert_roman_to_integer("MCMXCIV"))