def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1,number+1):
        print("{} {} {} {}".format((str(i).rjust(width)), (str(oct(i)[2:]).rjust(width)), (str(hex(i)[2:]).upper().rjust(width)), (str(bin(i)[2:]).rjust(width))))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
