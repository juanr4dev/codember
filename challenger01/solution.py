import re

requiredFields = ('usr','eme','psw','age','loc','fll')

## fll:111 eme:yrfa@gmail.com usr:@codember -> {"fll":"111","eme":"yrfa@gmail.com","usr":"@codember"}
def line2Dict(line):
    lst = re.split(':| ',line.strip())
    toDict = map( lambda i: (lst[i],lst[i+1]), range(len(lst)-1)[::2])
    return dict(toDict)
    
def loadInput():
    profiles = []
    profile = ''
    with open('users.txt') as f:
        for line in f.readlines():
            if not line.strip():
                profiles.append(line2Dict(profile))
                profile = ''
                continue
            profile += ' ' + line.strip()

    profiles.append(line2Dict(profile))
    return profiles

def hasCorrectKeys(profile):
    if all(key in profile for key in requiredFields):
        return True 

def main():
    input = loadInput()
    filtered = list(filter(hasCorrectKeys,input))
    print(f'{len(filtered)}'+filtered[-1]['usr'] )

if __name__ == '__main__':
    main() 