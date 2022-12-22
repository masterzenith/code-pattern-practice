import json

data = {
    "field1": {
        "a": 10,
        "b": 20,
    },
    "field2": {
        "c": 30,
        "d": 40,
    },
}


def generate_csv():
    with open('data.txt', 'w') as out_file:
        json.dump(data, out_file, sort_keys=True, indent=4, ensure_ascii=False)
