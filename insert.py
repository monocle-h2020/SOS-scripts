import json
import requests


insertSensorPayload = {
  "request": "InsertSensor",
  "service": "SOS",
  "version": "2.0.0",
  "procedureDescriptionFormat": "http://www.opengis.net/sensorml/2.0",
  "procedureDescription": "<<sensorML_holder>>",
  "observableProperty": [
    "http://www.52north.org/test/observableProperty/9_1",
    "http://www.52north.org/test/observableProperty/9_2",
    "http://www.52north.org/test/observableProperty/9_3",
    "http://www.52north.org/test/observableProperty/9_4",
    "http://www.52north.org/test/observableProperty/9_5",
    "http://www.52north.org/test/observableProperty/9_6"
  ],
  "observationType": [
    "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
    "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CategoryObservation",
    "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_CountObservation",
    "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_TextObservation",
    "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_TruthObservation",
    "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_GeometryObservation"
  ],
  "featureOfInterestType": "http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint"
}

insertObservationPayload = {
  "request": "InsertObservation",
  "service": "SOS",
  "version": "2.0.0",
  "offering": "http://www.52north.org/test/offering/9",
  "observation": {
    "identifier": {
      "value": "http://www.52north.org/test/observation/9",
      "codespace": "http://www.opengis.net/def/nil/OGC/0/unknown"
    },
    "type": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
    "procedure": "http://www.52north.org/test/procedure/9",
    "observedProperty": "http://www.52north.org/test/observableProperty/9_3",
    "featureOfInterest": {
      "identifier": {
        "value": "http://www.52north.org/test/featureOfInterest/9",
        "codespace": "http://www.opengis.net/def/nil/OGC/0/unknown"
      },
      "name": [
        {
          "value": "52North",
          "codespace": "http://www.opengis.net/def/nil/OGC/0/unknown"
        }
      ],
      "sampledFeature": [
        "http://www.52north.org/test/featureOfInterest/world"
      ],
      "geometry": {
        "type": "Point",
        "coordinates": [
          51.935101100104916,
          7.651968812254194
        ],
        "crs": {
          "type": "name",
          "properties": {
            "name": "EPSG:4326"
          }
        }
      }
    },
    "phenomenonTime": "2012-11-19T17:45:15+00:00",
    "resultTime": "2012-11-19T17:45:15+00:00",
    "result": {
      "uom": "test_unit_9_3",
      "value": 0.28
    }
  }
}




def insertSensor(server):
    sensorML_file_string = open("example_sensor_SML2_0.xml", "r").read()
    
    insertSensorPayload['procedureDescription'] = sensorML_file_string
    resp = requests.post(server, json=insertSensorPayload)
    print  resp.json()


def insertObservation(server):
    resp = requests.post(server, json=insertObservationPayload)
    print resp.json()


if __name__ == '__main__':
    #insertSensor('https://rsg.pml.ac.uk/sensorweb/service')
    insertObservation('https://rsg.pml.ac.uk/sensorweb/service')
    