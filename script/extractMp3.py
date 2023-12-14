import csv


def create_textfiles(row):

    fileName = str(row[0].split('.')[0])
    with open('output/' +fileName +'.txt', 'w') as f:
        f.write(row[1])
        f.close()


with open('validated.tsv', 'r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    data = []
    for row in reader:
        newRow = row[1:3]
        data.append(newRow)
        if newRow != ['path', 'sentence']:
            create_textfiles(newRow)


    with open ('data.tsv', 'a') as csvfile:
        writer =  csv.writer(csvfile, delimiter="\t")
        for line in data:
            writer.writerow(line)


        