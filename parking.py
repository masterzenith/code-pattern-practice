class Parking:
    def __init__(self):
        self.slots = {
            'small': 1,
            'medium': 1,
            'large': 2
        }
        self.count = 1
        self.ticket = {}

    def parking(self, type, size):
        if type == 'arrival':
            if self.slots[size] <= 0:
                return "reject"
            else:
                self.slots[size] -= 1
                self.ticket[self.count] = size
                self.count += 1
        else:
            size = self.ticket[size]
            self.slots[size] += 1


park = Parking()
print(park.parking(1, 1))
