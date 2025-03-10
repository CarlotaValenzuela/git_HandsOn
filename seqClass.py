#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

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
    else:
        print("MOTIF NOT FOUND")
