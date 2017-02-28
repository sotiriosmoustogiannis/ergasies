a=raw_input("give parentheses: \n")
z=0 # plhthos anoixtwn kai kleistwn parenthesewn
i=0
flag="true"
while i<len(a) and flag=="true":
    if (a[i]=="("):
        z=z+1
    elif (a[i]==")"):
        z=z-1
    if (z<0):
     flag="false" # an ginei arnhtiko to z tote einai lathos giati de ginetai
     # na arxizei mia mathimatikh praksh me )
    i=i+1
if (z==0):
    # otan z=0 tote kathe parenthesh poy anoigei kleinei
   print "TRUE"
else:
    print "FALSE"
    # otan z>0 h z<0 tote shmainei oses parentheseis exoun anoiksei den exoun kleisei
