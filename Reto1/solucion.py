def main():
    with open('users.txt') as f:
        users = f.readlines()
    print(users)

if __name__ == '__main__':
    main()