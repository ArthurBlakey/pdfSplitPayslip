#Importing the necessary modules
import os
import PyPDF2


#Making sure we're in the right directory
os.chdir('/Users/myname/Downloads')


#Choosing which pdf file we're going to split
inputpdf =   PyPDF2.PdfFileReader(open("File with all the paylsips.PDF", "rb"))

#Parts that make up the filename, and how those parts are structured to make up a filename
properties = 'Fiche de paie 2017-0X',
names = ("TRO", "BDE", "LBE", "GCO", "ITO", "FVB", "ANI", "WME", "CBE", "MNO")
filename = []

for prefix in properties:
    for suffix in names:
        filename.append("{} {}.pdf".format(suffix, prefix))

for i, name in enumerate(filename):
    output = PyPDF2.PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(name, 'wb') as f:
        output.write(f)



#Changing the filename from XXX Fiche de paie to XXX Loonfiche if person speaks dutch
path = "/Users/myname/Downloads"

for file in os.listdir("/Users/myname/Downloads"):
    if file.startswith(("GCO", "FVB", "ANI", "WME")):
        os.rename(path + "/"+file, path + "/"+file.replace("Fiche de paie", "Loonfiche"))
        print(file)
