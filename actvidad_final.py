
#Lista
autos = []
 
def registrar_auto(): #Función para registrar un auto
    print("\n---Registrar el auto---") 
    nombrePropietario = input ("Nombre del Propietario: ") #Ingreso de datos del propietario
    placa = input ("Placa del auto: ") #Ingreso de la placa
    anio = input ("Año del auto: ") #Ingreso del año del vehículo
    
    auto = { "Propietario": nombrePropietario, "Placa": placa, "Año": anio } #Crear un diccionario que permite almacenar la información del auto
    autos.append(auto) #Agregar el auto a la lista
    print("El auto ha sido registrado correctamente. \n")
    
def mostrar_autos(): #Función para mostrar los autos registrados
    print("\n---Lista de autos---") 
    if not autos: #Verificar si la lista está vacía
        print("No hay autos registrados.")
    else:
        for auto in autos: #Recorrer la lista de autos
            print(f"Propietario: {auto['Propietario']}, Placa: {auto['Placa']}, Año: {auto['Año']}") #Mostrar los datos del auto

def menu(): #Función del menú principal
    while True:
        print("\n Menú Autos Martin")
        print("1. Registrar auto")
        print("2. Mostrar autos")
        print("3. Salir")
        
        opcion = input ("Seleccione una opción: ")
        if opcion == "1":
            registrar_auto()
        if opcion == "2":
            mostrar_autos()
        elif opcion == "3":
            print("Saliendo del programa")
            break
        
            
def main():
        menu()
        
if __name__ == "__main__":
        main() # Ejecutar el programa principal