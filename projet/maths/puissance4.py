numero = ['1','2',' 3', '4', '5', '6', '7']
plat = [['_']*7,['_']*7,['_']*7,['_']*7,['_']*7,['_']*7]

compt= 0

def affplat():
    for i in range(6):
        print(plat[i])
print()
print(numero)
print()

def gagne(i , j ):
    gagneverti = False
    gagnehoriz = False
    jeton=plat[i][j]
    for k in range(4):
        n=0
        while n<4 and plat[i][j+n]==jeton:
            n+=1
        if n==4:
            gagnehoriz = True
    
    if i<3:
        n=1
        while n<4 and plat[i+n][j]==jeton:
            n+=1
        if n==4:
            gagneverti = True

    if (gagneverti or gagnehoriz):
        print('partie finit',jeton,' a gagne')

    return gagneverti or gagnehoriz

affplat()
print('')

compt = 0
while compt < 42:
    joueur = int(input('Choisissez une colonne')) - 1
    a = compt % 2
    for i in range(5, -1, -1):
        if plat[i][joueur] == '_':
            plat[i][joueur] = 'X' if a == 0 else 'O'
            gagne(i, joueur)
            affplat()
            compt += 1
            break
    else:
        print("Colonne pleine, veuillez rejouer")
    if compt >= 42:
        print('Partie nulle')