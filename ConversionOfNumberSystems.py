import time

def decimalToBinary():
    decimal = int(input("Write a decimal number:"))

    binaryList = []

    for i in range((decimal//2)+2):
        binaryList.append(decimal % 2)
        decimal = int(decimal//2) 

        if decimal == 1:
            binaryList.append(1)
            break

        if decimal == 0:
            binaryList.append(0)
            break

    binaryList.reverse()


    for i in binaryList:
        print(i,end="")
    
    

def decimalToHexadecimal():
    decimal = int(input("Decimal:"))

    decimalList = []
    hexa = []
    numbers = {
            "10" : "A",
            "11" : "B",
            "12" : "C",
            "13" : "D",
            "14" : "E",
            "15" : "F"
        }

    for i in range((decimal // 16) +2):
        if decimal // 16 < 16:
            decimalList.append(decimal // 16)
            decimalList.append(decimal % 16)
            decimal = decimal // 16
            break

        elif decimal // 16 >= 16:
            decimalList.append(decimal % 16)
            decimal = decimal // 16
    
        else:
            pass

    for i in decimalList:
        if i > 9:
            hexa.append(numbers[str(i)])

        else:
            hexa.append(str(i))

    if len(hexa) == 1:
        print(f"Hexadecimal: {hexa[0]}")

    elif len(hexa) == 2:
        print(f"Hexadecimal: {hexa[0]}{hexa[1]}")

    elif len(hexa) == 3:
        print(f"Hexadecimal: {hexa[0]}{hexa[1]}{hexa[2]}")

    elif len(hexa) == 4:
        print(f"Hexadecimal: {hexa[0]}{hexa[1]}{hexa[2]}{hexa[3]}")

    elif len(hexa) == 5:
        print(f"Hexadecimal: {hexa[0]}{hexa[1]}{hexa[2]}{hexa[3]}{hexa[4]}")

    else:
        print("You can't compute your number yet with this programme!")


def binaryToDecimal():

    binary = input("Write a binary number:")
    binaryList = [i for i in binary]

    twoPowers = [1,2,4,8,16,32,64,128]
    sumsOfDecimal = 0

    y = len(binaryList)
    binaryList.reverse()

    for i in range(int(y)):
        if binaryList[i] == "0":
            twoPowers.pop(0)

        elif binaryList[i] == "1":
            sumsOfDecimal += twoPowers[0]
            twoPowers.pop(0)

    print(f"Decimal number:{sumsOfDecimal}")

def binaryToHexadecimal():
    binary = input("Write a binary number:")
    binaryList = [i for i in binary]

    twoPowers = [1,2,4,8,16,32,64,128]

    letters = {
        "10" : "A",
        "11" : "B",
        "12" : "C",
        "13" : "D",
        "14" : "E",
        "15" : "F"
    }

    sums = 0
    letter = 0
    digit = 0

    hexa = []

    y = len(binaryList)
    binaryList.reverse()

    for i in range(int(y)):
    
        if binaryList[i] == "0":
            twoPowers.pop(0)
            if (i == 3 or i ==7) and sums < 10:
                twoPowers = [1,2,4,8,16,32,64,128]
                digit = sums
                hexa.append(digit)
                sums = 0

        elif binaryList[i] == "1":
            sums += twoPowers[0]
            twoPowers.pop(0)
            if i != 7 and sums > 9:
                letter = sums
                hexa.append(letters[str(letter)])
                sums = 0
                twoPowers = [1,2,4,8,16,32,64,128]

            elif i == 7 and sums > 9:
                letter = 0
                letter = sums
                hexa.append(letters[str(letter)])
                sums = 0
                twoPowers = [1,2,4,8,16,32,64,128]

            elif i == 3 and sums < 10:
                twoPowers = [1,2,4,8,16,32,64,128]
                digit = sums
                hexa.append(digit)
                sums = 0
            else:
                pass
        else:
            pass
    
    if len(hexa) == 2:
        print(f"Hexadecimal number:{str(hexa[1])+str(hexa[0])}")

    elif len(hexa) == 1:
        print(f"Hexadecimal number:{str(hexa[0])}")
    
    else:
        print("You can't write over 8 bit")

def main():
    while True:
        
        print("\n"+"WELCOME".center(50,"*"))
        choice = input("\n[1] Converting Binary to Decimal\n[2] Converting Binary to Hexadecimal\n[3] Converting Decimal to Binary\n[4] Converting Decimal to Hexadecimal\n[Q]Exit\n\nChoice:")

        if choice == "1":
            binaryToDecimal()
            time.sleep(1)

        elif choice == "2":
            print("Please write as 4 bit or 8 bit!")
            binaryToHexadecimal()
            time.sleep(1)
            
        elif choice == "3":
            decimalToBinary()
            time.sleep(1)
        
        elif choice == "4":
            decimalToHexadecimal()
            time.sleep(1)

        elif choice == "Q" or choice == "q": 
            print("Logged Out")
            break

        else:
            print("You made choice as incorrect!")
        
main()




