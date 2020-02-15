s=input("S'il vous plait entre vous votre message d'excuse:\n ")
c1=0
c2=0
c3=0
c4=0
formalle=False
x=s.startswith("Bonjour")
y=s.startswith("Salut")
if x or y :
    c1=1
else :
    print("Ton message dois commencer par 'Bonjour' ou 'salut'")
count=s.count("desole") or s.count("excuse")

if count :
    c2=2
else :
    print("votre msg dois contient mot 'desole' ou 'excuse'")
if  s.count("nous ")<= 2 :
    c3=3
else:
    print("le motb nous' ' ne doit pas se repeter 2 fois")
if len(s)>20 and 100>len(s):
    c4=4
else:
    print("votre message dois etre ou moins 20 charactere et au max 100 characteres")
formalle=c1+c2+c3+c4
if formalle==4:
    print("votre message est valide")
else:
    print("repeter une autre fois")
