from collections import Counter
file = open("day5_data.txt").read().replace(" -> ", ",").strip().split("\n")

def horizontal(x,y1,y2):
    x = int(x)
    y1 = int(y1)
    y2 = int(y2)
    diff = abs(y2 - y1) + 1
    smallest = min(y1,y2)
    for a in range(0,diff):
        across.append((x,smallest))
        smallest = smallest + 1
    return across

def vertical(x1,x2,y):
    x1,x2,y = int(x1),int(x2),int(y)
    diff = abs(x1-x2) + 1
    smallest = min(x1,x2)
    for a in range(0,diff):
        down.append((smallest, y))
        smallest = smallest +1
    return down

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def slope(x1,y1,x2,y2):
    #x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
    #diff = abs(x1-x2) + 1
    #print(x1,y1,x2,y2)
    m = 0
    n = 0
    #diff2 = abs(y1 - y2) + 1
    for a in range(0,difx + 1):
        if x1 <= x2:
            newx = x1 + m
        else:
            newx = x1 - m
        m = m + 1
        if y1 <= y2:
            newy = y1 + n
        else:
            newy = y1 - n
        n = n+1
        diagonal.append((newx,newy))
    #print(diagonal)
    return diagonal


across = []
down = []
diagonal = []
combined_set = ()
#look for when the x is the same for both
for str in file:
    str = str.split(",")
    x1 = str[0]
    y1 = str[1]
    x2 = str[2]
    y2 = str[3]
    x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
    difx = abs(x1 - x2)
    dify = abs(y1 - y2)
# for when x is the same for both
    if x1 == x2:
        horizontal(x1,y1,y2)
# for when y is the same for both
    if y1 == y2:
        vertical(x1,x2,y1)
# for diagonals that are at 45 degrees - length x1 -> x2 = y1 -> y2
    if difx == dify:
        slope(x1,y1,x2,y2)
# find the duplicates within each of the three lists
across_duplicates = [ele for ele, count in Counter(across).items()
                                          if count > 1]
down_duplicates = [ele for ele, count in Counter(down).items() if count > 1]
diagonal_duplicates = [ele for ele, count in Counter(diagonal).items()
                                          if count > 1]
#find intersections of the three lists with each other
across_down_intersection = intersection(across, down)
across_diagonal_intersection = intersection(across, diagonal)
down_diagonal_intersection = intersection(down, diagonal)
#combine the six lists
combined_list = across_duplicates + down_duplicates + diagonal_duplicates + across_down_intersection + across_diagonal_intersection+ down_diagonal_intersection

# use set to find the number of unique values in the list
combined_set = set(combined_list)
number_of_unique_values = len(combined_set)
print(number_of_unique_values)