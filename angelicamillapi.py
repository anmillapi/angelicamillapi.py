import random
import csv 
import math

#lista de empleados
trabajadores = ["Juan Pérez", "María García", "Carlos López" , "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez","Francisco Díaz", "Elena Fernández"]

#diccionario para almacenar los sueldos de los empleados
sueldos = {}
def asignar_sueldos():
    """asignatura sueldo aleatorios entre $300.000 y $2.500.000 a los empleados"""
    global sueldos 
    sueldos ={trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    """Clasifica los sueldos en diferentes categorias y muetra los resultados."""
    menores_800k = [(nombre, sueldo) for nombre, sueldo in sueldos.items() if sueldo < 800000]
    entre_800k_y_2m = [(nombre, sueldo) for nombre, sueldo in sueldos.items if 800000 <= sueldo <=2000000]
    mayores_2m = [(nombre, sueldo) for nombre, sueldo in sueldos.items () if sueldo > 2000000 ]
    
    print(f"sueldos menores a $800.000 Total:  {len(menores_800k)}")
    for nombre, sueldo in menores_800k:
        print(f"{nombre} ${sueldo}")
        
    print(f"\nSueldos entre $800.000 y $2.000.000 Total: {len(entre_800k_y_2m)}")
    for nombre, sueldo in entre_800k_y_2m:
        print(f"{nombre} ${sueldo}")
        
    print(f"\nSueldos superiores a $2.000.000 Total: {len(mayores_2m)}")
    for nombre. sueldo in mayores_2m:
        print(f"{nombre} ${sueldo}")
        
    total_sueldos = sum(sueldos.values())
    print(f"\nTotal sueldos: ${total_sueldos}")
    
def ver_estadisticas():
    """muestra estadisticas  sobre los sueldos."""
    if not sueldos:
        print("no hay sueldos asignados.")
        return
    
    sueldos_lista = list(sueldos.values())
    sueldo_mas_alto = max(sueldos_lista)
    sueldo_mas_bajo = min(sueldos_lista)
    promedio_sueldos = sum(sueldos_lista) / len(sueldos_lista)
    media_geometrica = math.exp(sum(math.log(sueldo) for sueldo in sueldos_lista)/ len(sueldos_lista))
    
    print(f"sueldo mas alto: ${sueldo_mas_alto}")
    print(f"sueldo mas bajo ${sueldo_mas_bajo}")
    print(f"promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"media geometrica_ {media_geometrica:.2f}")
    
def reporte_sueldos():
    """reporte de sueldos y este es guardado en un archivo csv"""
    if not sueldos:
        print("no hya sueldos asignados.")
        return
    
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = {'nombre empleado', 'sueldo base', 'descuento salud', 'descuento AFP', 'sueldo liquido'}
        writer =csv.direcwitrer(csvfile, fieldnames=fieldnames)
        
        writer.writerheader()
        for nombre, sueldo in sueldo.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo *0.12
            sueldo_liquido= sueldo - descuento_salud - descuento_afp
            writer.writerow({
                'nombre empleado': nombre,
                'sueldo base': sueldo,
                'descuento salud': descuento_salud
                'descuento afp': descuento_afp
                'sueldo liquido':sueldo_liquido
            })
    print("reporte de sueldos guardados en 'reporte_sueldos.csv'.")

def  mostra_menu():
    """muestra el menu principal"""
    while True:
        print("\----------- Menu principal -----------")
        print("1. Asignar sueldos aletatorios")
        print("2. Clasificar sueldos ")
        print("3. ver estadisticas")
        print("4. reporte de sueldos ")
        print("5.salir del programa")
        
        opcion = input("elija una opcion de 1 a 5: ")
        
        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5:
             print("Finalizando programa.... Desarrollado por Carlos Vergara. RUT 12.345.678-9")
             break
        else: 
         print("Opcion no valida. Por favor ingrese una opcion del 1 al 5")
            
if __name__ == "__main__":
    mostra_menu
        
    
        
    
        
    
    
    
    