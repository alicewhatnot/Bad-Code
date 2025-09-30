def inputNum(case):
    valid_entry = False
    while valid_entry == False:
        try:
            if case == "":
                num = int(input("Enter a number: "))
            if case == "base":
                num = int(input("Enter a base: "))
            if num > -1:
                valid_entry = True
            else:
                print ("Not a valid input.")
                
            if case == "base" and (num < 2 or num > 35):
                valid_entry = False
                print ("Not a valid input.")
        except:
            print ("Not a valid input.")
    return num

def getLargestPower(number,base):
    found_largest = False
    largest_power = 0
    while found_largest == False:
        if number // (base**largest_power) > 0:
            largest_power += 1
        else:
            found_largest = True
    return (largest_power - 1)

def calcHex(number,largest_power,base):
    power = largest_power
    output = ""
    while power > -1:
        divisor = base**power
        amount_of_divisor = number // divisor
        number -= divisor*amount_of_divisor
        if amount_of_divisor > 9:
            amount_of_divisor += 55
            amount_of_divisor = chr(amount_of_divisor)
        output += str(amount_of_divisor)
        power -= 1
    return output

denary = inputNum("")
base = inputNum("base")
largest_power = getLargestPower(denary,base)
print (f"{denary} in base {base}:")
print (calcHex(denary,largest_power,base))



