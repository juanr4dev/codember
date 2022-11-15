message = '11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101'

def decryptWord(word):
    asciiChar = ''
    asciiList = []
    for num in word:
        asciiChar += num
        if ( int(asciiChar) >= ord('a') and int(asciiChar) <= ord('z') ):
            asciiList.append(int(asciiChar))
            asciiChar = ''
    return ''.join(map(chr, asciiList))


def decryptMsg(msg):
    decrypted = ''
    for word in msg.split(' '):
        decrypted += ' '+decryptWord(word)
    
    return decrypted

def main():
    print(decryptMsg(message))

if __name__ == '__main__':
    main()