import argparse
import readline
import glob
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Enable tab completion for file names
readline.parse_and_bind("tab: complete")

def complete(text, state):
    """Function to auto-complete filenames when pressing tab."""
    return (glob.glob(text + '*') + [None])[state]

readline.set_completer(complete)

def translate_cds(input_file, output_file):
    """Function to translate CDS sequences into protein sequences."""
    protein_records = []
    for record in SeqIO.parse(input_file, "fasta"):
        protein_seq = Seq(record.seq).translate(to_stop=True)  # Translate CDS to protein
        protein_record = SeqRecord(protein_seq, id=record.id, description="translated protein")
        protein_records.append(protein_record)

    # Write translated proteins to output FASTA file
    SeqIO.write(protein_records, output_file, "fasta")
    print(f" Translation complete! Protein sequences saved to: {output_file}")

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Translate CDS FASTA file to Protein FASTA file.")
    parser.add_argument("-i", "--input", required=True, help="Input CDS FASTA file")
    parser.add_argument("-o", "--output", required=True, help="Output Protein FASTA file")

    args = parser.parse_args()

    # Run translation function
    translate_cds(args.input, args.output)
