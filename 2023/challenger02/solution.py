
def main():
    with open('message_02.txt','r') as f:
        message = f.readline()
    calculated = 0
    output = []
    for char in message:
        match char:
            case '#': calculated+=1
            case '@': calculated-=1
            case '*': calculated=calculated**2
            case '&': output.append(calculated)
    print(''.join(str(i) for i in output))
if __name__ == '__main__':
    main()