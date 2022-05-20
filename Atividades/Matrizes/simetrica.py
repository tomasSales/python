# Recebe uma matriz e returne True se a matriz for simetrica, em caso contrario retorna False.


def simetrica(matriz):

    print(f"Matriz: {len(matriz), len(matriz[0])}")

    for i in range(len(matriz)):
        print("")

        for j in range(len(matriz[i])):
            print(matriz[i][j], " ", end="")

    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][1] == matriz[1][0] and matriz[0][2] == matriz[2][0] and matriz[1][2] == matriz[2][1]:
        return True
    else:
        return False


a = [[1, 2, 3], [2, 1, 4], [3, 4, 1]]

if simetrica(a):
    print("\n\nAprovado")

else:
    print("\n\nReprovado")
