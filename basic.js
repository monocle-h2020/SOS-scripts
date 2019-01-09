const request = require('request')



const getCapabilitiesPayload = {
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


const describeSensorPayload = {
    "request": "DescribeSensor",
    "service": "SOS",
    "version": "2.0.0",
    "procedure": "",
    "procedureDescriptionFormat": "http://www.opengis.net/sensorml/2.0"
  }


const getDataAvailabilityPayload = {
    "request": "GetDataAvailability",
    "service": "SOS",
    "version": "2.0.0",
    "procedure": "",
    "observedProperty": ""
  }

const getCapabilities = (url) => {
    console.log(JSON.stringify(getCapabilitiesPayload));
    const getCapabilitiesOpts = {
        method : 'POST',
        url : url,
        body : getCapabilitiesPayload,
        json: true
    }
    request(getCapabilitiesOpts, function(err,resp,body){
        console.log(body);
    });
}


const describeSensor = (url,sensor) => {
    describeSensorPayload.procedure = sensor;
    console.log(JSON.stringify(describeSensorPayload));
    const describeSensorOpts = {
        method : 'POST',
        url : url,
        body : describeSensorPayload,
        json: true
    }
    request(describeSensorOpts, function(err,resp,body){
        console.log(body.procedureDescription.description);
    });
}



const getDataAvailability = (url,sensor, observedProperty) => {
    getDataAvailabilityPayload.procedure = sensor;
    getDataAvailabilityPayload.observedProperty = observedProperty;
    console.log(JSON.stringify(getDataAvailabilityPayload));
    const getDataAvailabilityOpts = {
        method : 'POST',
        url : url,
        body : getDataAvailabilityPayload,
        json: true
    }
    request(getDataAvailabilityOpts, function(err,resp,body){
        console.log(body.dataAvailability[0].phenomenonTime);
    });
}





//getCapabilities('https://rsg.pml.ac.uk/sensorweb/service')
describeSensor('https://rsg.pml.ac.uk/sensorweb/service','Penlee')
//getDataAvailability('https://rsg.pml.ac.uk/sensorweb/service','Penlee','http://mmisw.org/ont/cf/parameter/air_pressure');