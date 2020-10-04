import json
import geoip2.database
from geoip2.models import City

db = None

def get_db():
    global db
    if db is None:
        db = geoip2.database.Reader('src/GeoLite2-City.mmdb')
    return db


def get_geo(ip: str):
    geo = get_db().city(ip)

    return {
        "continentCode": geo.continent.code,
        "countryCode": geo.country.iso_code
    }


def geoip(event, context):
    if event.get("queryStringParameters", None) is None or "ip" not in event["queryStringParameters"]:
        return {
            "statusCode": 400,
            "body": json.dumps({"msg": "parameter 'ip' is needed"})
        }
    ip = event["queryStringParameters"]["ip"]
    geo = get_geo(ip)
    return {
        "statusCode": 200,
        "body": json.dumps(geo)
    }


if __name__ == "__main__":
    print(get_geo("7.7.7.7"))