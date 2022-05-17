# Recebe uma matriz e returne True se a matriz for simetrica, em caso contrario retorna False.


def simetrica(matriz=bool):

    print(f"Matriz: {len(matriz), len(matriz[0])}")

    for i in range(len(matriz)):
        print("")
        for j in range(len(matriz[i])):
            print(matriz[i][j], "   ", end="")


a = [[11, -3, 4, 8], [-3, 12, 6, 11], [4, 6, 5, 13], [8, 11, 13, 5]]

if simetrica(a):
    print("Aprovado")

else:
    print("Reprovado")
