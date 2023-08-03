#This code spits out a correct path, but the method for finding the answer is flawed.


def crawl(pyramid):
    return rec_crawl(0, 0, pyramid)

def rec_crawl(height, width, pyramid):
    if height == len(pyramid) - 1:
        return pyramid[height][width], [pyramid[height][width]]

    left_sum, left_path = rec_crawl(height + 1, width, pyramid)
    right_sum, right_path = rec_crawl(height + 1, width + 1, pyramid)

    if left_sum >= right_sum:
        return pyramid[height][width] + left_sum, [pyramid[height][width]] + left_path
    else:
        return pyramid[height][width] + right_sum, [pyramid[height][width]] + right_path

if __name__ == '__main__':
    pyramid = []
    while True:
        g = input()
        if g == 'end':
            break
        numbers = g.split()
        numbers = [int(num) for num in numbers]
        pyramid.append(numbers)
    a_number = 0
    max_sum, path = crawl(pyramid)
    print(path)
    for i in path:
        a_number = a_number + i
    print(a_number)