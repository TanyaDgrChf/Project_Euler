def crawl_grid(down, right, length):
    coords = []
    for i in range(1, length + 1):
        down_coords = []
        for j in range(1, length + 1):
            down_coords.append(None)
        coords.append(down_coords)
    return crawl_grid_rec(down, right, length, coords)

def crawl_grid_rec(down, right, length, coords):
    if down >= length:
        return 1
    if right >= length:
        return 1
    if coords[down][right] != None:
        return coords[down][right]
    else:
        num = crawl_grid_rec(down + 1, right, length, coords) + crawl_grid_rec(down, right + 1, length, coords)
        coords[down][right] = num
        return num

if __name__ == '__main__':
    print(crawl_grid(0, 0, 20))


        