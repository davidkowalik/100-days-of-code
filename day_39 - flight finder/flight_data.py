class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_city_name, countryTo, countryFrom, departure_airport_code, arrival_city_name, arrival_airport_code, outbound_date, inbound_date, flight_url):
        self.price = price
        self.departure_city_name = departure_city_name
        self.countryTo = countryTo
        self.countryFrom = countryFrom
        self.departure_airport_code = departure_airport_code
        self.arrival_city_name = arrival_city_name
        self.arrival_airport_code = arrival_airport_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.flight_url = flight_url
