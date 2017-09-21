import csv
import sys

columns = []
table = []

def getColumnsInHeader(header):
	for k in range(0, len(header)):
		if header[k].upper() == 'Ncbi_Build'.upper():
			columns.append(k)
		elif header[k].upper() == 'Chrom'.upper():
			columns.append(k)
		elif header[k].upper() == 'Start_Position'.upper():
			columns.append(k)
		elif header[k].upper() == 'Reference_Allele'.upper():
			columns.append(k)
		elif header[k].upper() == 'Tumor_Seq_Allele1'.upper():
			columns.append(k)
		elif header[k].upper() == 'Tumor_Seq_Allele2'.upper():
			columns.append(k)
		elif header[k].upper() == 'Tumor_Sample_Barcode'.upper():
			columns.append(k)

def printMafEncurtado(fileName, reader):
	name = fileName+'.encurted'
	with open(name, 'w') as out:
		writer = csv.writer(out, delimiter='\t')		
		for row in reader:
			line = []
			for col in columns:
				line.append(row[col])
			writer.writerow(line)
		
def readMafFile(fileName):
	with open(fileName, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='\t',  quotechar='|')
		for row in spamreader:
			table.append(row)
		
		header = table[0]
		#print (header)

		getColumnsInHeader(header)
		print('Identified: '+str(columns))
		return table

#Funcao principal
if __name__ == '__main__':
	fileName = sys.argv[len(sys.argv)-1]
	reader = readMafFile(fileName)
	printMafEncurtado(fileName, reader)
	