def digital_root(number):
    number = str(number)
    output = 0
    for i in range(0, len(number)):
        output += int(number[i])
    return output

if __name__ == '__main__':
    a = 2**1000
    print(digital_root(a))