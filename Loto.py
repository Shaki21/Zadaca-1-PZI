import random

def izvlacenje():
           loto=list(range (1,46))
           brojevi = []
           for i in range(6):
                   brojevi.append(random.choice(loto))
                   loto.pop(loto.index(brojevi[i]))
        
           return brojevi
    
def brojevi_igraca (igracevi,izvuceni):
           pogodeni=0
        
           for broja in igracevi:
                      for brojb in izvuceni:
                                 if broja==brojb:
                                            pogodeni +=1
           return pogodeni
            
brojevi = []
for i in range(6):
           broj=int(input("Unesite broj: "))
           brojevi.append(broj)
    
izvuceni_brojevi=izvlacenje()
pogodeni_brojevi = brojevi_igraca(brojevi,izvuceni_brojevi)

print(" Vasi brojevi su:",brojevi,"\n",
      "Izvuceni brojevi su:",izvuceni_brojevi, "\n",
      "Pogodeno je: ", pogodeni_brojevi, "brojeva")