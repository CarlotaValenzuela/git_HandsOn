#!/usr/bin/env python

# Import 
import sys, re
from argparse import ArgumentParser

# Initialize the ArgumentParser object
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')

# Add input sequence (-s or --seq)
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# Add argument for motif (-m or --motif)
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Check if no arguments are provided, if not print the help message and exit
if len(sys.argv) == 1:
    parser.print_help()  # Display the help message
    sys.exit(1)  # Exit the script


args = parser.parse_args()

args.seq = args.seq.upper()

if re.search('^[ACGT]+$', args.seq):  # Sequence contains only ACGT -> DNA
    print('The sequence is DNA')
elif re.search('^[ACGU]+$', args.seq):  # Sequence contains only ACGU -> RNA
    print('The sequence is RNA')
elif re.search('T', args.seq) and re.search('U', args.seq):  # Sequence contains both T and U
    print('ERROR: Sequence contains both T (DNA) and U (RNA), cannot classify.')
else:
    print('ERROR: Invalid sequence. It contains characters other than ACGTU.')

if args.motif:
    args.motif = args.motif.upper()  # Convert motif to uppercase
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("SUCCESSFUL - MOTIF FOUND")
# Convert the sequence to uppercase 
args.seq = args.seq.upper()

# Check if the sequence contains only valid nucleotide
if re.search('^[ACGTU]+$', args.seq):
    # If the sequence contains 'T', classify it as DNA
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    # If the sequence contains 'U', classify it as RNA
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    # If it contains neither 'T' nor 'U', it could be both DNA or RNA
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('ERROR')

# Perform motif search
if args.motif:
    # Convert the motif to uppercase
    args.motif = args.motif.upper()
    # Print a message 
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    # Search for the motif in the sequence and print the result
    if re.search(args.motif, args.seq):
        print("SUCCESSFUL-MOTIF FOUND")  # Motif is found
    else:
        print("MOTIF NOT FOUND")  # Motif is not found
