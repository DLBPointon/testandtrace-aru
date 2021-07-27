CREATE TABLE IF NOT EXISTS cog_table(
    test_id INT PRIMARY KEY,
    test_seq_name VARCHAR(15),
    test_strain VARCHAR(20),
    test_s_year int,
    test_strain_seq VARCHAR
);

CREATE TABLE IF NOT EXISTS seq_table(
    seq_id INT PRIMARY KEY,
    seq_header VARCHAR,
    seq_sequence VARCHAR
);

CREATE TABLE IF NOT EXISTS seq2main_table(
    ref_id INT PRIMARY KEY,
    seq_f_fk INT REFERENCES seq_table(seq_id),
    seq_r_fk INT REFERENCES seq_table(seq_id)
);

CREATE TABLE IF NOT EXISTS supplier_table(
    supplier_pk INT PRIMARY KEY,
    supplier VARCHAR(50),
    supplier_add VARCHAR,
    supplier_postcode VARCHAR(9),
    supplier_country VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS nucleotide_table(
    nucleo_id INT PRIMARY KEY,
    nucleo_conc INT,
    nucleo_mix VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS buffer_table(
    buffer_id INT PRIMARY KEY,
    buffer_name VARCHAR,
    buffer_conc INT
);

CREATE TABLE IF NOT EXISTS manufacturer_table(
    manu_id INT PRIMARY KEY,
    manu_name VARCHAR
);

CREATE TABLE IF NOT EXISTS enzyme_table(
    enz_id INT PRIMARY KEY,
    enz_name VARCHAR,
    enz_conc INT
);

CREATE TABLE IF NOT EXISTS pcr_main_table(
    pcr_id INT,
    pcr_name VARCHAR,
    pcr_order_no INT PRIMARY KEY,
    pcr_cost NUMERIC,
    manu_fk INT REFERENCES manufacturer_table(manu_id),
    supplier_fk INT REFERENCES supplier_table(supplier_pk),
    buffer_fk INT REFERENCES buffer_table(buffer_id),
    enz_fk INT REFERENCES enzyme_table(enz_id),
    nucleo_fk INT REFERENCES nucleotide_table(nucleo_id)
);

CREATE TABLE IF NOT EXISTS patient_table(
    patient_id INT PRIMARY KEY,
    patient_fname VARCHAR,
    patient_lname VARCHAR,
    patient_title VARCHAR(4),
    patient_phone BIGINT,
    patient_email VARCHAR,
    patient_postcode VARCHAR(9)
);

CREATE TABLE IF NOT EXISTS scientist_table(
    scientist_id INT PRIMARY KEY,
    scientist_name VARCHAR,
    scientist_title VARCHAR(4),
    scientist_centre VARCHAR,
    scientist_phone BIGINT,
    scientist_email VARCHAR
);

CREATE TABLE IF NOT EXISTS denature_table(
    denature_pk INT PRIMARY KEY,
    denature_temp INT,
    denature_time INT
);

CREATE TABLE IF NOT EXISTS annealing_table(
    annealing_pk INT PRIMARY KEY,
    annealing_temp INT,
    annealing_time INT
);

CREATE TABLE IF NOT EXISTS elongate_table(
    elongate_pk INT PRIMARY KEY,
    elongate_temp INT,
    elongate_time INT
);

CREATE TABLE IF NOT EXISTS completion_table(
    completion_pk INT PRIMARY KEY,
    completion_temp INT,
    completion_time TIME
);

CREATE TABLE IF NOT EXISTS master_table(
    cog_fk INT REFERENCES cog_table(test_id),
    master_result VARCHAR(8),
    master_dayoftest DATE,
    master_timeoftest TIME,
    pcr_main_fk INT REFERENCES pcr_main_table(pcr_order_no),
    denature_fk INT REFERENCES denature_table(denature_pk),
    elongate_fk INT REFERENCES elongate_table(elongate_pk),
    annealing_fk INT REFERENCES annealing_table(annealing_pk),
    completion_fk INT REFERENCES completion_table(completion_pk),
    master_cycle_count INT,
    pcr_fk INT REFERENCES seq2main_table(ref_id),
    master_amp_seq VARCHAR,
    master_purpose VARCHAR,
    master_primer_conc VARCHAR,
    master_primer_supplier VARCHAR,
    master_cost INT,
    patient_fk INT REFERENCES patient_table(patient_id),
    scientist_fk INT REFERENCES scientist_table(scientist_id)
)