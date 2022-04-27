"""
Hegycsúcs neve;Hegység;Magasság
Ágasvár;Mátra;789
Bálvány;Bükk-vidék;956
"""
#Hangyás-bérc (2);Börzsöny;854

class Hegyek:
  def __init__(self,sor):
    hegycsucs, hegyseg, magassag = sor.strip().split(";")
    self.hegycsucs = hegycsucs
    self.hegyseg = hegyseg
    self.magassag = int(magassag)
    
with open("hegyekMo.txt","r",encoding="utf-8") as f:
  f.readline()
  lista = [Hegyek(sor) for sor in f]
  
#3
print(f"3.feladat: Hegycsúcsok száma: {len(lista)} db")  

#4
magassagok = [sor.magassag for sor in lista]

ossz = sum(magassagok)
atlag = ossz / len(magassagok)
atlag = str(atlag)
atlag = atlag.replace(".",",")

print(f"4.feladat: Hegycsúcsok átlagos magassága: {atlag} m")

#5
legmagasabb = [(sor.magassag, sor) for sor in lista]

nagy, adat = max(legmagasabb)

print(f"""5.feladat: A legmagasabb hegycsúcs adatai:
      Név: {adat.hegycsucs}
      Hegység: {adat.hegyseg}
      Magasság: {nagy}""")

#6

bekeres = int(input("6.feladat: Kérek egy magasságot: "))

#alternativ megoldás 

#kereso = [sor.hegycsucs for sor in lista if bekeres < sor.magassag and sor.hegyseg == "Börzsöny"]

#if len(kereso) > 0:
  #print(f"      Van {bekeres}m-nél magasabb hegysúcs a Börzsönyben!")
#else: 
   #print(f"      Nincs {bekeres}m-nél magasabb hegysúcs a Börzsönyben!")


volt_e = False
megy = True
while megy:
  for sor in lista:
    if bekeres < sor.magassag and sor.hegyseg == "Börzsöny":
      volt_e = True
      megy = False
  break

if volt_e == True:
  print(f"      Van {bekeres}m-nél magasabb hegysúcs a Börzsönyben!")
else: 
   print(f"      Nincs {bekeres}m-nél magasabb hegysúcs a Börzsönyben!")

egy_lab = 3.280839895

haromezer_lab = len([sor.hegycsucs for sor in lista if sor.magassag * egy_lab > 3000])

print(f"7.feladat: 3000 lábnál magasabb hegycsúcsok száma: {haromezer_lab}")
                     
                     
                     #3000 * egy_lab < sor.magassag * egy_lab])
  
      
  