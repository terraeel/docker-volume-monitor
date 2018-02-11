function drawChart() {

    var url = 'http://localhost:5000/api/volumes';
    $.getJSON(url, { get_param: 'value' }, function(volumes) {
        dataTable = new google.visualization.DataTable();

        var newData = [['Id','Time','Name','Size']];
        dataTable.addColumn('string', newData[0][2]);
        dataTable.addColumn('number', newData[0][3]);

        $.each( volumes, function( index, element ) {
            dataTable.addRow([element[2],element[3]]);
        });

        var options = {
            title: 'Volumes Size',
            hAxis: {title: 'Id', titleTextStyle: {color: 'red'}},
            sliceVisibilityThreshold:0
        };

        chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(dataTable, options);
    });
}