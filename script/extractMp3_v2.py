import os
from os import path
from itertools import islice
import csv


Path = "" # chemin à modifier selon l'emplacement sinon vide
langues = ["es", "fr", "ar" ] # definir listes des langues avec lesquelles on va travailler

def create_textfiles(row, langue):
    fileName = str(row[0].split('.')[0])
    ''' renommage fichier quand trop long '''
    output_path = '../output/textfiles/' +langue + "/" + fileName + '.txt'
    # Check if the output file already exists
    output_directory = os.path.dirname(output_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print("creating folders...")
    with open(output_path, 'w') as f:
        f.write(row[1])
        # f.close()


   
def main():
    
    for langue in langues:
        file_path = Path + "../corpus/" + langue + "/validated.tsv"
        # Check if the file exists
        if os.path.exists(file_path):
            
            with open(Path+ file_path, "r") as tsvfile:
                reader = csv.reader(tsvfile, delimiter='\t')
                next(reader)
                data = []
                for row in reader:
                    newRow = row[1:3]
                    data.append(newRow) ### what does data do ?
                    create_textfiles(newRow, langue)
                    
                    with open ("../output/textfiles/" +langue + "/" + "data.tsv", 'w') as csvfile:
                        writer =  csv.writer(csvfile, delimiter="\t")
                        # header = 
                        for line in data:
                            if line:
                                writer.writerow(line)
                print(f'len data = {len(data)}')

        else:
            print("Données indisponibles pour " + langue)




if __name__== "__main__":
    main()