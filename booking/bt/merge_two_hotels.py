def solve(hotels):
    hotels.sort()
    map = {}
    stack = []
    for hotel in hotels:
        start = hotel[0]
        end = hotel[1]

        if start - 1 in map:
            interval = map.get(start - 1).pop()
            if not map.get(start - 1):
                map.pop(start - 1)
            if end not in map:
                stack.append((interval[0], end))
        else:
            if hotel not in map:
                stack.append(hotel)

    al = []
    for key in map.keys():
        st = map.get(key, 0)
        while st:
            al.append(st.pop())
    return al 