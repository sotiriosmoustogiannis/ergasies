a=map(int, raw_input("dwse mia seira apo ari8mous me keno metaksi toys: \n").split()) # xwrizei toys ari8mous me keno

b=a.count(0) # metrao ta mhdenika stoixeia ths listas

for i in range (b):
    a.remove(0) # aferei to prwto mhdeniko poy briskei sth lista
    a.append(0) # prosthetei to mhdenika sto telos

print a
