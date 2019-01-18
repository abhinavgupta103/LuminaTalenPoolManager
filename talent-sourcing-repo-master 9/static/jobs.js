var dropdown_url = "/jobrole";
var default_url = "/jobs/Healthcare_Representative"
//Select the dropdown
var selector = document.getElementById('selDataset');
//Creating Dropdown
Plotly.d3.json(dropdown_url, function(error, response) {
    if (error) return console.warn(error);
    var data = [response];
    //Jobs contains a list of all job names in the data
    var jobs1 = data[0]["x"]
    var jobs = jobs1.sort();
    for(var i=0;i<jobs.length-1;i++) {
        //Create a dropdown option for each job name in the data, if it has a space, replace with underscore
        
        //Sample Code, You can edit anything in this for loop in order to create the drop down as long as the link
        //in the dropdown goes to /jobs/Laboratory_Technician if the job is "Laboratory Technician"
        var currentOption = document.createElement('option');
        currentOption.text = jobs[i];
        currentOption.value = "/jobs/"+jobs[i].replace(" ", "_");
        selector.appendChild(currentOption);
    }
})
Plotly.d3.json(default_url, function(error, response) {
    if (error) return console.warn(error);
    var data = [response];
    console.log(data)
    console.log(data[0][0])
    var layout1 = { margin: { t: 30, b:100 },
               title: "Gender by Job Role",
               xaxis: { title: "Gender"},
               yaxis: { title: "Number of Employees"}            
    }
    var layout2 = { margin: { t: 30, b:100 },
               title: "Age by Job Role",
               xaxis: { title: "Age Range"},
               yaxis: { title: "Number of Employees"}            
    }
    var layout3 = { margin: { t: 30, b:100 },
               title: "Department by Job Role",
               xaxis: { title: "Department"},
               yaxis: { title: "Number of Employees"}            
    }
    Plotly.newPlot("pie", [data[0][0]], layout1)
    Plotly.newPlot("bar", [data[0][1]], layout2)
    Plotly.newPlot("pie2", [data[0][2]], layout3)
})

function plotGraphs(graph_url) {
    Plotly.d3.json(graph_url, function(error, response) {
        if (error) return console.warn(error);
        var data = [response];
        console.log(data)
        console.log(response)

        var layout1 = { margin: { t: 30, b:100 },
                   title: "Gender by Job Role",
                   xaxis: { title: "Gender"},
                   yaxis: { title: "Number of Employees"}            
        }
        var layout2 = { margin: { t: 30, b:100 },
                   title: "Age by Job Role",
                   xaxis: { title: "Age Range"},
                   yaxis: { title: "Number of Employees"}            
        }
        var layout3 = { margin: { t: 30, b:100 },
                   title: "Department by Job Role",
                   xaxis: { title: "Department"},
                   yaxis: { title: "Number of Employees"}            
        }
        Plotly.newPlot("pie", [data[0][0]], layout1)
        Plotly.newPlot("bar", [data[0][1]], layout2)
        Plotly.newPlot("pie2", [data[0][2]], layout3)
    })
}