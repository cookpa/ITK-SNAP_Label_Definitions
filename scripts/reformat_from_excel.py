#!/usr/bin/env python

import sys

def replace_tabs_and_quote(input_file, output_file, tab_width=8):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.strip():  # Skip empty lines
                continue
            expanded_line = ''
            segments = line.rstrip('\n').split('\t')
            for i, segment in enumerate(segments):
                if i == 7:  # Quote the text in the 8th column
                    segment = f'"{segment}"'
                expanded_line += segment
                if i < len(segments) - 1:  # Don't add spaces after the last segment
                    space_count = tab_width - (len(expanded_line) % tab_width)
                    expanded_line += ' ' * space_count
            outfile.write(expanded_line + '\n')

def main():
    if len(sys.argv) != 3:
        print("Usage: replace_tabs.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    replace_tabs_and_quote(input_file, output_file)
    print(f"Tabs replaced with spaces and text in the 8th column quoted in {output_file}")

if __name__ == "__main__":
    main()

