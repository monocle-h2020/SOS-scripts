# Authentication Design

## ideas

* a simple node application, should suffice
* a small secured database of allowed sensor developers
* pobably sqlite3 for initial testing
* generate a token and store for checking against later
* will need a proxy infront of the SOS insert methods to act as auth layer

## API (draft)

* /get_token/<sensor_name>
* /revoke_token/<sensor_name|token>


## Flow

1. Sensor dev is issued with credentials to identify themselves
    * username
    * password
2. sensor dev provides very basic sensor information 
    * sensor name
    * sensor type (maybe)
3. call to `/get_token`
    * send credentials and sensor name
    * store sensor name/sensor_company/timestamp as a unique string
    * generate a token and associate with that sensor in DB
    * return token to user
4. device can then issue requests to the SOS using the token as auth and ID