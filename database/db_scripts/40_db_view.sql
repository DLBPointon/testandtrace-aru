CREATE VIEW mk_strain AS
SELECT master_result, patient_fname, patient_lname, patient_postcode, scientist_centre, test_strain
    FROM master_table INNER JOIN scientist_table st on st.scientist_id = master_table.scientist_fk
    INNER JOIN cog_table ct on ct.test_id = master_table.cog_fk
    INNER JOIN patient_table pt on pt.patient_id = master_table.patient_fk
    WHERE test_strain = 'LOND-1362B14';