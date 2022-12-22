from typing import Set

dataset = {

    176: [
        {
            "price": 120,
            "features": ["breakfast", "refundable"],
            "availbility": 5
        }
    ],
    177: [
        {
            "price": 130,
            "features": ["breakfast"],
            "availbility": 1
        },
        {
            "price": 140,
            "features": ["breakfast", "refundable", "wifi"],
            "availbility": 3
        }
    ],
    178: [
        {
            "price": 130,
            "features": ["breakfast"],
            "availbility": 2
        },
        {
            "price": 140,
            "features": ["breakfast", "refundable", "wifi"],
            "availbility": 10
        }
    ]
}

input = {
    "checkin": 176,
    "checkout": 178,
    "features": ["breakfast"],
    "rooms": 1

}
output = [
    {
        "price": 250,
        "features": ["breakfast"],
        "availbility": 1
    },
    {
        "price": 260,
        "features": ["breakfast", "refundable"],
        "availbility": 3
    }
]


def get_rooms(input, dataset):
    checkin: int = input.get('checkin')
    checkout: int = input.get('checkout')
    given_features: Set[str] = set(input.get('features'))
    first_day_rooms = dataset.get(checkin)
    result = []

    for room in first_day_rooms:
        if is_suitable(given_features, room):
            get_next_room(dataset, checkin, checkout, 0, room.get('availbility'), given_features,
                          set(room.get('features')), result)

    return result


def get_next_room(dataset, checkin, checkout, curr_price, availbility, given_features, common_features, result):
    if checkin == checkout:
        result.append({
            'price': curr_price,
            'features': list(common_features),
            'availbility': availbility
        })
        return

    next_day_rooms = dataset.get(checkin)
    for room in next_day_rooms:
        if is_suitable(given_features, room):
            curr_price += room.get('price')
            new_common_features = get_common_features(common_features, room.get('features'))
            new_availbility = min(availbility, room.get('availbility'))
            get_next_room(dataset, checkin + 1, checkout, curr_price, new_availbility, given_features,
                          new_common_features, result)
            curr_price -= room.get('price')


def is_suitable(features, room) -> bool:
    if room.get('availbility') < 1: return False
    count = 0
    room_features = room.get('features')
    for feature in room_features:
        if feature in features:
            count += 1
    return count == len(features)


def get_common_features(prev_room_features, curr_room_features) -> Set[str]:
    return list(set(prev_room_features) & set(curr_room_features))


print(get_rooms(input, dataset))