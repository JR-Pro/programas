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
    
    def RCuadrante(filas,colum):
        if filas <=2 and colum<=2:
            return 1
        elif filas <=5 and colum<=2:
            return 4
        elif filas <=8 and colum<=2:
            return 7
        elif filas <=2 and colum<=5:
            return 2
        elif filas <=5 and colum<=5:
            return 5
        elif filas <=8 and colum<=5:
            return 8
        elif filas <=2 and colum<=8:
            return 3
        elif filas <=5 and colum<=8:
            return 6
        elif filas <=8 and colum<=8:
            return 9
        
    def RetornaPosiblesVertical(tabla,fila,colum):
        disp =[1,2,3,4,5,6,7,8,9]
        filas =len(tabla)
        for i in range(filas):
            if i!=fila:
                valor=tabla[i][colum] #valor que hay asignado
                if valor in disp: #si el valor que hemos leido esta en la lista
                    disp.remove(valor) #lo borramos de la lista ya que no disponible
        return disp
   
    def RetornaPosiblesHorizontal(tabla,fila,colum):
        disp =[1,2,3,4,5,6,7,8,9]
        colum =len(tabla[0])
        for i in range(colum):
            if i!=colum:
                valor=tabla[fila][i] #valor que hay asignado
                if valor in disp: #si el valor que hemos leido esta en la lista
                    disp.remove(valor) #lo borramos de la lista ya que no disponible
        return disp

    def RetornaPosiblesCuadrante(tabla,fila,colum):
        disp =[1,2,3,4,5,6,7,8,9]
        cuad = RCuadrante(fila,colum)
        mfilas = rmfilas(tabla,cuad)
        mcolum = rmcolumnas(tabla,cuad)
        valorinicialenpuntoestudio=tabla[fila][colum]
        tabla[fila][colum]='estudio'
        for i in mfilas:
            for j in mcolum:
                if tabla[i][j]!='estudio':
                    valor=tabla[i][j]
                    if valor in disp:
                        disp.remove(valor)
        tabla[fila][colum]=valorinicialenpuntoestudio #volvemos a poner el valor inicial
        return disp

    def R_Invertidos(posibles):
        imposibles=[]
        if not(1 in posibles):
            imposibles.append(1)
        if not(2 in posibles):
            imposibles.append(2)
        if not(3 in posibles):
            imposibles.append(3)
        if not(4 in posibles):
            imposibles.append(4)
        if not(5 in posibles):
            imposibles.append(5)
        if not(6 in posibles):
            imposibles.append(6)
        if not(7 in posibles):
            imposibles.append(7)
        if not(8 in posibles):
            imposibles.append(8)
        if not(9 in posibles):
            imposibles.append(9)
        return imposibles

    def RetornaTotalPosibles(tabla,fila,columna):
        lista1 =RetornaPosiblesVertical(tabla,fila,columna)
        lista2 =RetornaPosiblesHorizontal(tabla,fila,columna)
        lista3 =RetornaPosiblesCuadrante(tabla,fila,columna)
        lista1 =RetornaInvertidos(lista1)
        lista2 =RetornaInvertidos(lista2)
        lista3 =RetornaInvertidos(lista3)
        listatotal=lista1+lista2+lista3
        listaimposibles=[]
        if 1 in listatotal:
            listaimposibles.append(1)
        if 2 in listatotal:
            listaimposibles.append(2)      
        if 3 in listatotal:
            listaimposibles.append(3)
        if 4 in listatotal:
            listaimposibles.append(4)
        if 5 in listatotal:
            listaimposibles.append(5)
        if 6 in listatotal:
            listaimposibles.append(6)       
        if 7 in listatotal:
            listaimposibles.append(7)
        if 8 in listatotal:
            listaimposibles.append(8)   
        if 9 in listatotal:
            listaimposibles.append(9)
        listaposibles = RetornaInvertidos(listaimposibles)
        return listaposibles

    def CompruebaTerminado(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            valor=0
            for j in range(columnas):
                valor+=tabla[i][j]
            print ("La suma de columna=",i,"es de",valor)
        for j in range(columnas):
            valor=0
            for i in range(filas):
                valor+=tabla[i][j]
            print ("La suma de fila=",i,"es de",valor)

    def RellenaInmediatos(tabla):
        actuado = 0
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            for j in range(columnas):
                if tabla[i][j]==0:
                    posibles = RetornaTotalPosibles(tabla,i,j)
                    if len(posibles)==1:
                        tabla[i][j]=posibles[0]
                        actuado=1
        return actuado

    def RetornaUnoDeLaLista(lista):
                longitud = len(lista)
                return lista[random.randint(0,longitud-1)]

    def RellenaUnaCasillaCon2Posibles(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            for j in range(columnas):
                if tabla[i][j]==0:      #casilla vacia
                    posibles = RetornaTotalPosibles(tabla,i,j)
                    if len(posibles)==2:
                        tabla[i][j]=RetornaUnoDeLaLista(posibles)
                        return 1
        return 0

    def RellenaUnaCasillaCon3Posibles(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            for j in range(columnas):
                if tabla[i][j]==0:      #casilla vacia
                    posibles = RetornaTotalPosibles(tabla,i,j)
                    if len(posibles)==3:
                        tabla[i][j]=RetornaUnoDeLaLista(posibles)
                        return 1
        return 0

    def RellenaUnaCasillaCon4Posibles(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            for j in range(columnas):
                if tabla[i][j]==0:      #casilla vacia
                    posibles = RetornaTotalPosibles(tabla,i,j)
                    if len(posibles)==4:
                        tabla[i][j]=RetornaUnoDeLaLista(posibles)
                        return 1
        return 0

    def RellenaUnaCasillaCon5Posibles(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            for j in range(columnas):
                if tabla[i][j]==0:      #casilla vacia
                    posibles = RetornaTotalPosibles(tabla,i,j)
                    if len(posibles)==5:
                        tabla[i][j]=RetornaUnoDeLaLista(posibles)
                        return 1
        return 0

    def RellenaUnaCasillaCon6Posibles(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            for j in range(columnas):
                if tabla[i][j]==0:      #casilla vacia
                    posibles = RetornaTotalPosibles(tabla,i,j)
                    if len(posibles)==6:
                        tabla[i][j]=RetornaUnoDeLaLista(posibles)
                        return 1
        return 0

    def RellenaUnaCasillaCon7Posibles(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        for i in range(filas):
            for j in range(columnas):
                if tabla[i][j]==0:      #casilla vacia
                    posibles = RetornaTotalPosibles(tabla,i,j)
                    if len(posibles)==7:
                        tabla[i][j]=RetornaUnoDeLaLista(posibles)
                        return 1
        return 0
                    
    def RellenaPosibilidades(tabla):
        filas=len(tabla)
        columnas=len(tabla[0])
        contador=0
        while CuentaCeros(tabla)!=0 and contador<=200:
            contador+=1
            while RellenaInmediatos(tabla)==1:
                print ("rellenada inmediatos")
                #VisualizaTabla(tabla)
            if RellenaUnaCasillaCon2Posibles(tabla):
                print ("rellenada 2 posibles")
                #VisualizaTabla(tabla)
            elif RellenaUnaCasillaCon3Posibles(tabla):
                print ("rellenada 3 posibles")
                #VisualizaTabla(tabla)           
            elif RellenaUnaCasillaCon4Posibles(tabla):
                print ("rellenada 4 posibles")
                #VisualizaTabla(tabla)
            elif RellenaUnaCasillaCon5Posibles(tabla):
                print ("rellenada 5 posibles")
                #VisualizaTabla(tabla)
            elif RellenaUnaCasillaCon6Posibles(tabla):
                print ("rellenada 6 posibles")
                #VisualizaTabla(tabla)
            elif RellenaUnaCasillaCon7Posibles(tabla):
                print ("rellenada 7 posibles")
                #VisualizaTabla(tabla)

    def O_Celdas(tabla,nivel):
        if nivel=="facil":
            maxceros = 35
        elif nivel =="medio":
            maxceros = 39
        else:
            maxceros = 42
        cerosinsertados=0
        contador=0
        filas=len(tabla)
        columnas=len(tabla[0])
        while (maxceros>cerosinsertados and contador<1000):
            contador+=1
            fila=random.randint(0,filas-1)
            columna=random.randint(0,columnas-1)
            if tabla[fila][columna]!=0:
                if len(RetornaTotalPosibles(tabla,fila,columna))==1:
                    tabla[fila][columna]=0
                    cerosinsertados+=1
        #VisualizaTabla(tabla)

    def SolucionaSudoku(tabla):
        ceros = CuentaCeros(tabla)
        bajando = 1
        contador =0
        print("\nEstado inicial de la tabla")
        VisualizaTabla(tabla)
        print ("\nInicialmente hay",ceros,"ceros.")
        while ceros>0 and bajando==1:
            RellenaInmediatos(tabla)
            if ceros > CuentaCeros(tabla):
                ceros = CuentaCeros(tabla)
                bajando = 1
            else:
                bajando = 0
            contador+=1
            print ("En",contador,"pasada quedan",ceros,"ceros")
        print("\nEstado final de la tabla")
        VisualizaTabla(tabla)
        if bajando==0:
                print ("No se pudo solucionar, compruebe que los valores introducidos son correctos")