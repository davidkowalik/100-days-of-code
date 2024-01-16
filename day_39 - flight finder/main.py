from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from notification_manager import NotificationManager
import datetime


DATE_FROM = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
DATE_TO = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
DEPARTURE_AIRPORTS= [["KRK", "Kraków"], ["KTW", "Katowice"]]

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

google_data = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
send_mail = False

sheet_data = google_data.get_sheet_data()



# update IATA code in a sheet -------------------------------------------
empty_iata_code = False

for item in sheet_data['prices']:
    print(item)
    if item['iataCode'] == "":
        item['iataCode'] = flight_search.search_airtport(city = item['city'])['locations'][0]['code']
        empty_iata_code = True

if empty_iata_code:
    google_data.update_sheet(sheet_data=sheet_data)
#------------------------------------------------------------------------

print(notification_manager.message)

for departure_code in DEPARTURE_AIRPORTS:
    notification_manager.message += f"Loty z {departure_code[1]} [{departure_code[0]}]"
    notification_manager.html_message += "<p>"
    notification_manager.html_message += f"Loty z {departure_code[1]} [{departure_code[0]}]:<br><br>" 
    for destination in sheet_data['prices']:
        flight = flight_search.search_flights(destination_city_code=destination['iataCode'], origin_city_code=departure_code[0], from_time=DATE_FROM, to_time=DATE_TO)
        if flight != None and flight.price < destination['lowestPrice']:
            notification_manager.message += f'{flight.price}PLN, lot: {flight.departure_city_name} [{flight.departure_airport_code}] ({flight.countryFrom}) -> {flight.arrival_city_name} [{flight.arrival_airport_code}] ({flight.countryTo}) w dniach: [{flight.outbound_date} - {flight.inbound_date}]. Sprzawdz: <a href="{flight.flight_url}">URL</a>\n\n'
            notification_manager.html_message += f'{flight.price}PLN, lot: {flight.departure_city_name} [{flight.departure_airport_code}] ({flight.countryFrom}) -> {flight.arrival_city_name} [{flight.arrival_airport_code}] ({flight.countryTo}) w dniach: [{flight.outbound_date} - {flight.inbound_date}]. Sprzawdz: <a href="{flight.flight_url}">URL</a><br>'
            print(notification_manager.message)
            send_mail = True
    notification_manager.html_message += "</p><hr>"

if send_mail:
    # notification_manager.send_message()
    notification_manager.send_html_message()

