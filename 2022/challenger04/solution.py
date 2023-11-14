import re

passMin = 11098
passMax = 98123

def searchPwd(fromNum, toNum):
    possiblePwd = []
    for pwd in range(fromNum,toNum):
        increment = True
        prevDigit = '0'
        for digit in str(pwd):
            if digit < prevDigit:
                increment = False
                break
            prevDigit = digit
        if ( increment and str(pwd).count('5') >= 2 ):
            possiblePwd.append(pwd)
    return possiblePwd

def main():
    passwords = searchPwd(passMin,passMax)
    print(f'{len(passwords)}-{passwords[55]}')

if __name__ == '__main__':
    main()