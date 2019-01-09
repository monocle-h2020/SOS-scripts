import requests




getCapabilitiesPayload = {
    "request": "GetCapabilities",
    "service": "SOS",
    "sections": [
        "ServiceIdentification",
        "ServiceProvider",
        "OperationsMetadata",
        "FilterCapabilities",
        "Contents"
    ]
}


describeSensorPayload = {
    "request": "DescribeSensor",
    "service": "SOS",
    "version": "2.0.0",
    "procedure": "",
    "procedureDescriptionFormat": "http://www.opengis.net/sensorml/2.0"
}


getDataAvailabilityPayload = {
    "request": "GetDataAvailability",
    "service": "SOS",
    "version": "2.0.0",
    "procedure": "",
    "observedProperty": ""
}


print getCapabilitiesPayload


def getCapabilities(server):
    print "sending request to %{}".format(server)
    print "with payload %{}".format(getCapabilitiesPayload)
    resp = requests.post(server, json=getCapabilitiesPayload)
    print resp.json()

def describeSensor(server, sensor):
    describeSensorPayload['procedure'] = sensor;
    print "sending request to %{}".format(server)
    print "with payload %{}".format(describeSensorPayload)
    resp = requests.post(server, json=describeSensorPayload)
    print resp.json()   




def getDataAvailability(server, sensor, observedProperty):
    getDataAvailabilityPayload['procedure'] = sensor
    getDataAvailabilityPayload['observedProperty'] = observedProperty
    print "sending request to %{}".format(server)
    print "with payload %{}".format(getDataAvailabilityPayload)
    resp = requests.post(server, json=getDataAvailabilityPayload)
    print resp.json()



if __name__ == '__main__':
    #getCapabilities('https://rsg.pml.ac.uk/sensorweb/service')
    #describeSensor('https://rsg.pml.ac.uk/sensorweb/service','Penlee')
    getDataAvailability('https://rsg.pml.ac.uk/sensorweb/service','Penlee','http://mmisw.org/ont/cf/parameter/air_pressure')
    