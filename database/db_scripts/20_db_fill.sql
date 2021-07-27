COPY cog_table FROM '/var/lib/postgresql/tandtdb/sheet4_cog_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY seq_table FROM '/var/lib/postgresql/tandtdb/sheet3_seq_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY seq2main_table FROM '/var/lib/postgresql/tandtdb/sheet3_ref_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY supplier_table FROM '/var/lib/postgresql/tandtdb/sheet2_supplier_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY nucleotide_table FROM '/var/lib/postgresql/tandtdb/sheet2_nucleotide_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY buffer_table FROM '/var/lib/postgresql/tandtdb/sheet2_buffer_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY manufacturer_table FROM '/var/lib/postgresql/tandtdb/sheet2_manu_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY enzyme_table FROM '/var/lib/postgresql/tandtdb/sheet2_enzyme_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY pcr_main_table FROM '/var/lib/postgresql/tandtdb/sheet2_pcr_main_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY patient_table FROM '/var/lib/postgresql/tandtdb/sheet1_patient_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY scientist_table FROM '/var/lib/postgresql/tandtdb/sheet1_scientist_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY denature_table FROM '/var/lib/postgresql/tandtdb/sheet1_denature_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY elongate_table FROM '/var/lib/postgresql/tandtdb/sheet1_elongate_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY annealing_table FROM '/var/lib/postgresql/tandtdb/sheet1_annealing_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY completion_table FROM '/var/lib/postgresql/tandtdb/sheet1_completion_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';
COPY master_table FROM '/var/lib/postgresql/tandtdb/sheet1_master_table_dump.tsv' CSV HEADER DELIMITER E'\t' NULL '';