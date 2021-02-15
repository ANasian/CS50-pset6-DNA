# A DNA software recognition

import sys
import csv

def main():
    # checking Usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py data.csv file.txt")

    # Open in memory the CSV file
    fileCSV = open(sys.argv[1], "r")

    # Create the object for reading the file.csv as dict
    reader = csv.DictReader(fileCSV)

    # open the file.txt for reading, save the sequence in the sequence object (f.read() returns a string)
    with open(sys.argv[2], "r") as f:
        sequence = f.read()

    # Get the counts for each STR (after "name") and save it in a dict
    counts = {}
    for STR in reader.fieldnames[1:]: # [1:] from 1 to the end
        counts[STR] = count_match(sequence, STR)

    # Check each row in the reader for a match
    for row in reader:
        if all(counts[STR] == int(row[STR]) for STR in counts):
            print(row["name"])
            fileCSV.close()
            return
    print("No match")
    fileCSV.close

def count_match(sequence, STR):
    longest = 0
    lenght = len(STR)
    for i in range(len(sequence)): #for every index in the lenght of the sequence
        count = 0
        while True: #keep loopig until the STR repeats on the sequence
            start = i + lenght * count
            end = start + lenght
            if (sequence[start:end] == STR):
                count += 1
            else:
                break
        longest = max(longest, count)
    return longest

if __name__ == "__main__":
    main()

