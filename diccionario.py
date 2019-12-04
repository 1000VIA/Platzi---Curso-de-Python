def run():
    calificaciones = {}

    calificaciones['algoritmos'] = 4.5
    calificaciones['js'] = 5
    calificaciones['python'] = 4
    calificaciones['bases_de_datos'] = 5
    suma_de_calificaciones = 0

    print('')
    print('Retornar solo llaves:')
    for key in calificaciones:
        print('Las competencias es: {}'.format(key))

    print('')
    print('Retornar solo los valores:')
    for value in calificaciones.values():
        print('La calificación es:  {}'.format(value))

    print('')
    print('Retornar llaves y valores:')
    for key, value in calificaciones.items():
        print('Llaves: {}, valor: {}'.format(key, value))

    print('')
    print('La suma y el promedio de las calificaciones:')
    for calificacion in calificaciones.values():
        suma_de_calificaciones += calificacion
        promedio = suma_de_calificaciones/len(calificaciones)
    print('')
    print('La sumas es: {}'.format(suma_de_calificaciones))
    print('')
    print('Promedio: {}'.format(promedio))


if __name__ == "__main__":
    run()
