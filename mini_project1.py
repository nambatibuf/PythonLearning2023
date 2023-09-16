def determine_data_type(value):
    """
    The function takes a string input and determines its data type to be either a float, int, or string. 
    """
    # BEGIN SOLUTION
    try:
        int(value)
        return int
    
    except:
        try:
            float(value)
            return float
        
        except:
            str(value)
            return str
        pass
    # END SOLUTION


def determine_data_type_of_list(values):
    """
    Write a function whose input is a list of strings. 
    This function determines the correct data type of all the elements in the list. 
    For example, ['1', '2', '3'] is int, ['1.1', '2.2', '3.3'] is float, ['1.1', '2', '3.3'] 
    is also float, and ['1.1', '234String', '3.3'] is str. 
    The purpose of this function to figure out what to cast an array of strings to. 
    Some lists might be all ints, in which case the data type is int. 
    Some might be a mixture of ints and floats, in which case the data type will be a float. 
    Some lists might be a mixture of ints, floats, and strings, 
    in which case the data type of the list will be a string.
    NOTE: This function should use "determine_data_type" function you coded previously

    """
    # BEGIN SOLUTION
    temp=[]
    for i in values:
            temp.append(determine_data_type(i))
    temp2=set(temp)
    temp2=list(temp2)
    if len(temp2)==1:
        return temp2[0]
    elif str in temp2:
        return str
    elif float in temp2:
        return float
    else:
        return int
    # END SOLUTION


def format_sample_fields(format_field, sample_field):
    """
    Write a function whose inputs are a format field and sample field. 
    The format field looks like format_field = 'GT:AD:DP:GQ:PGT:PID:PL' and 
    the sample field looks like

    sample_field = {'XG102': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                'XG103': '1/1:0,52:52:99:.:.:1517,156,0',
                'XG104': '0/1:34,38:72:99:.:.:938,0,796',
                'XG202': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                'XG203': '1/1:0,52:52:99:.:.:1517,156,0',
                'XG204': '0/1:34,38:72:99:.:.:938,0,796',
                'XG302': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                'XG303': '1/1:0,52:52:99:.:.:1517,156,0',
                'XG304': '0/1:34,38:72:99:.:.:938,0,796',
                'XG402': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                'XG403': '1/1:0,52:52:99:.:.:1517,156,0',
                'XG404': '0/1:34,38:72:99:.:.:938,0,796'}

    Transform the inputs such that the output looks like this:

    output = {
        'XG102': {'AD': '0,76',
            'DP': '76',
            'GQ': '99',
            'GT': '1/1',
            'PGT': '1|1',
            'PID': '48306945_C_G',
            'PL': '3353,229,0'},
        'XG103': {'AD': '0,52',
                'DP': '52',
                'GQ': '99',
                'GT': '1/1',
                'PGT': '.',
                'PID': '.',
                'PL': '1517,156,0'},
        'XG104': {'AD': '34,38',
                'DP': '72',
                'GQ': '99',
                'GT': '0/1',
                'PGT': '.',
                'PID': '.',
                'PL': '938,0,796'},
        'XG202': {'AD': '0,76',
                'DP': '76',
                'GQ': '99',
                'GT': '1/1',
                'PGT': '1|1',
                'PID': '48306945_C_G',
                'PL': '3353,229,0'},
        'XG203': {'AD': '0,52',
                'DP': '52',
                'GQ': '99',
                'GT': '1/1',
                'PGT': '.',
                'PID': '.',
                'PL': '1517,156,0'},
        'XG204': {'AD': '34,38',
                'DP': '72',
                'GQ': '99',
                'GT': '0/1',
                'PGT': '.',
                'PID': '.',
                'PL': '938,0,796'},
        'XG302': {'AD': '0,76',
                'DP': '76',
                'GQ': '99',
                'GT': '1/1',
                'PGT': '1|1',
                'PID': '48306945_C_G',
                'PL': '3353,229,0'},
        'XG303': {'AD': '0,52',
                'DP': '52',
                'GQ': '99',
                'GT': '1/1',
                'PGT': '.',
                'PID': '.',
                'PL': '1517,156,0'},
        'XG304': {'AD': '34,38',
                'DP': '72',
                'GQ': '99',
                'GT': '0/1',
                'PGT': '.',
                'PID': '.',
                'PL': '938,0,796'},
        'XG402': {'AD': '0,76',
                'DP': '76',
                'GQ': '99',
                'GT': '1/1',
                'PGT': '1|1',
                'PID': '48306945_C_G',
                'PL': '3353,229,0'},
        'XG403': {'AD': '0,52',
                'DP': '52',
                'GQ': '99',
                'GT': '1/1',
                'PGT': '.',
                'PID': '.',
                'PL': '1517,156,0'},
        'XG404': {'AD': '34,38',
                'DP': '72',
                'GQ': '99',
                'GT': '0/1',
                'PGT': '.',
                'PID': '.',
                'PL': '938,0,796'}}
    """

    # BEGIN SOLUTION
    dic={}  
    temp=format_field.split(":")
    for key,value in sample_field.items():
        temp2=value.split(":")
        dic[key]=dict(zip(temp,temp2))
    return dic
    # END SOLUTION


def create_dict_from_line(header, line):
    """
    Given the header and a single line, transform them into dictionary as described above. 
    Header and line input are provided in this cell. 

    Write a function whose inputs are a list containing the vcf header and a variant line. 
    The function should return a dictionary using the header as keys and the variant line as values.
     The function should use the format_sample_fields you wrote previously to format the sample fields. 
     The output of the first line looks like this:

    {'ALT': 'G',
    'CHROM': '4',
    'FILTER': 'PASS',
    'ID': '.',
    'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2,IL21;GeneDetail.refGene=dist=38536,dist=117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471,ENSG00000138684;GeneDetail.ensGene=dist=38306,dist=117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END',
    'POS': '123416186',
    'QUAL': '23.25',
    'REF': 'A',
    'SAMPLE': {'XG102': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG103': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG104': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'},
            'XG202': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG203': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG204': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'},
            'XG302': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG303': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG304': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'},
            'XG402': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG403': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG404': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'}}}
    """
    # BEGIN SOLUTION
    p=line.split("\t")
    temp=dict(zip(header,p))
    format_field=temp.get("FORMAT")
    sample_field = {i: j for i, j in temp.items() if i.startswith('XG')}
    last_temp=format_sample_fields(format_field, sample_field)
    l2={"SAMPLE":last_temp}
    sds=dict(list(temp.items())[:8])
    sds.update(l2)
    return sds
    # END SOLUTION


def read_vcf_file(filename):
    """
    Write a function whose input is a filename for a vcf. 
    The function reads the vcf file one variant at a time and transforms it 
    into a dictionary using the create_dict_from_line function. 
    It returns a list containing all the variant dictionaries. 
    NOTE: Your function should be able to handle multiple lines.
    """
    # BEGIN SOLUTION
    with open(filename) as my_file:
        temp=[]
        for i in my_file:
            if i[0]=='#':
                i=i.strip("#")
                i=i.strip("\n")
                header=i.split("\t")
            else:
                i=i.strip("\n")
                temp2 = create_dict_from_line(header,i)
                temp.append(temp2)
        return temp

    pass
    # END SOLUTION


def extract_info_field(data):
    """
    Write a function that extracts the info field from the data dictionary that was 
    created in the previous part. The function should return all the info field dictionaries as list. 
    """
    # BEGIN SOLUTION
    info_fields = []
    for variant in data:
        info_fields.append(variant['INFO'])
    return info_fields
    pass
    # END SOLUTION


def create_dictionary_of_info_field_values(data):
    """
    You now need to figure out that data types for each of the info fields. Begin by writing a function that first takes the info fields and turns them into a dictionary. Make sure to skip any fields that do not have a value or are missing a value.

    Note: only return keys that have values! 
    """
    dict = {}
    for info in data:
        temp=info.split(';')
        for i in temp:
            if i.rfind("=")==-1:
                continue
            temp2=i.split('=')
            if len(temp2)>1:
                value=['='.join(temp2[1:])]
            else:
                value=[temp2[1]]
            if temp2[1]!='.':
                key = temp2[0]
                if key in dict and dict[key] != value:
                        dict[key]=dict[key]+value
                else:
                    dict[key]=value
    return dict
    # END SOLUTION


def determine_data_type_of_info_fields(data):
    """
    Write a function whose input is the output from create_dictionary_of_info_field_values 
    and uses the previously written function determine_data_type_of_list to determine 
    the data type of each of the info fields. The output is a dictionary whose 
    keys are the name of the info fields and values are the data type. 
    """
    # BEGIN SOLUTION
    dic={}
    for key,value in data.items():
        temp4=determine_data_type_of_list(value)
        dic[key]=temp4
    return dic
    pass
    # END SOLUTION


def format_data(data, info_field_data_type):
    
    output_data=[]
    extracted_data=extract_info_field(data)
    for i in range(len(data)):
        field_data=create_dictionary_of_info_field_values([extracted_data[i]])
        for key, value in field_data.items():
            field_data[key]=info_field_data_type[key](value[0])
        data_dict=data[i]
        data_dict['POS']=int(data_dict.get('POS'))
        data_dict['QUAL']=float(data_dict.get("QUAL"))
        data_dict['INFO']=field_data
        output_data.append(data_dict)
    
    return output_data
    # BEGIN SOLUTION

    pass
    # END SOLUTION


def save_data_as_json(data, filename):
    """
    Write a function whose inputs are a Python dictionary and filename. 
    The function will saves the dictionary as a json file using the filename given. 
    Use the json library. 
    Use these options to correctly format your JSON -- 
    sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False. 
    Use this function to save your parsed data as a json file.
    """
    # BEGIN SOLUTION
    import json
    with open(filename, 'w') as file:
        return json.dump(data,file,sort_keys=True,indent=4,separators=(',', ': '))
    pass
    # END SOLUTION


def load_data_from_json(filename):
    """
    Write a function whose input is a filename for a json file. 
    The function should use the filename to read the JSON file in 
    which you saved your final parsed data. 
    """
    # BEGIN SOLUTION
    import json
    with open(filename) as file:
        return json.load(file)
    pass
    # END SOLUTION


def find_variant(CHROM, REF, ALT, POS, filename):
    """
    Write a function whose inputs are CHROM, REF, ALT, POS, and filename. 
    Using these inputs, the function should load a JSON file using the given 
    filename and return a list of variants that match the given CHROM, REF, ALT, and POS. 
    """
    # BEGIN SOLUTION
    data_json=load_data_from_json(filename)
    final_list=[]

    for entry in data_json:
        if entry["ALT"] == ALT and entry["CHROM"] == CHROM and entry["REF"] == REF and entry["POS"] == POS:
            final_list.append(entry)

    return final_list
    pass
    # END SOLUTION


def pull_basic_and_predictor_fields(filename):
    """
    Load mini_project1_data.json and pull out all the variants that have a 
    """
    pred_scores = {
        "FATHMM_pred": {"T": 0, "D": 1},
        "LRT_pred": {"D": 1, "N": 0, "U": 0},
        "MetaLR_pred": {"T": 0, "D": 1},
        "MetaSVM_pred": {"T": 0, "D": 1},
        "MutationAssessor_pred": {"H": 1, "N": 0, "L": 0.25, "M": 0.5},
        "MutationTaster_pred": {"D": 1, "P": 0, "N": 0, "A": 1},
        "PROVEAN_pred": {"D": 1, "N": 0},
        "Polyphen2_HDIV_pred": {"D": 1, "B": 0, "P": 0.5},
        "Polyphen2_HVAR_pred": {"D": 1, "B": 0, "P": 0.5},
        "SIFT_pred": {"D": 1, "T": 0}
    }
    temp=pred_scores.keys()
    predictors=list(temp)
    other_fields = [
        'CHROM',
        'POS',
        'REF',
        'ALT'
    ]
    import json
    filename = 'mini_project1_data.json'
    with open(filename) as file:
        data_json = json.load(file)
    # BEGIN SOLUTION
    temp=[]
    for i in data_json:
        temp_d={}
        sum_predictor_values = 0
        info = i["INFO"]
        for key in predictors:
            if key in info.keys():
                sum_predictor_values+=pred_scores[key][info[key]]
                temp_d[key]=info[key]
        if len(temp_d.keys())>0:
            temp_d["sum_predictor_values"]=sum_predictor_values
            for k in other_fields:
                temp_d[k]=i[k]
            temp.append(temp_d)
            
    return temp

    pass

def pull_basic_and_predictor_fields_gzip(filename):
    # BEGIN SOLUTION
    predictors = [
        'FATHMM_pred',
        'LRT_pred',
        'MetaLR_pred',
        'MetaSVM_pred',
        'MutationAssessor_pred',
        'MutationTaster_pred',
        'PROVEAN_pred',
        'Polyphen2_HDIV_pred',
        'Polyphen2_HVAR_pred',
        'SIFT_pred',
        'fathmm_MKL_coding_pred'
    ]

    other_fields = [
        'CHROM',
        'POS',
        'REF',
        'ALT'
    ]

    pred_scores = {
        "FATHMM_pred": {"T": 0, "D": 1},
        "LRT_pred": {"D": 1, "N": 0, "U": 0},
        "MetaLR_pred": {"T": 0, "D": 1},
        "MetaSVM_pred": {"T": 0, "D": 1},
        "MutationAssessor_pred": {"H": 1, "N": 0, "L": 0.25, "M": 0.5},
        "MutationTaster_pred": {"D": 1, "P": 0, "N": 0, "A": 1},
        "PROVEAN_pred": {"D": 1, "N": 0},
        "Polyphen2_HDIV_pred": {"D": 1, "B": 0, "P": 0.5},
        "Polyphen2_HVAR_pred": {"D": 1, "B": 0, "P": 0.5},
        "SIFT_pred": {"D": 1, "T": 0},
        "fathmm-MKL_coding_pred": {"D": 1, "N": 0}
    }

    import gzip
    with gzip.open('test_4families_annovar.vcf.gz','rt') as fp:
        temp_l=[]
        for line in fp:
            if line.startswith("#"):
                    continue
            temp_d={}
            line_split = line.strip().split('\t')
            info_field = line_split[7]
            sum_predictor_values=0
            for ele in info_field.split(";"):
                try:
                    k,v=ele.split("=")
                    if k in predictors:
                        if v != ".":
                            temp_d[k]=v
                            sum_predictor_values+=pred_scores[k][v]
                except:
                    pass
            ct=0
            if len(temp_d.keys())>0:
                other_field_vals = line_split[:2]+line_split[3:5]
                for f in other_fields:
                    temp_d[f]=other_field_vals[ct]
                    ct+=1
                temp_d["sum_predictor_values"]=sum_predictor_values
                temp_l.append(temp_d)
    import json
    filename = "mini_project1_gzip.json"
    with open(filename, 'w') as file:
        return json.dump(temp_l, file, sort_keys=True, indent=2, separators=(',', ': '))
    # END SOLUTION


def return_all_non_zero_sum_predictor_values():
    # BEGIN SOLUTION 
    import json
    with open('mini_project1_gzip.json') as file:
        data_json = json.load(file)
    data_l = []
    for i in data_json:
        sum_value = i["sum_predictor_values"]
        if sum_value != 0:
            data_l.append(i)
    with open("sum_predictor_values_gt_zero.json", 'w') as file:
        return json.dump(data_l, file, sort_keys=True, indent=2, separators=(',', ': '))
    # END SOLUTION
