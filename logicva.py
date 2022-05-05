#como funcionaria el sudoku
class cuerpo():
        
    def rellenar(self,tabla, cuad):
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
        return   = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]]
                  
        
        
        