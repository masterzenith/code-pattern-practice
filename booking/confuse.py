from collections import defaultdict

hotels = [("hotel_1234", "Sheraton", "Amsterdam"), ("hotel_1000", "Sheraton", "Buenos Aires"),
          ("hotel_1001", "Hilton", "Amsterdam"), ("hotel_1002", "Royal Palace", "Bogota"),
          ("hotel_1003", "Sheraton", "Amsterdam"), ("hotel_1004", "Sheraton", "Buenos Aires"),
          ("hotel_1005", "Sheraton", "Buenos Aires"), ("hotel_1234", "Sheraton", "Amsterdam")]


def confuse():
    d = defaultdict(int)
    for hotel in hotels:
        d[(hotel[1], hotel[2])] += 1

    for k, v in d.items():
        if v >= 3:
            print(k)


print(confuse())
