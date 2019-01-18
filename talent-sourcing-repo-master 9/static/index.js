var gender_url = "/gender";
var jobroles_url = "/jobrole";
var depts_url = "/department";
var satisfaction_url = "/satisfaction";
var tableData_url = "/table"

Plotly.d3.json(tableData_url, function(error, response) {
    if (error) return console.warn(error);
    var data = [response];
    console.log(response)
    var layout = { margin: { t: 30, b:100 },
                   title: "Gender Statistics",
                   xaxis: { title: "Gender"},
                   yaxis: { title: "Number of Employees"}            
    }
    Plotly.plot("pie", data, layout)
})


Plotly.d3.json(gender_url, function(error, response) {
    if (error) return console.warn(error);
    var data = [response];
    console.log(response)
    var layout = { margin: { t: 30, b:100 },
                   title: "Gender Statistics",
                   xaxis: { title: "Gender"},
                   yaxis: { title: "Number of Employees"}            
    }
    Plotly.plot("pie", data, layout)
})
Plotly.d3.json(jobroles_url, function(error, response) {
    if (error) return console.warn(error);
    var data = [response];
    console.log(response)
    var layout = { margin: { t: 30, b:100 },
                   title: "Job Role Statistics",
                   xaxis: { title: "Job Role"},
                   yaxis: { title: "Number of Employees"}            
    }
    Plotly.plot("bar", data, layout)
})
Plotly.d3.json(depts_url, function(error, response) {
    if (error) return console.warn(error);
    var data = [response];
    console.log(response)
    var layout = { margin: { t: 30, b:100 },
                   title: "Department Statistics",
                   xaxis: { title: "Department"},
                   yaxis: { title: "Number of Employees"}            
    }
    Plotly.plot("bar2", data, layout)
})
Plotly.d3.json(satisfaction_url, function(error, response) {
    if (error) return console.warn(error);
    var data = [response];
    console.log(response)
    var layout = { margin: { t: 30, b:100 },
                   title: "Department Satisfaction",
                   xaxis: { title: "Department"},
                   yaxis: { title: "Average Satisfaction"}            
    }
    Plotly.plot("bar3", data, layout)
})

