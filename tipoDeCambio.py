
def  foreign_exchange_calculator(ammount):
    mex_to_col_rate = 172

    return mex_to_col_rate * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a peasos colombianos.')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))

    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()