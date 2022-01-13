#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"

def main():
    resp= requests.get(URL).json()
    
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    epochtime = datetime.datetime.fromtimestamp(resp["timestamp"])
    ts = epochtime.strftime('%Y-%m-%d %H:%M:%S')
    locator_resp = rg.search((lat, lon))	
    city = locator_resp[0]["name"]
    cc = locator_resp[0]["cc"]
    print("CURRENT LOCATION OF THE ISS:")
    print("Timestamp: " + ts)
    print("Lon: " + lon)
    print("Lat: " + lat)
    print(f"City/Country: {city}, {cc}")

if __name__ == "__main__":
    main()
