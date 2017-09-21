from subprocess import call

fileNames = []

def removeAndCreateFolders():
	call(['rm', '-r', 'encurtedMafFolder/'])
	call(['rm', '-r', 'vcfFolder/'])

	call(['mkdir', 'encurtedMafFolder/'])
	call(['mkdir', 'vcfFolder/'])


def moveAll(fileName):
	call(['mv', fileName+'.encurted', './encurtedMafFolder/'])
	call(['mv', fileName+'.vcf', './vcfFolder/'])

def findMafFiles():
	fileOut = open('finded.txt', 'w')
	call(['find', 'sources/', '-name', '*.maf'], stdout=fileOut)
	attachFileNames()

def attachFileNames():
	with open('finded.txt', 'r') as mafFiles:
		while(True):
			line = mafFiles.readline().rstrip();
			if line == '':
				break
			fileNames.append(line)

#Funcao principal
if __name__ == '__main__':

	removeAndCreateFolders()
	findMafFiles()

	for n in fileNames:
		#fileName = "sources/hgsc.bcm.edu__Illumina_Genome_Analyzer_DNA_Sequencing_level2.maf"
		fileName = n
		call(['python',  'encurtarMaf.py', fileName])

		fileOut = open(fileName+'.vcf', 'w')
		call(['perl',  'maf-TO-vcf.pl', fileName+'.encurted'], stdout=fileOut)
		fileOut.close()

		moveAll(fileName)