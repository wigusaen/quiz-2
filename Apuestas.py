arch1= open('Dados.txt','r')
C1=0
Acum1= 0
bandera1=False 
Nombre_primero= ''
apuesta= False
C2=0
for registro in arch1:
    linea=registro.split(',')
    Nombre=str(linea[0])
    Num_apostado=int(linea[1])
    Num_D1=int(linea[2])
    Num_D2=int(linea[3])
    Monto_apostado=int(linea[4])
    Num_total_dados= Num_D1 + Num_D2
    if Num_total_dados== Num_apostado:
        apuesta=True
        C1+=1
        Acum1=Monto_apostado
        print('El jugador gano la apuesta.')
    else:
           apuesta=False 
           print('El jugador perdio la apuesta.')
    if Num_apostado== 12:
           C2+=1
    if bandera1==False and C2==1:
        Nombre_primero= Nombre
        bandera1=True
        if apuesta==True:
        	print(Nombre_primero,'	Fue el primero en apostar al 12 y gano la apuesta')
        else: 
              print(Nombre_primero,'Fue el primero en apostar al 12 y perdio la apuesta')
if C1!=0:
 	promedio = Acum1/C1
 	print('El promedio de Bs apostados en partidas ganadas es de',promedio,'Bs.')
