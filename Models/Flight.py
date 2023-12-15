class Flight:
    def __init__(self, startingPoint='', departureTime='', arrivalTime='', destination='', id=0, flightNumber=''):
        """
        Constructor for Flight
        """
        self.startingPoint = startingPoint
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.destination = destination
        self.id = id
        self.flightNumber = flightNumber