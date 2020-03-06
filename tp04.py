#!/usr/bin/env python
#- * -coding: utf - 8 - * -##testdom2.py##
DATA_FILE = 'annuaire-v0.2.xml'
import xml.dom.minidom as minidom
import sys
def main():
    try:
        xmldoc = minidom.parse(DATA_FILE)
    except:
        print("Can't Open the file",)
    sys.exit()
    print(xmldoc.toxml())
    return 0
def treat_doc(xmldoc):
    # get the annuaire list
    annuaire = xmldoc.getElementsByTagName('annuaire')[0]
    print (annuaire)
    cpt = 0
    # display personne by personne
    for personne in annuaire.childNodes:
     print("-"*40)
    print ("Personne n°", cpt)
    print (personne.toxml())
    cpt += 1
if __name__ == '__main__':
    main()