import csv
import os
import shutil
import sys

from extractMp3 import langues





# shutil.move(source, destination, copy_function = copy2)
# with open ("../output/" +langue + "/" + "data.tsv", 'a') as csvfile:
# output_path = '../output/textfiles/' +langue + "/" + fileName + '.txt'

def move_mp3(fileName,input_path, output_path):
    
    
    # if not os.path.exists(input_path):
    #     print(f"Input path '{input_path}' does not exist.")
    #   
    # return
    
    if not fileName.endswith(".mp3"):
        fileName = fileName + ".mp3"
        
    # shutil.move((input_path+fileName), (output_path+fileName))
    print(fileName+ "\n")
    
    try:
        shutil.move((input_path+fileName), (output_path+fileName))
        print(input_path+fileName, output_path+fileName)
        

    except FileNotFoundError as e:
        print(f"File {input_path+fileName} not found!")
    #     return





def main():
    # output_path = "../output/textfiles/" +langue + "/"
    # input_path = "../corpus/" + langue + "/clips/"

    for langue in langues:
        output_path = "../output/audiofiles/" + langue + "/"
        input_path = "../corpus/" + langue + "/clips/"
        
        output_directory = os.path.dirname(output_path)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
            print("creating folders...")

        if os.path.exists("../output/textfiles/" + langue + "/" + "data.tsv"):
            with open ("../output/textfiles/" + langue + "/" + "data.tsv", 'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter='\t')
                
                print(csv_reader)

                # Iterate through each row in the CSV file
                for row in csv_reader:
                    # print(f'row =   {row[0]}')
                    # print()
                    # Extract the value of the first column
                    mp3_file = row[0]
                    print(f"mp3_File = {mp3_file} ")
                    move_mp3(mp3_file, input_path, output_path)
                    
            
            
    


if __name__=="__main__":
    main()