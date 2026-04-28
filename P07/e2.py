def print_genes(genes):
    print("Dictionary of Genes!")
    print(f"There are {len(genes)} genes in the dictionary:\n")

    for gene, gene_id in genes.items():
        print(f"{gene}: --> {gene_id}")

genes ={
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6-269P": "ENSG00000212385",
    "MIR633": "ENSG00000207716",
    "TTTY4C": "ENSG00000229807",
    "RBMY2YP": "ENSG00000214728",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

print_genes(genes)