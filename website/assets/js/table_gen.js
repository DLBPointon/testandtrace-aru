var headerMenu = function(){
    var menu = [];
    var columns = this.getColumns();

    for(let column of columns){

        //create checkbox element using font awesome icons
        let icon = document.createElement("i");
        icon.classList.add("fas");
        icon.classList.add(column.isVisible() ? "fa-check-square" : "fa-square");

        //build label
        let label = document.createElement("span");
        let title = document.createElement("span");

        title.textContent = " " + column.getDefinition().title;

        label.appendChild(icon);
        label.appendChild(title);

        //create menu item
        menu.push({
            label:label,
            action:function(e){
                //prevent menu closing
                e.stopPropagation();

                //toggle current column visibility
                column.toggle();

                //change menu item icon
                if(column.isVisible()){
                    icon.classList.remove("fa-square");
                    icon.classList.add("fa-check-square");
                }else{
                    icon.classList.remove("fa-check-square");
                    icon.classList.add("fa-square");
                }
            }
        });
    }

   return menu;
};

function tabler() {

    var url = 'http://0.0.0.0:3010/master_table?select=cog_fk(test_id,test_seq_name,test_strain,test_s_year,test_strain_seq),master_result,master_dayoftest,pcr_main_fk(pcr_name,pcr_order_no,pcr_cost,manu_fk(manu_id,manu_name),supplier_fk(supplier_pk,supplier,supplier_add,supplier_postcode,supplier_country),buffer_fk(buffer_id,buffer_name,buffer_conc),enz_fk(enz_id,enz_name,enz_conc),nucleo_fk(nucleo_id,nucleo_conc,nucleo_mix)),denature_fk(denature_temp,denature_time),annealing_fk(annealing_temp,%20annealing_time),elongate_fk(elongate_temp,elongate_time),master_cycle_count,completion_fk(completion_temp,completion_time),pcr_fk(ref_id,seq_f_fk(seq_id,seq_header,seq_sequence),seq_r_fk(seq_header,seq_sequence)),master_amp_seq,master_purpose,master_primer_conc,master_primer_supplier,master_cost,patient_fk(patient_id,patient_fname,patient_lname,patient_title,patient_phone,patient_email,patient_postcode),scientist_fk(scientist_id,scientist_name,scientist_title,scientist_centre,scientist_phone,scientist_email)'

    var table = new Tabulator("#tableLoc", {
        ajaxURL: url,
        pagination: 'local',
        paginationSize: 16,
        movableColumns: true,
        virtualDomHoz:true,
        groupBy: "master_result",
        columnHeaderVertAlign:"bottom",
        initialSort:[
            {
                column:"cog_fk.test_id",
                dir:"asc"
            }
        ],
        columns: [
            {
                title: "Test Result",
                field: "master_result",
                headerFilter: "input",
                headerMenu:headerMenu
            },
            {
                title: "Scientist ID",
                field: "scientist_fk.scientist_id",
                headerFilter: "input",
                headerMenu:headerMenu
            },
            {
                title: "Patient PK",
                field: "patient_fk.patient_id",
                headerFilter: "input",
                headerMenu:headerMenu
            },
            {
                Title: "COG Data",
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Test PK",
                        field: "cog_fk.test_id",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Tested Strain ID",
                        field: "cog_fk.test_seq_name",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Tested Strain",
                        field: "cog_fk.test_strain",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Test Strain Year ID",
                        field: "cog_fk.test_s_year",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                ]
            },
            {
                Title: "PCR Kit Data",
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "PCR Kit Name",
                        field: "pcr_main_fk.pcr_name",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Order No.",
                        field: "pcr_main_fk.pcr_order_no",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Manufacturer",
                        field: "pcr_main_fk.manu_fk.manu_name",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Supplier",
                        field: "pcr_main_fk.supplier_fk.supplier",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Supplier Address",
                        field: "pcr_main_fk.supplier_fk.supplier_add",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Supplier Postcode",
                        field: "pcr_main_fk.supplier_fk.supplier_postcode",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Supplier Country",
                        field: "pcr_main_fk.supplier_fk.supplier_country",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Buffer",
                        field: "pcr_main_fk.buffer_fk.buffer_name",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Buffer Conc",
                        field: "pcr_main_fk.buffer_fk.buffer_conc",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Enzyme",
                        field: "pcr_main_fk.enz_fk.enz_name",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Enzyme Conc",
                        field: "pcr_main_fk.enz_fk.enz_conc",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Nucleotide Mix",
                        field: "pcr_main_fk.nucleo_fk.nucleo_mix",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Nucleotide Conc",
                        field: "pcr_main_fk.nucleo_fk.nucleo_conc",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                ]
            },
            {
                Title: "Patient Data",
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Patient First Name",
                        field: "patient_fk.patient_fname",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Patient Last Name",
                        field: "patient_fk.patient_lname",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Patient Title",
                        field: "patient_fk.patient_title",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Patient Phone No.",
                        field: "patient_fk.patient_phone",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Patient Email",
                        field: "patient_fk.patient_email",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Patient Postcode",
                        field: "patient_fk.patient_postcode",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                ]
            },
            {
                Title: "Scientist Data",
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Scientist Name",
                        field: "scientist_fk.scientist_name",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Scientist Title",
                        field: "scientist_fk.scientist_title",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Scientist Centre",
                        field: "scientist_fk.scientist_centre",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Scientist Phone No.",
                        field: "scientist_fk.scientist_phone",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Scientist Email",
                        field: "scientist_fk.scientist_email",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                ]
            },
            {
                Title: "Main Data",
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Date of Test",
                        field: "master_dayoftest",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Time of Test",
                        field: "master_timeoftest",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "PCR Cycle Count",
                        field: "master_cycle_count",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Sequence for Amplification",
                        field: "master_amp_seq",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Purpose of Test",
                        field: "master_purpose",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Date of Test",
                        field: "master_dayoftest",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Cost of Test",
                        field: "master_cost",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                ]
            },
            {
                Title: 'Elongation Data',
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Elongation Temperature",
                        field: "elongate_fk.elongate_temp",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Elongation Time",
                        field: "elongate_fk.elongate_time",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    }
                ]
            },
            {
                Title: 'Denature Data',
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Denature Temperature",
                        field: "denature_fk.denature_temp",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Denature Time",
                        field: "denature_fk.denature_time",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    }
                ]
            },
            {
                Title: 'Annealing Data',
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Annealing Temperature",
                        field: "annealing_fk.annealing_temp",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Annealing Time",
                        field: "annealing_fk.annealing_time",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    }
                ]
            },
            {
                Title: 'Completion Data',
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Completion Temperature",
                        field: "completion_fk.completion_temp",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Completion Time",
                        field: "completion_fk.completion_time",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    }
                ]
            },
            {
                Title: "PCR Primer Data",
                headerHozAlign:"center",
                headerMenu:headerMenu,
                columns: [
                    {
                        title: "Primer Name 'F'",
                        field: "pcr_fk.seq_f_fk.seq_header",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Primer Seq 'F'",
                        field: "pcr_fk.seq_f_fk.seq_sequence",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Primer Name 'R'",
                        field: "pcr_fk.seq_r_fk.seq_header",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                    {
                        title: "Primer Seq 'R'",
                        field: "pcr_fk.seq_r_fk.seq_sequence",
                        headerFilter: "input",
                        headerMenu:headerMenu
                    },
                ]
            }
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

