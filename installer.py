import urllib.request
import os

def installer():
    urllib.request.urlretrieve("https://github.com/Mat-12/The_Filvi_Game/releases/download/0.1/The.Filvi.GameUbuntu.zip",".file.zip")
    os.system("unzip .file.zip")
    os.system("pip3 install pygame")
    os.system("pip3 install keyboard")

print('''\n\n
/\/\/\/\/\//\/\/\/\/\//\/\/\/\/\//\/\/\/\/\//\/\/\/\/\/
            Mat Games Store Installer
/\/\/\/\/\//\/\/\/\/\//\/\/\/\/\//\/\/\/\/\//\/\/\/\/\/\n\n
''')

y_n = input("Vuoi installare Mat Games Store (y/n) --> ")

if y_n == "y":
    installer()

else:
    print("! Installazione annullata !")