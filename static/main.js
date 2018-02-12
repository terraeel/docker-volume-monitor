function drawChart() {

    var url = 'http://localhost:5000/api/volumes';
    $.getJSON(url, function(volumes) {
        dataTable = new google.visualization.DataTable();

        var newData = [['Id','Time','Name','Size']];
        dataTable.addColumn('string', newData[0][2]);
        dataTable.addColumn('number', newData[0][3]);

        $.each( volumes, function( index, element ) {
            dataTable.addRow([element[2],element[3]]);
        });

        var options = {
            title: 'Volumes Size',
            sliceVisibilityThreshold:0,
            backgroundColor: { fill: "#263238" },
            legendTextStyle: { color: '#FFF' },
            titleTextStyle: { color: '#FFF' },
            hAxis: {
                color: '#FFF',
            }
        };

        chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(dataTable, options);
    });
}