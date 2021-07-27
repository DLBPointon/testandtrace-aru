## Test and Trace Database - Assignment 

This is a full stack development built for an assignment for my 
Degree Apprenticeship @ ARU in conjunction with the Sanger Institute.

## Current Command
Once running the full data table can be received by entering this into the browser:

"""

http://0.0.0.0:3010/master_table?select=cog_fk(test_id,test_seq_name,test_strain,test_s_year,test_strain_seq),master_result,master_dayoftest,pcr_main_fk(pcr_name,pcr_order_no,pcr_cost,manu_fk(manu_id,manu_name),supplier_fk(supplier_pk,supplier,supplier_add,supplier_postcode,supplier_country),buffer_fk(buffer_id,buffer_name,buffer_conc),enz_fk(enz_id,enz_name,enz_conc),nucleo_fk(nucleo_id,nucleo_conc,nucleo_mix)),denature_fk(denature_temp,denature_time),annealing_fk(annealing_temp, annealing_time),elongate_fk(elongate_temp,elongate_time),master_cycle_count,completion_fk(completion_temp,completion_time),pcr_fk(ref_id,seq_f_fk(seq_id,seq_header,seq_sequence),seq_r_fk(seq_header,seq_sequence)),master_amp_seq,master_purpose,master_primer_conc,master_primer_supplier,master_cost,patient_fk(patient_id,patient_fname,patient_lname,patient_title,patient_phone,patient_email,patient_postcode),scientist_fk(scientist_id,scientist_name,scientist_title,scientist_centre,scientist_phone,scientist_email)

"""

## Task

## Notes
Containers are currently personalised for my personal machine,
please double check file locations in the docker-compose.yaml.

## Containers
