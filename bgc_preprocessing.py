# Andrew Shen
# October 2023
# Script to preprocess BGC genomes into chunks for input into species classification task

# Start script
print("Script 'bgc_preprocessing.py' running...")

# Imports
import gzip

# Read in the 10 BGC genomes
curr_bgc_location = "/global/scratch/users/andrew7shen/data/species/"
curr_human_location = "/global/scratch/users/andrew7shen/data/species_example"
bgc_genome_paths = ["Bacillus_subtilis", "Enterococcus_faecalis", "Lactobacillus_fermentum", "Pseudomonas_aeruginosa", "Salmonella_enterica", "Cryptococcus_neoformans", "Escherichia_coli", "Listeria_monocytogenes", "Saccharomyces_cerevisiae", "Staphylococcus_aureus"]
bgc_genome_dict = {}  # Dictionary that contains input BGC genome strings, key: genome name, value: genome file split by lines
# Read in the file at each of the path locations
for path in bgc_genome_paths:
    curr_file = "/" + path + "_genome.fasta"
    curr_path = curr_bgc_location + path + curr_file
    with open(curr_path, "r") as file:
        curr_genome_in_lines = file.readlines()
        bgc_genome_dict[path] = curr_genome_in_lines

# Read in human chr1 to see length and format
analyze_human = False
if analyze_human:
    human_chr1_path = curr_human_location + "/human/chr1.fna"
    with open(human_chr1_path, "r") as file:
        curr_human_chr1_lines = file.readlines()
    num_bp = 0
    num_lines = len(curr_human_chr1_lines)
    for i in range(1, num_lines):
        curr_line = curr_human_chr1_lines[i]
        num_bp += len(curr_line)
    print("Number of base pairs: " + str(num_bp))

# Split them into the bacterial and yeast genomes
bacterial_genomes = ["Bacillus_subtilis", "Enterococcus_faecalis", "Lactobacillus_fermentum", "Pseudomonas_aeruginosa", "Salmonella_enterica", "Escherichia_coli", "Listeria_monocytogenes", "Staphylococcus_aureus"]
yeast_genomes = ["Cryptococcus_neoformans", "Saccharomyces_cerevisiae"]

# TODO: Iterate through each of the 5 train/val/test bacterial genomes
for genome in ["Bacillus_subtilis", "Enterococcus_faecalis", "Lactobacillus_fermentum", "Pseudomonas_aeruginosa", "Listeria_monocytogenes"]:
    
    # Initialize variables
    curr_genome_header = bgc_genome_dict[genome][0].strip()
    curr_genome_str = bgc_genome_dict[genome][1].strip()
    chr_num = 1
    curr_base = 0
    curr_out_path = curr_bgc_location + genome + "/chr"
    
    # Iterate through curr_genome_str in blocks of 300kb
    while True:
    
        # Prepend string with info about chunk number and species
        curr_chunk = curr_genome_header + " chunk " + str(chr_num) + "\n"
        chunk_length = len(curr_chunk) + 300000
    
        # Save current block of 20k bp as curr_chunk
        curr_chunk += curr_genome_str[curr_base: curr_base+300000]
        curr_chunk = curr_chunk.encode()
        
        # TODO: Match formatting to the human chromosome files
        
        # TODO: Write curr_chunk to appropriate directory as gzipped chr#.fa
        out_path = curr_out_path + str(chr_num) + ".fna.gz"
        file_out = gzip.open(out_path, "wb")
        file_out.write(curr_chunk)
        file_out.close()
        
        # Increment variables
        chr_num += 1
        curr_base += 300000
        
        # Finish iterating through whole genome
        if len(curr_chunk) < 300000:
            break
    
# Finish script
print("Script 'bgc_preprocessing.py' finished!")
        
        