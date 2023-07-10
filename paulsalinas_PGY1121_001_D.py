asi_entra = [14,15]
rut_entra = [19836213,18836213]
pla = 1
gold = 1
silver = 1
XD = 1

udi1 = [1,2,3,4,5,6,7,8,9,10]
udi2 = [11,12,13,'  x','  x','  x',17,18,19,20]
udi3 = [21,22,23,24,25,26,27,28,29,30]
udi4 = [31,32,'  x',34,35,36,37,38,39,40]
udi5 = [41,42,43,44,'  x',46,47,48,49,50]
udi6 = [51,52,53,54,55,56,57,58,59,60]
udi7 = [61,62,63,64,65,66,67,68,69,70]
udi8 = [71,72,73,74,75,76,77,78,79,80]
udi9 = [81,82,83,84,85,86,87,88,89,90]
udi10 =[91,92,93,94,95,96,97,98,99,100]

udicaciones_d1 = """ 


                ESCENARIO
1   2   3   4   5   6   7   8   9   10
11  12  13  x   x   x   17  18  19  20
21  22  23  24  25  26  27  28  29  30
31  32  x   34  35  36  37  38  39  40
41  42  43  44  x   46  47  48  49  50
51  52  53  54  55  56  57  58  59  60
61  62  63  64  65  66  67  68  69  70
71  72  73  74  75  76  77  78  79  80
81  82  83  84  85  86  87  88  89  90
91  92  93  94  95  96  97  98  99  100
"""

udicaciones_nod = [14,15,16,33,45]
udicaciones_d2 = f"""
|---------------------------------------|
|                esenario               |
|---------------------------------------|
|{udi1[0]:3}|{udi1[1]:3}|{udi1[2]:3}|{udi1[3]:3}|{udi1[4]:3}|{udi1[5]:3}|{udi1[6]:3}|{udi1[7]:3}|{udi1[8]:3}|{udi1[9]:3}|
|{udi2[0]:3}|{udi2[1]:3}|{udi2[2]:3}|{udi2[3]:3}|{udi2[4]:3}|{udi2[5]:3}|{udi2[6]:3}|{udi2[7]:3}|{udi2[8]:3}|{udi2[9]:3}|
|{udi3[0]:3}|{udi3[1]:3}|{udi3[2]:3}|{udi3[3]:3}|{udi3[4]:3}|{udi3[5]:3}|{udi3[6]:3}|{udi3[7]:3}|{udi3[8]:3}|{udi3[9]:3}|
|{udi4[0]:3}|{udi4[1]:3}|{udi4[2]:3}|{udi4[3]:3}|{udi4[4]:3}|{udi4[5]:3}|{udi4[6]:3}|{udi4[7]:3}|{udi4[8]:3}|{udi4[9]:3}|
|{udi5[0]:3}|{udi5[1]:3}|{udi5[2]:3}|{udi5[3]:3}|{udi5[4]:3}|{udi5[5]:3}|{udi5[6]:3}|{udi5[7]:3}|{udi5[8]:3}|{udi5[9]:3}|
|{udi6[0]:3}|{udi6[1]:3}|{udi6[2]:3}|{udi6[3]:3}|{udi6[4]:3}|{udi6[5]:3}|{udi6[6]:3}|{udi6[7]:3}|{udi6[8]:3}|{udi6[9]:3}|
|{udi7[0]:3}|{udi7[1]:3}|{udi7[2]:3}|{udi7[3]:3}|{udi7[4]:3}|{udi7[5]:3}|{udi7[6]:3}|{udi7[7]:3}|{udi7[8]:3}|{udi7[9]:3}|
|{udi8[0]:3}|{udi8[1]:3}|{udi8[2]:3}|{udi8[3]:3}|{udi8[4]:3}|{udi8[5]:3}|{udi8[6]:3}|{udi8[7]:3}|{udi8[8]:3}|{udi8[9]:3}|
|{udi9[0]:3}|{udi9[1]:3}|{udi9[2]:3}|{udi9[3]:3}|{udi9[4]:3}|{udi9[5]:3}|{udi9[6]:3}|{udi9[7]:3}|{udi9[8]:3}|{udi9[9]:3}|
|{udi10[0]:3}|{udi10[1]:3}|{udi10[2]:3}|{udi10[3]:3}|{udi10[4]:3}|{udi10[5]:3}|{udi10[6]:3}|{udi10[7]:3}|{udi10[8]:3}|{udi10[9]:3}|
|---------------------------------------|
"""

menu = """ MENU

    1) Compra de entradas
    2) Mostrar dicaciones disponibles 
    3) Ver listado de asistentes 
    4) Mostrar ganancias totales
    5) Salir 

"""

def compra ():
    print ("ha ingresado a compra de entradas")
    while True:
        try:
            c = int(input("ingrese la cantidad de estradas (min 1 -- max 3) : "))
            if c < 1 or c > 3:
                print ("ingrese una cantidad valida")
            else:   
                print(f"esta comprando {c}")
                break
        except:
            print("esta ingresando un dato no valido")

    while True:
        
        print("""selecione su ubicacion
los precios son los sigientes:

|--------------|-----------------------|
| Tipo Entrda  |zona de asientos       |
|platinum      |(asientos del 1 - 20)  |
|gold          |(asientos del 21 - 50) |
|silver        |(asientos del 51 - 100)|
|--------------|-----------------------|
                    """)
        print(udicaciones_d2) 
        i = 1   
        f = i
        while i <= c:    
            print(f"ingrese el asiento {i}:")
            nu = int(input())
        
            if nu == 0 or nu > 100:
                print("ingrese un numero disponible")
                i=i
                  
            for x in range(len(udicaciones_nod)):
                print("aqui2")
                print(f"{udicaciones_nod[x]}")
                if nu == udicaciones_nod[x]:            
                    print("el asiento selecionado no esta disponible")
                    i=i

            if nu <= 20:
                pla = pla +1
                udicaciones_nod.append(nu)  
                asi_entra.append(nu)
                i = i+1  
            if nu > 50:
                silver = silver+1
                udicaciones_nod.append(nu)  
                asi_entra.append(nu)
                i = i+1   
            if nu > 20: 
                if nu <=50:
                    gold = gold+1
                    udicaciones_nod.append(nu)  
                    asi_entra.append(nu)
                    i = i+1  
                          
        while f <= c:
            try:
                print(f"""ingrese el run de la persona del asiento{f} 
                              este deve ser ingresado de la siginte manera (ej: 19216813)""")
                run = int(input())
                if len(run) < 6 or len(run) > 9:
                    print("su rut esta mal ingresado")
                else:
                    rut_entra.append[run]
                    print(f"se ha guardado su run al asiento {f}")
                    f = f+1      
            except:
                print("error en el ingreso de asistente")
        
            
def dispo ():
    print(udicaciones_d2)

def lista ():
    print("ha selecionado ver los asistentes")
    print("""
   |----+----------+--------|
   | n° |run       |asiento |
   |----+----------+--------|""")
    for y in range(len(rut_entra)):
        print(f"""   |{y+1:4}|{rut_entra[y]:9} | {asi_entra[y]:7}|
   |----+----------+--------|""")

def ganan ():
    print("ha selecionado ver las ganacias")
    print(f"""
    | Tipo Entrda      |Cantidad |total      |
    |------------------+---------+-----------|      
    |platinum $120.000 |{pla:9}| {pla*120000:10}|
    |gold     $80.000  |{gold:9}| {gold*80000:10}|
    |silver   $50.000  |{silver:9}| {silver*50000:10}|
    |------------------+---------+-----------| 
    """)
while XD == 1:
    try:
        print (menu)
        print ("selecciones su opcion:") 
        op = int(input())
        if op == 1:
            compra()
        if op == 2:
            dispo()
        if op == 3:
            lista()
        if op == 4:
            ganan()
        if op == 5:
            print("usted a salido del programa") 
            XD = 2
    except:
        print("error menu")
