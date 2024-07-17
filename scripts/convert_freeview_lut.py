#!/usr/bin/env python3

import sys

def convert_lut_to_itksnap(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:

        header = \
'''################################################
# ITK-SnAP Label Description File
# File format:
# IDX   -R-  -G-  -B-  -A--  VIS MSH  LABEL
# Fields:
#    IDX:   Zero-based index
#    -R-:   Red color component (0..255)
#    -G-:   Green color component (0..255)
#    -B-:   Blue color component (0..255)
#    -A-:   Label transparency (0.00 .. 1.00)
#    VIS:   Label visibility (0 or 1)
#    IDX:   Label mesh visibility (0 or 1)
#  LABEL:   Label description
################################################
'''

        outfile.write(header)

        labelIndex = 0
        labelName = "clear label"
        R = '0'
        G = '0'
        B = '0'
        A = '0'
        new_line = f'{labelIndex:<4} {R:<4} {G:<4} {B:<4} {A:<4} 1   1   "{labelName}"\n'
        outfile.write(new_line)

        for line in infile:
            # Split the line into components
            components = line.strip().split()
            if len(components) != 6:
                continue  # Skip any lines that do not have exactly 6 columns

            labelIndex = components[0]
            labelName = components[1]
            R = components[2]
            G = components[3]
            B = components[4]
            A = '1'  # ITK-SNAP uses 1 for opaque

            # Construct the new line in ITK-SNAP format with aligned columns
            new_line = f'{labelIndex:<4} {R:<4} {G:<4} {B:<4} {A:<4} 1   1   "{labelName}"\n'
            outfile.write(new_line)

def print_usage():
    usage = """Usage: convert_lut.py <input_file> <output_file>

    <input_file>  : Path to the Freeview LUT file
    <output_file> : Path to the output ITK-SNAP label definition file
    """
    print(usage)

def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_lut_to_itksnap(input_file, output_file)

if __name__ == "__main__":
    main()

