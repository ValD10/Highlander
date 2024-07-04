import brazilcep as bc
import time as tm
from geopy.geocoders import Nominatim

while 1==1:
    CEP = input("Digite aqui o CEP, apenas os números:     ")

    endereco = bc.get_address_from_cep(CEP)
    ad = endereco["street"].split("-")[0]+" "+endereco["city"]
    print(ad)

    geolocator = Nominatim(user_agent="test_app")
    location = geolocator.geocode(ad)

    lat = (location.latitude)
    lon = (location.longitude)
    print("Latitude:",lat,"Longitude",lon)

    tm.sleep(2)