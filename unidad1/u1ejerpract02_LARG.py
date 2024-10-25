dicRouters = {}
dicRouters = {'Linksys Hydra 6 MR2000-KE':'192.168.1.100','D-Link DWR-953V2':'192.168.1.101', 'AVM FRITZ!Box 7590': '192.168.1.102', 'ASUS ROG Rapture GT-AX11000 Pro' : '192.168.1.103'}

while True:
    print('Menu de opciones')
    print('a. Agregar nombre de Router y su IP.')
    print('b. Modificación de Router y su IP.')
    print('d. Eliminación de Router')
    print('c. Listado de Routers')
    print('d. Verificar el tamaño del diccionario')
    print('e. Salir')
    opcion = input('Seleccione una opción:') 
    if opcion == 'a':
        while True: 
            nombre = input('Ingrese el nombre del router: ').strip()
            ip = input('Ingrese la dirección IP del router: ').strip()
            if not nombre:
                print('No puede haber campos vacíos, por favor ingrese un router.')
                continue 
            if not ip:
                print('No puede haber campos vacíos, por favor ingrese una dirección IP.')
                continue
            if nombre in dicRouters:
                print('El nombre del router ya existe')
                continue
            if ip in dicRouters.values():
                print('La dirección IP ya esta en uso')
                continue
            dicRouters[nombre] = ip 
            print('Router agregado correctamente ')
            break
    elif opcion == 'b':
        while True:
            nombre = input('Ingrese el nombre del router a modificar: ').strip()
            if not nombre:
                print('No puede haber campos vacíos, por favor ingrese un router.')
                continue 
            if nombre not in dicRouters:
                print('El router no esta en el diccionario')
            break
            nuevaIP = input('Ingrese la nueva IP: ').strip()
            if not nuevaIP:
                print('No puede haber campos vacíos, por favor ingrese una dirección IP.')
                continue
            if nuevaIP in dicRouters.values():
                print('La dirección IP ya esta en uso')
                continue
            dicRouters[nombre] = nuevaIP
            print('Router modificado con éxito')
            break
    elif opcion == '':
        while True:
            nombre = input('Ingrese el nombre del router a eliminar: ').strip()
            if nombre not in dicRouters:
                print('El router no se encuentra en el diccionario ')
                break
            confirmacion = input(f'¿Desea eliminar el router? {nombre} (s/n)').strip().lower()
            if confirmacion == 's': 
                del dicRouters[nombre]
                print('Router eliminado con exito')
            else:
                print('Operación cancelada')
                break
    elif opcion == 'c':
        print('\n Listado de Routers')
        print(f"{'Routeador':< 40}{'Direccion IP':<15}")
        print("-" * 55)
        for nombre, ip in dicRouters.items():
            print(f"{nombre:<40}{ip :<15}")
    elif opcion == 'd':
        print(f'El diccionario contiene {len(dicRouters)} routers')
    elif opcion == 'e':
        print('Saliendo del programa')
    break        