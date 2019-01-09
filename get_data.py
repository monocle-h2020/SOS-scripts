from datetime import datetime

import requests
import matplotlib.pyplot as plt

getObservationPayload = {
    "request": "GetObservation",
    "service": "SOS",
    "version": "2.0.0",
    "procedure": "Penlee",
    "offering": "PenleeMetData",
    "observedProperty": "http://mmisw.org/ont/cf/parameter/air_temperature",
    "temporalFilter": {
        "during": {
            "ref": "om:phenomenonTime",
            "value": [
                "2015-01-02T13:50:00.000Z",
                "2016-01-02T13:50:00.000Z"
            ]
        }
    }
}

getDummyObservationPayload = {
  "request": "GetObservation",
  "service": "SOS",
  "version": "2.0.0",
  "procedure": "http://www.52north.org/test/procedure/9",
  "offering": "http://www.52north.org/test/offering/9",
  "observedProperty": "http://www.52north.org/test/observableProperty/9_3",
  "featureOfInterest": "http://www.52north.org/test/featureOfInterest/9"
}


def getObservation(server):
    resp = requests.post(server, json=getObservationPayload)
    #plotData(resp.json())
    print resp.json()

def plotData(data):
    times = []
    values = []
    locations = []

    for item in data['observations']:
        print "adding result"
        print times
        times.append(datetime.strptime(item['phenomenonTime'], "%Y-%m-%dT%H:%M:%S.%fZ"))
        values.append(item['result']['value'])
        locations.append(item['featureOfInterest']['geometry']['coordinates'])
    
    #print times
    #print values
    #plt.plot(times,values)
    #plt.show()




if __name__ == "__main__":
    getObservation('https://rsg.pml.ac.uk/sensorweb/service')