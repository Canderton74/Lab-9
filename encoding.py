def encoder(num):
    string = str(num)
    str_blank = ''
    for i in string:
        i = str((int(i)+3)%10)
        str_blank+=i

    return str_blank

def decoder(num):
    string = str(num)
    str_blank = ''
    for i in string:
        i = str((int(i)-3)%10)
        str_blank+=i

    return str_blank

def main():
    password = None
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit
              """)
        choice = input('Please enter an option: ')
        if choice == '1':
            password = encoder(input('Please enter your password to encode: '))
            print("Your password has been encoded and stored!")
        if choice == '2':
            print(f'The encoded password is {password}, and the original password is {decoder(password)}.')
        if choice == '3':
            break
if __name__ == "__main__":
    main()