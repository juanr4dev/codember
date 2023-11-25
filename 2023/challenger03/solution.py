import collections
def invalidPolicies(policy):
    rule, text = policy.split(":")
    times, letter = rule.split(" ")
    minTimes, maxTimes = times.split("-")
    letterTimes = collections.Counter(text)
    if ( not(letterTimes[letter] >= int(minTimes) and letterTimes[letter] <= int(maxTimes))):
        return text.strip()

def main():
    invalidKeys = []
    with open('encryption_policies.txt','r') as f:
        for line in f:
            vp = invalidPolicies(line)
            if (vp): invalidKeys.append(vp)
    print(invalidKeys[41])
    print("Contraseña: %s" % invalidKeys[12])

if __name__ == '__main__':
    main()