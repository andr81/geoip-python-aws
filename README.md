# Serverless python GeoIp

AWS Lambda and MaxMind GeoLite to find a location of IP addresses.

## Install
- git clone git@github.com:andr81/geoip-python-aws.git
- cd serverless-geoip
- sls plugin install -n serverless-python-requirements
- sls deploy

## Database
Download the GeoLite2 database and put to the src folder  
http://dev.maxmind.com/geoip/geoip2/geolite2/

## Usage
```
curl https://yoururl.execute-api.us-east-1.amazonaws.com/prod/geoip?ip=7.7.7.7
```
```
{"continentCode": "NA", "countryCode": "US"}
```