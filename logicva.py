#como funcionaria el sudoku
# colum = columnas, cuad = cuadrante
import random  
class cuerpo():
    
    def rellenar(tabla, cuad = 1):
        filas = len(tabla)
        colum = len(tabla[0])
        disp = [1,2,3,4,5,6,7,8,9]
        mfilas = rmfilas(tabla,cuad)
        mcolum = rmcolum(tabla,cuad)
        for i  in mfilas:
            for j in mcolum:
                long = len(disp)
                alea = random.randint(0,long-1)
                tabla[i][j] = disp[alea]
                disp.remove(disp[alea])
                
    def forma(self):
        return   [[0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0]]
    
    def valores(tabla):
        filas = len(tabla)
        colum = len(tabla[0])
        centrar = [[],[],[],[],[],[],[],[],[]]
        for i  in range(9):
            while len(centrar[i]) != 9:
                print("Introduzca los valores de la fila", i + 1)
                centrar[i] = int(input())
        for i in range(filas):
            for j in range(colum):       
                tabla[i][j]=int(centrar[i][j])
                
    def vertabla(tabla):
        filas=len(tabla)
        colum=len(tabla[0])
        for i in range(filas):
            if i==0 or i==3 or i==6: print("- - - - - - - - - - - - -")
            for j in range(colum):
                if j==0 or j==3 or j==6: 
                    print("|")
                print(tabla[i][j])
                if j==8: 
                    print("|")
            if i==8: print("- - - - - - - - - - - - -")
            
    def C_Ceros(tabla):
        filas =len(tabla)
        colum=len(tabla[0])
        ceros=0
        for i in range(filas):
            for j in range(colum):
                if tabla[i][j]==0:
                    ceros+=1
        return ceros   
    
    def rmfilas(tabla,cuad):
        if cuad == 1 or cuad == 2 or cuad == 3:
            return [0,1,2]
        elif cuad == 4 or cuad == 5 or cuad == 6:
            return [3,4,5]
        elif cuad == 7 or cuad == 8 or cuad == 9:
            return [6,7,8]

    def rmcolum(tabla,cuad):
        if cuad == 1 or cuad == 2 or cuad == 3:
            return [0,1,2]
        elif cuad == 4 or cuad == 5 or cuad == 6:
            return [3,4,5]
        elif cuad == 7 or cuad == 8 or cuad == 9:
            return [6,7,8]
    
    
        
    
        
        