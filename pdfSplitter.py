#Importing the necessary modules

import os
import PyPDF2

os.chdir('/Users/glencoppens/Downloads')

inputpdf =   PyPDF2.PdfFileReader(open("FOPAI_0031_110496_000003_000129_20170327_000003 (1).PDF", "rb"))

properties = 'Fiche de paie 2017-04',
names = ("TRO", "BDE", "LBE", "GCO", "ITO", "FVB", "ANI", "WME","MNO")
filename = []

for prefix in properties:
    for suffix in names:
        filename.append("{} {}.pdf".format(suffix, prefix))

for i, name in enumerate(filename):
    output = PyPDF2.PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(name, 'wb') as f:
        output.write(f)
        print(f)



#Changing the filename from XXX Fiche de paie to XXX Loonfiche if person speaks dutch

path = "/Users/glencoppens/Downloads"

for file in os.listdir("/Users/glencoppens/Downloads"):
    if file.startswith('GCO')\
           or file.startswith("FVB")\
            or file.startswith("ANI")\
            or file.startswith("WME"):
        os.rename(path + "/"+file, path + "/"+file.replace("Fiche de paie", "Loonfiche"))
        print(file)
