
class Flight:
    def __int__(self, date, from, to, price):
        self.date = date
        self.from = from
        self.to = to
        self.price = price


def findLI(self, flights, hotelCost, budget):
        flightList = []
        for i in range(0, len(hotelCost) - 1):
            flightList.append([Flight])

        for flight in flights:
            flightList.get(flight[1] - 1).append(flight[0], flight[1], flight[2], flight[3])

        getIt(flightList, hotelCost, budget, 0, 1, 1, 10, [])

def getIt(self, flightList, hotelCost, budget, budgetUsed, src, dst, dateFrom, stops):
    if budgetUsed >= budget:
        return

    if dst == src and len(stops) > 0:
        print("budgetUsed", budgetUsed)
        print(stops.join(","))

    for flight in flightList.get(src - 1):
        stops.append(src)
        budgetUsed += flight.price
        if flight.date - dateFrom > 0:
            budgetUsed += hotelCost[flight.from - 1] * (flight.date - dateFrom)
            getIt(flightList, hotelCost, budget, budgetUsed, flight.to, dst, flight.date, stops)
            budgetUsed -= flight.price
            if flight.date - dateFrom > 0:
                budgetUsed += hotelCost[flight.from - 1] * (flight.date - dateFrom) * -1
            stops.pop(len(stops) - 1)