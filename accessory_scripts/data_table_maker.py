"""
Data_table_maker.py
---------------------

This script is intended to to take data provided for this assignment and split into
tsv files ready for ingestion to a relational postgresql database

"""
import numpy as np
import pandas as pd
import argparse
import csv


def parse_args():
    """
    Take arguments of file locations and hardcode output
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-data1", "--MAIN-DATA",
                        dest="data1",
                        help="Main data file for database",
                        default='/home/dlbp/databse_testandtrace/input_data/test-and-trace-coursework.xlsx')
    parser.add_argument("-data2", "--PRIMER-DATA",
                        dest="data2",
                        help="Primer Data for database",
                        default="/home/dlbp/databse_testandtrace/input_data/primers-test-and-trace.fa")
    parser.add_argument("-data3", "--COG-DATA",
                        dest="data3",
                        help="COG Data for database",
                        default="/home/dlbp/databse_testandtrace/input_data/cog-uk-test-and-trace.fa")
    args = parser.parse_args()
    return args


def sheet1(sheet, kitorder, primer, cog):
    """
    Takes sheet one from excel and parses into usable data tables
    :param sheet:
    :param kitorder:
    :param primer:
    :param cog:
    :return:
    """
    full_table = pd.DataFrame()
    full_table = full_table.append(sheet, ignore_index=False)
    full_table.drop(full_table.columns[0], axis=1, inplace=True)

    test_table = full_table.iloc[0:2]
    info_table = full_table.iloc[3:6]

    denature_table = full_table.iloc[6:8]
    annealing_table = full_table.iloc[8:10]
    elongate_table = full_table.iloc[10:12]
    completion_table = full_table.iloc[13:15]
    cycle_count = full_table.iloc[12:13]
    seq_primer_table = full_table[16:21]
    patient_table = full_table[22:29]
    scientist_table = full_table.iloc[30:37]

    # ------ Code Block for Scientists
    scientist_table = scientist_table.values.tolist()
    scientist_pk, scientist_name, scientist_title, scientist_centre, scientist_phone, scientist_email = [], [], [], \
                                                                                                        [], [], []
    scientist_fk = []
    counter = 0
    for i in scientist_table[0]:
        if not i in scientist_name:
            scientist_pk.append(counter)
            scientist_name.append(i)
            scientist_title.append(scientist_table[1][counter])
            scientist_centre.append(scientist_table[2][counter])
            scientist_phone.append(scientist_table[3][counter])
            scientist_email.append(scientist_table[4][counter])
            counter += 1

    for i in scientist_table[0]:
        if i in scientist_name:
            scientist_fk.append(scientist_pk.index(scientist_name.index(i)))

    scientist_final_table = [scientist_pk, scientist_name, scientist_title,
                             scientist_centre, scientist_phone, scientist_email]
    # ------ Code Block for Test info
    test_table = test_table.values.tolist()
    cog_fk = []
    for i in test_table[0]:

        if any(i in sl for sl in cog):
            for ii in cog:
                if i == ii[1]:
                    cog_fk.append(ii[0])

        else:
            cog_fk.append('99')

    # ------ Code Block for Info
    info_table = info_table.values.tolist()

    # ------ Code Block for seq_primer table
    primer_fk = []
    seq_primer_table = seq_primer_table.values.tolist()
    for i in seq_primer_table[3]:
        for ii in primer:
            if i.startswith(ii[1]):
                primer_fk.append(ii[0])

    # ------ Code Block for patients
    patient_pk, patient_fname, patient_lname,\
    patient_title, patient_phone, patient_email,\
    patient_postcode = [], [], [], [], [], [], []

    patient_table = patient_table.values.tolist()
    counter = 0

    for i in patient_table[1]:
        if not i in patient_fname:
            patient_pk.append(counter)
            patient_fname.append(i)
            patient_lname.append(patient_table[2][counter])
            patient_phone.append(patient_table[4][counter])
            patient_email.append(patient_table[5][counter])
            patient_postcode.append(patient_table[6][counter])
            if len(patient_table[3][counter]) > 4:
                patient_title.append('XXXX')
            else:
                patient_title.append(patient_table[3][counter])
            counter += 1

    patient_final_table = [patient_pk, patient_fname, patient_lname,
                           patient_title, patient_phone, patient_email, patient_postcode]

    costs = [int(item) for item in full_table.values.tolist()[21]]
    cycle_count = [int(item) for item in cycle_count.values.tolist()[0]]

    denature_pk, denature_fk, denature_temp, denature_time = [], [], [], []
    elongate_pk, elongate_fk, elongate_temp, elongate_time = [], [], [], []
    annealing_pk, annealing_fk, annealing_temp, annealing_time = [], [], [], []
    completion_pk, completion_fk, completion_temp, completion_time = [], [], [], []

    denature_table = denature_table.values.tolist()
    annealing_table = annealing_table.values.tolist()
    elongate_table = elongate_table.values.tolist()
    completion_table = completion_table.values.tolist()

    # These could be their own function

    counter = 0
    for i in denature_table[0]:
        if not i in denature_temp:
            denature_pk.append(counter)
            denature_temp.append(i)
            denature_time.append(denature_table[1][denature_table[0].index(i)])
            denature_fk.append(counter)
            counter += 1
        else:
            denature_fk.append(denature_pk.index(denature_temp.index(i)))

    counter = 0
    for i in elongate_table[0]:
        if not i in elongate_temp:
            elongate_pk.append(counter)
            elongate_temp.append(i)
            elongate_time.append(elongate_table[1][elongate_table[0].index(i)])
            elongate_fk.append(counter)
            counter += 1
        else:
            elongate_fk.append(elongate_pk.index(elongate_temp.index(i)))

    counter = 0
    for i in annealing_table[0]:
        if not i in annealing_temp:
            annealing_pk.append(counter)
            annealing_temp.append(i)
            annealing_time.append(annealing_table[1][annealing_table[0].index(i)])
            annealing_fk.append(counter)
            counter += 1
        else:
            annealing_fk.append(annealing_pk.index(annealing_temp.index(i)))

    counter = 0
    for i in completion_table[0]:
        if not i in completion_temp:
            completion_pk.append(counter)
            completion_temp.append(i)
            completion_time.append(completion_table[1][completion_table[0].index(i)])
            completion_fk.append(counter)
            counter += 1
        else:
            completion_fk.append(completion_pk.index(completion_temp.index(i)))

    denature_final_table = [denature_pk, denature_temp, denature_time]
    elongate_final_table = [elongate_pk, elongate_temp, elongate_time]
    annealing_final_table = [annealing_pk, annealing_temp, annealing_time]
    completion_final_table = [completion_pk, completion_temp, completion_time]

    master_table = [cog_fk, test_table[1], info_table[0], info_table[1], info_table[2],
                    denature_fk, elongate_fk, annealing_fk, completion_fk, cycle_count,
                    primer_fk, seq_primer_table[0], seq_primer_table[1], seq_primer_table[2],
                    seq_primer_table[4], costs, patient_pk, scientist_fk]

    master_pd = np.array(master_table).T
    patient_final_pd = np.array(patient_final_table).T
    scientist_f_pd = np.array(scientist_final_table).T
    denature_pd = np.array(denature_final_table).T
    elongate_pd = np.array(elongate_final_table).T
    annealing_pd = np.array(annealing_final_table).T
    completion_pd = np.array(completion_final_table).T

    tsv_sheet_2_out(denature_pd, 'denature_table', 1)
    tsv_sheet_2_out(elongate_pd, 'elongate_table', 1)
    tsv_sheet_2_out(annealing_pd, 'annealing_table', 1)
    tsv_sheet_2_out(completion_pd, 'completion_table', 1)
    tsv_sheet_2_out(scientist_f_pd, 'scientist_table', 1)
    tsv_sheet_2_out(master_pd, 'master_table', 1)
    tsv_sheet_2_out(patient_final_pd, 'patient_table', 1)


def sheet2(sheet):
    """
    Function takes data from sheet 2 and outputs a series of lists which represent columns of data
    ready for ingestion
    :param sheet:
    :return:
    """
    # Main table
    pcr_pk, pcr_kit_name, pcr_order_no, pcr_cost, manu_fk, supplier_fk, buffer_fk, enz_fk, nucleo_fk = [], [], [], [], \
                                                                                                       [], [], [], [], \
                                                                                                       []

    # Manufacturer Table
    manu_pk, manu_name = [], []

    # Supplier Table
    supplier_pk, supplier, supplier_add, supplier_postk, supplier_country = [], [], [], [], []

    # Buffer Table
    buffer_pk, buffer_name, buffer_conc = [], [], []

    # Enzyme Table
    enz_pk, enz_name, enz_conc = [], [], []

    # Nucleotide Table
    nucleo_pk, nucleo_mix, nucleo_conc = [], [], []

    # Initiate Data table and insert excel sheet then convert to series of lists
    full_table = pd.DataFrame()
    full_table = full_table.append(sheet, ignore_index=False)
    full_table.drop(full_table.columns[0], axis=1, inplace=True)
    full_lists = full_table.values.tolist()

    # Parse list 1 into manufacturer, pk and fk
    for i in full_lists[0]:
        if i in manu_name:
            manu_fk.append(int(manu_name.index(i)))
        else:
            new_int = len(manu_name)
            manu_fk.append(new_int)
            manu_name.append(i)
            if not new_int in manu_pk:
                manu_pk.append(new_int)
            else:
                pass

    # Create PK for pcr main table
    counter = 0
    for i in manu_fk:
        pcr_pk.append(counter)
        counter += 1

    # Parse list 2 into kit name
    for i in full_lists[1]:
        pcr_kit_name.append(i)

    # Parse list 3 into pcr order no
    for i in full_lists[2]:
        pcr_order_no.append(i)

    # Parse list 4 into fk, pl, name, address
    for i in full_lists[3]:
        address_list = i.split(',')
        if address_list[0] in supplier:
            supplier_fk.append(int(supplier.index(address_list[0])))
        else:
            supplier.append(address_list[0])
            supplier_country.append(address_list[-1])
            supplier_postk.append(address_list[-2])
            supplier_add.append('.'.join(address_list[1:-2]))
            new_int = len(supplier)
            supplier_fk.append(new_int-1)
            if not new_int in supplier_pk:
                supplier_pk.append(new_int - 1)
            else:
                pass

    # Parse list 5 for costs of pcrkit
    for i in full_lists[4]:
        pcr_cost.append(i)

    # Parse list 6 and 7 for buffer info
    for i in full_lists[5]:
        if i in buffer_name:
            buffer_fk.append(int(buffer_name.index(i)))
        else:
            buffer_conc.append(full_lists[6][full_lists[5].index(i)])
            new_int = len(buffer_name)
            buffer_fk.append(new_int)
            buffer_name.append(i)
            if not new_int in buffer_pk:
                buffer_pk.append(new_int)
            else:
                pass

    for i in full_lists[7]:
        if i in enz_name:
            enz_fk.append(int(enz_name.index(i)))
        else:
            new_int = len(enz_name)
            enz_fk.append(new_int)
            enz_conc.append(full_lists[8][full_lists[7].index(i)])
            enz_name.append(i)
            if not new_int in enz_pk:
                enz_pk.append(new_int)
            else:
                pass

    # Parse list 10 and 11 for nucleotide
    for i in full_lists[9]:
        if i in nucleo_mix:
            nucleo_fk.append(int(nucleo_mix.index(i)))
        else:
            new_int = len(nucleo_conc)
            nucleo_fk.append(new_int)
            nucleo_mix.append("dNTP")  # Very Hacky
            nucleo_conc.append(full_lists[10][full_lists[9].index(i)])
            if not new_int in nucleo_pk:
                nucleo_pk.append(new_int)
            else:
                pass

    # ------ Code Chunk below converts a series of lists that represent rows
    # into a series of lists which represent columns ------
    main_table = [pcr_pk, pcr_kit_name, pcr_order_no, pcr_cost,
                  manu_fk, supplier_fk, buffer_fk, enz_fk, nucleo_fk]
    main_table_pd = np.array(main_table).T

    manu_table = [manu_pk, manu_name]
    manu_table_pd = np.array(manu_table).T

    supplier_table = [supplier_pk, supplier, supplier_add, supplier_postk, supplier_country]
    supplier_pd = np.array(supplier_table).T

    buffer_table = [buffer_pk, buffer_name, buffer_conc]
    buffer_table_pd = np.array(buffer_table).T

    enzyme_table = [enz_pk, enz_name, enz_conc]
    enzyme_table_pd = np.array(enzyme_table).T

    nucleotide_table = [nucleo_pk, nucleo_conc, nucleo_mix]
    nucleotide_table_pd = np.array(nucleotide_table).T

    tsv_sheet_2_out(main_table_pd, 'pcr_main_table', 2)
    tsv_sheet_2_out(manu_table_pd, 'manu_table', 2)
    tsv_sheet_2_out(supplier_pd, 'supplier_table', 2)
    tsv_sheet_2_out(buffer_table_pd, 'buffer_table', 2)
    tsv_sheet_2_out(enzyme_table_pd, 'enzyme_table', 2)
    tsv_sheet_2_out(nucleotide_table_pd, 'nucleotide_table', 2)

    pk_orderno_ref = list(zip(pcr_pk, pcr_order_no))
    return pk_orderno_ref  # This will act as our fk -> pk reference when building the main table.


def tsv_sheet_2_out(data, filename, sheet_no):
    """
    Takes list of lists for a table and creates a tsv for it
    :param data:
    :param filename:
    :param sheet_no:
    :return:
    """
    file_name = f'sheet{sheet_no}_{filename}_dump.tsv'
    print(f'Writing: {filename}')
    for i in data:
        with open(f'database_ingestion_data/{file_name}', 'a+', newline='') as end_file:
            tsv_out = csv.writer(end_file, delimiter='\t')
            tsv_out.writerow(i)

    tsv_prepender(file_name)


def tsv_prepender(file_name):
    """
    Prepends tsv with header info
    :param file_name:
    :return:
    """
    topline = 'I AM THE COLUMN HEADER LINE'
    if file_name == 'sheet1_master_table_dump.tsv':
        top_line = 'cog_fk\tresult\tdate\ttime\torder_no_fk\t' \
                   'denature_fk\telongate_fk\tannealing_fk\tcompletion_fk\tcycle_count\t' \
                   'primer_fk\tseq_to_amp\ttest_purpose\tprimer_conc\t' \
                   'primer_supplier\tcosts\tpatient_pk\tscientist_fk\n'
    elif file_name == 'sheet1_patient_table_dump.tsv':
        top_line = 'patient_pk\tpatient_fname\tpatient_lname\tpatient_title\tpatient_phone\tpatient_email\tpatient_postcode\n'
    elif file_name == 'sheet1_scientist_table_dump.tsv':
        top_line = 'scientist_pk\tscientist_name\tscientist_title\tscientist_centre\tscientist_phone\tscientist_email\n'
    elif file_name == 'sheet2_pcr_main_table_dump.tsv':
        top_line = 'pcr_pk\tpcr_kit_name\tpcr_order_no\tpcr_cost\tmanu_fk\tsupplier_fk\tbuffer_fk\tenz_fk\tnucleo_fk\n'
    elif file_name == 'sheet2_manu_table_dump.tsv':
        top_line = 'manu_pk\tmanu_name\n'
    elif file_name == 'sheet2_supplier_table_dump.tsv':
        top_line = "supplier_pk\tsupplier\tsupplier_add\tsupplier_postk\tsupplier_country\n"
    elif file_name == "sheet2_buffer_table_dump.tsv":
        top_line = 'buffer_pk\tbuffer_name\tbuffer_conc\n'
    elif file_name == "sheet2_enzyme_table_dump.tsv":
        top_line = 'enz_pk\tenz_name\tenz_conc\n'
    elif file_name == "sheet2_nucleotide_table_dump.tsv":
        top_line = 'nucleo_pk\tnucleo_conc\tnucleo_mix\n'
    elif file_name == 'sheet3_seq_table_dump.tsv':
        top_line = 'seq_pk\tseq_header\tseq_seq\n'
    elif file_name == 'sheet3_ref_table_dump.tsv':
        top_line = 'ref_pk\tseq_f_pk\tseq_r_pk\n'
    elif file_name == 'sheet4_cog_table_dump.tsv':
        top_line = 'test_id\ttest_seq_name\ttest_strain\ttest_s_year\ttest_strain_seq\n'
    elif file_name == 'sheet1_denature_table_dump.tsv':
        top_line = 'denature_pk\tdenature_temp\tdenature_time\n'
    elif file_name == 'sheet1_elongate_table_dump.tsv':
        top_line = 'elongate_pk\telongate_temp\telongate_time\n'
    elif file_name == 'sheet1_annealing_table_dump.tsv':
        top_line = 'annealing_pk\tannealing_temp\tannealing_time\n'
    elif file_name == 'sheet1_completion_table_dump.tsv':
        top_line = 'completion_pk\tcompletion_temp\tcompletion_time\n'
    else:
        top_line = 'NULL\n'

    with open(f'database_ingestion_data/{file_name}', 'r+') as file:
        original = file.read()
        top_check = file.seek(0, 0)  # Move the cursor to top line
        if top_check == top_line:
            pass
        else:
            file.seek(0, 0)
            file.write(top_line)
            file.write(original)


def load_data(arguments):
    """
    Loading data logic
    :return:
    """
    sheets = pd.ExcelFile(arguments.data1)
    pcrpk2kitorder = sheet2(sheets.parse('PCR Kit'))  # As data from here is required for sheet 1
    seqpk2primerfk = load_pcr_seq_data(arguments)
    cogpk2testid = load_cog_data(arguments)
    sheet1(sheets.parse('Test'), pcrpk2kitorder, seqpk2primerfk, cogpk2testid)


def load_pcr_seq_data(arguments):
    """
    Loads pcd and sequence data from a fasta
    :param arguments:
    :return:
    """
    # Seq Table
    seq_pk, seq_header, seq_seq = [], [], []

    # Ref table
    ref_pk, seq_f_pk, seq_r_pk = [], [], []

    # pk2fk
    ref, seq = [], []

    with open(arguments.data2, 'r') as orifile:
        for line in orifile:
            if line.startswith('>'):
                if line.strip('>') not in seq_header:
                    seq_header.append(line.strip('>').strip('\n'))
                    seq_pk.append(len(seq_header) - 1)
            if not line.startswith('>') and line.upper().startswith(('A', 'T', 'C', 'G', 'N')):
                seq_seq.append(line.strip())

    # due to inclusion of both forward and reverse, there needs to be a secondary table to
    # link f and r to a pk -> fk in main table
    for i in seq_header:
        if i.endswith('F'):
            seq_f_pk.append(seq_header.index(i))
            fin = ''
            if i.startswith('H'):
                if i.__contains__('|'):
                    fin = i.split(' | ')[0].strip(' CDC')
            if i.startswith('CDC'):
                try:
                    fin = i.replace(' | ', ' ').strip('_R')
                finally:
                    fin = i.replace(' | ', ' ').strip('_F')
            if i.startswith('Char'):
                fin = 'Charité/Berlin (WHO) '
            seq.append(fin.strip())
        else:
            if i.endswith('R'):
                seq_r_pk.append(seq_header.index(i))

    count = 0
    for i in seq_f_pk:
        ref_pk.append(count)
        ref.append(count)

        count += 1

    seq_table = [seq_pk, seq_header, seq_seq]
    seq_table_pd = np.array(seq_table).T

    ref_table = [ref_pk, seq_f_pk, seq_r_pk]
    ref_table_pd = np.array(ref_table).T

    tsv_sheet_2_out(seq_table_pd, 'seq_table', 3)
    tsv_sheet_2_out(ref_table_pd, 'ref_table', 3)

    pk2ref = list(zip(ref, seq))
    return pk2ref


def load_cog_data(arguments):  # The marcus fenix of functions
    """
    Load COG data for target organism sequences
    :param arguments:
    :return:
    """
    # cog sequence ids
    test_id, test_seq_name, test_strain, test_s_year, test_strain_seq = [], [], [], [], []

    with open(arguments.data3, 'r') as orifile:
        for line in orifile:
            if line.startswith('>'):
                line_list = line.split('/')
                test_id.append(len(test_seq_name))
                test_seq_name.append(line_list[0].strip().strip('>'))
                test_strain.append(line_list[1].strip())
                test_s_year.append(line_list[2].strip())
            else:
                test_strain_seq.append(line.strip())

    test_id.append('99')
    test_seq_name.append('NULL')
    test_strain.append('UNKNOWN')
    test_s_year.append('9999')
    test_strain_seq.append('UNKNOWN')
    cog_data = [test_id, test_seq_name, test_strain, test_s_year, test_strain_seq]
    cog_table_pd = np.array(cog_data).T
    tsv_sheet_2_out(cog_table_pd, 'cog_table', 4)

    pk2seqname = list(zip(test_id, test_seq_name))

    return pk2seqname


def main():
    """
    Main logic function
    :return:
    """
    args = parse_args()

    load_data(args)


if __name__ == "__main__":
    main()
