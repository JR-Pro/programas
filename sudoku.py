import logicva
logica = logicva.cuerpo()
class sudo():
    
    def MenuPrincipal(self):   
        print ("Bienvenido \n")
        print ("Desea solucionar un Sudoku? (S/N):")
        deseo = input()
        if deseo.lower()=='s':
            sudoku=logica.forma()
            logica.valores(sudoku)
            logica.SolucionaSudoku(sudoku)
        print ("Desea generar un Sudoku? (S/N):")
        deseo = input()
        if deseo.lower()=='s':
            print ("Nivel de dificultat? (facil=0/medio=1/dificil=2):")
            dificultad = int(input())
            sudoku = logica.forma()
            logica.rellenar(sudoku,1)
            logica.rellenar(sudoku,5)
            logica.rellenar(sudoku,9)
            logica.RellenaPosibilidades(sudoku)
            if dificultad=="0":
                logica.O_Celdas(sudoku,"facil")
            elif dificultad =="1":
                logica.O_Celdas(sudoku,"medio")
            else:
                logica.O_Celdas(sudoku,"dificil")
            logica.vertabla(sudoku)
            print ("Desea ver la solucion ahora? (S/N):")
            solucion = input()
            if solucion.lower()=='s':
                logica.SolucionaSudoku(sudoku)
                
                