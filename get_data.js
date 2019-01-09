const request = require('request')
const fs = require('fs');

const PLOTLY_KEY = "d2r90DUO7klS4cjjrhuv";
const PLOTLY_USERNAME = 'doclements';

const plotly = require('plotly')(PLOTLY_USERNAME,PLOTLY_KEY)

const getObservationPayload = {
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


const processOutput = (output) => {
    const obs = output.observations;
    data = []
    obs.forEach(datum => {
        data.push({
            date : datum.phenomenonTime,
            value : datum.result.value
        })
        //console.log(datum.phenomenonTime)
        //console.log(datum.result.value)
    });
    return data
}

const plotData = (data) => {
    //console.log(data);
    const x = [];
    const y = [];
    data.forEach(element => {
        x.push(element.date);
        y.push(element.value);
    });
    const plot_data = {
        x : x,
        y : y, 
        type : "scatter"
    };

    //var graphOptions = {filename: "test_sos_plot", fileopt: "overwrite"};
    var imgOpts = {
        format : "png",
        height: 2500,
        width : 5000,
        title: "test title"
    }

    var layout = {
        title : "A Plot Test from SOS",
        xaxis: {
            title : "Observation Date"
        },
        yaxis : {
            title : "Air Temp"
        }
    }

    const figure  = { 'data' : [plot_data], layout:layout}
    plotly.getImage(figure, imgOpts, function(error,imageStream){
        if (error) return console.log (error);

        var fileStream = fs.createWriteStream('test_plot.png');
        imageStream.pipe(fileStream);    
    });
}

const getObservation = (url) => {

    //console.log(JSON.stringify(getObservationPayload));
    const getObservationOpts = {
        method : 'POST',
        url : url,
        body : getObservationPayload,
        json: true
    }
    request(getObservationOpts, function(err,resp,body){
        //console.log(body);
        plotData(processOutput(body));
    });
}


getObservation('https://rsg.pml.ac.uk/sensorweb/service')

