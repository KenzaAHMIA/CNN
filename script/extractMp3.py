import csv


def create_textfiles(row): # function to create text files
    fileName = str(row[0].split('.')[0]) 
    with open('../corpus/fr/' +fileName +'.txt', 'w') as f: # create text file
        f.write(row[1]) # write sentence to text file
        f.close() # close file


with open('../corpus/fr/validated.tsv', 'r') as tsvfile: # open tsv file
    reader = csv.reader(tsvfile, delimiter='\t') # read tsv file
    data = [] # create empty list
    for row in reader: # loop through each row
        newRow = row[1:3] # create new row with only sentence and path
        data.append(newRow) # append new row to data list
        if newRow != ['path', 'sentence']: # if new row is not the header row
            create_textfiles(newRow) # create text file for each row


    with open ('data.tsv', 'a') as csvfile: # create new tsv file
        writer =  csv.writer(csvfile, delimiter="\t") # write tsv file
        for line in data: # loop through each row
            writer.writerow(line) # write row to tsv file


        