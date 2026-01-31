import random
file=open("scripts/holder.gitkeep","r")
def Mutate_DNA(seq):
    mut=""
    p=0
    for j in range (3):
     place = random.randint(p,len(seq)-1)
     nuc=random.randint(1,4)
     for i in range (len(seq)):
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
      p=i
    return mut   