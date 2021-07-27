function tabler2() {

    var url = 'http://0.0.0.0:3010/master_table?select=cog_fk(test_id,test_seq_name,test_strain,test_s_year,test_strain_seq),patient_fk(patient_id)'

    var table = new Tabulator("#tableLoc2", {
        ajaxURL: url,
        pagination: 'local',
        paginationSize: 16,
        movableColumns: true,
        virtualDomHoz:true,
        initialSort:[
            {
                column:"cog_fk.test_id",
                dir:"asc"
            }
        ],
        columns: [
            {
                title: "Test PK",
                field: "cog_fk.test_id",
                headerFilter: "input"
            },
            {
                title: "Patient ID",
                field: "patient_fk.patient_id",
                headerFilter: "input"
            },
            {
                title: "Test Sequence",
                field: "cog_fk.test_strain_seq",
                headerFilter: "input",
                formatter: "plaintext"
            },
            ]
    });
            //trigger download of data.csv file
    document.getElementById("download-csv").addEventListener("click", function(){
        table.download("csv", "data.csv");
    });

    //trigger download of data.json file
    document.getElementById("download-json").addEventListener("click", function(){
        table.download("json", "data.json");
    });
}