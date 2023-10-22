# Andrew Shen
# October 2023
# Script to preprocess BGC genomes into chunks for input into species classification task


# Read in the 10 BGC genomes
curr_bgc_location = "/global/scratch/users/andrew7shen/data/species/"
curr_human_location = "/global/scratch/users/andrew7shen/data/species_example"
bgc_genome_paths = ["Bacillus_subtilis", "Enterococcus_faecalis", "Lactobacillus_fermentum", "Pseudomonas_aeruginosa", "Salmonella_enterica", "Cryptococcus_neoformans", "Escherichia_coli", "Listeria_monocytogenes", "Saccharomyces_cerevisiae", "Staphylococcus_aureus"]

# Split them into the bacterial and yeast genomes

# Iterate through each of the 7 training bacterial genomes

    # Store the entire genome as string curr_genome_str
    
    # Iterate through curr_genome_str in blocks of 20k, skipping by 5k
    
        # Prepend string with info about chr # and species
    
        # Save current block of 20k bp as curr_chunk_str
        
        # Match formatting to the human chromosome files
        
        # Write curr_chunk_str to appropriate directory as chr#.fa
        
        