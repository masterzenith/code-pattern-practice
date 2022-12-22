from collections import Counter


def output_most_popular_destination(count):
    myList = list()
    i = count

    while i > 0:
        tmpData = input()
        myList.append(tmpData)
        i = i - 1

    c = Counter(myList)
    print("Most Popular Destination: ", c.most_common(1)[0][0])


count = int(input())
output_most_popular_destination(count)

