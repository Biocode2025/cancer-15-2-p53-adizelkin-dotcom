import random
file=open("scripts/holder.gitkeep","r")
fileW=open("scripts/mutated_p53.fasta","w")

def Mutate_DNA(seq):
    mut=""
    for j in range (3):
     place = random.randint(0,len(seq)-1)
     nuc=random.randint(1,4)
     for i in range (len(seq)-1):
      if seq[i,i+2]=="UAA" or seq[i,i+2]=="UAG" or seq[i,i+2]=="UGA":
         break
      if i==place and nuc !=seq[i]:
        if nuc == 1:
            mut+="A"
        elif nuc == 2:
            mut+="T"
        elif nuc == 3:
            mut+="C"
        elif nuc == 4:
            mut+="G"
      else:
       mut+=seq[i] 
    return mut   

seq=""
for line in file:
   seq+=line


fileW.write("the original:")
fileW.write(seq)
fileW.write("the muted:")
fileW.write(Mutate_DNA(seq))
if len(Mutate_DNA(seq))<seq:
   fileW.write("got smaller")
elif len(Mutate_DNA(seq))==seq:
   fileW.write("stayd same length")