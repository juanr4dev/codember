from collections import defaultdict

def main():
    word_count = defaultdict(int)
    with open('message_01.txt','r') as file:
        for line in file:
            for word in line.split():
                word_count[word] += 1
    [print(f'{key}{word_count[key]}',end='') for key in word_count]

if __name__ == '__main__':
    main()
