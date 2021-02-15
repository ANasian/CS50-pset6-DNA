This is a python application which identifies a person based on their DNA. https://cs50.harvard.edu/x/2020/psets/6/dna/

How it works

- There are two main datasets compated within in this program, firstly the databases CSV files and the DNA sequences, the CSV file contains data of individuals   names and the the number of sequential nucleotides which occur within their DNA. The DNA sequence files contain one 'raw' long string consisting of A, C, G and T which together make up nucleotides.

 - dna.py is used to compare the sequences against the databases. To do this dna.py iterates through the DNA sequences and counts how many sequential occurances of each DNA nucleotide occur and then saves this to an array.

 - the values are then compared to the values contained in the CSVs, if all of the values match a person, it can be concluded that the DNA sequence belongs to them.

NOTE the datasets and dna sequences were provided within CS50.
