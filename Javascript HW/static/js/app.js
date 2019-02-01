// from data.js
var tableData = data;

// YOUR CODE HERE!

var tbody = d3.select("tbody");

function buildTable(data) {

  tbody.html('');

  data.forEach((ufoSighting) => {
    var row = tbody.append("tr");
    Object.values(ufoSighting).forEach(value => {
      var cell = row.append("td");
      cell.text(value);
    });
  });

}

buildTable(tableData);



var button = d3.select("#filter-btn")

button.on('click', handleClick);

function handleClick() {

  d3.event.preventDefault();

  var date = d3.select("#datetime").property('value');
  var city = d3.select("#city").property('value');
  

  console.log(date);

  var filteredDate = tableData;
  if (date || city) {

    filteredDate = filteredDate.filter(row => row.datetime === date);
    filteredDate = filteredDate.filter(row => row.city === city);

    console.log(filteredDate);

  }

  buildTable(filteredDate);

};



 
