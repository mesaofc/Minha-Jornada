def result1(resultado1):
    print(f'Resultado: {resultado1}.')

print('"1" operações arítimeticas')
print('"2" operações de conversão')
qual = input('Gostaria de fazer qual tipo de operação?: ')

# Operações aritméticas
if qual == '1':
    resultado1 = float(input('Coloque o primeiro valor: '))

    while True:
        valor1 = float(input('Coloque o próximo valor: '))

        print('Escolha a operação: ')
        print('"1" para adição')
        print('"2" para subtração')
        print('"3" para multiplicação')
        print('"4" para divisão')
        
        operação = input('Digite o número da operação: ')

        if operação == '1':
            resultado1 = resultado1 + valor1
            result1(resultado1)
        elif operação == '2':
            resultado1 = resultado1 - valor1
            result1(resultado1)
        elif operação == '3':
            resultado1 = resultado1 * valor1
            result1(resultado1)
        elif operação == '4':
            if valor1 != 0:
                resultado1 = resultado1 / valor1
                result1(resultado1)
            else:
                print('Não é possível dividir por 0.')
        else:
            print('Operação inválida.')

        continuar = input('Deseja realizar outra operação? (s/n): ')
        if continuar.lower() != 's' and continuar.lower() != 'n':
            print('Por favor escolha entre "s" ou "n".')
        elif continuar.lower() == 'n':
            print('Calculadora encerrada.')
            break

# Operação de Métrica
elif qual == '2':
    
    print('Selecione qual tipo de conversão gostaria de fazer:')
    print('"1" para conversões métricas')
    print('"2" para conversões de temperatura')
    print('"3" para conversões de angular')
    print('"4" para conversões de tempo')
    print('"5" para conversões de peso')
    conversão = input('Selecione um tipo: ')
    
    if conversão == '1':
        valor2 = float(input('Coloque o valor: '))
        print('"1" para km -> m')
        print('"2" para km -> cm')
        print('"3" para km -> mm')
        print('"4" para m -> km')
        print('"5" para m -> cm')
        print('"6" para m -> mm')
        print('"7" para cm -> km')
        print('"8" para cm -> m ')
        print('"9" para cm -> mm')
        print('"10" para mm -> km')
        print('"11" para mm -> m')
        print('"12" para mm -> cm')
                                
        conversão1 = input('Qual medida gostaria de transformar?: ')
        if conversão1 == '1':
            conversão11 = (valor2 * 1000)
            print(f'{valor2}km em Metros fica: {conversão11}m')
        elif conversão1 == '2':
            conversão12 = (valor2 * 100000)
            print(f'{valor2}km em Centímetros fica: {conversão12}cm')
        elif conversão1 == '3':
            conversão13 = (valor2 * 1000000)
            print(f'{valor2}km em Milímetros fica: {conversão13}mm')
        elif conversão1 == '4':
            conversão21 = (valor2 / 1000)
            print(f'{valor2}m em Kilometros fica: {conversão21}km')
        elif conversão1 == '5':
            conversão22 = (valor2 * 100)
            print(f'{valor2}m em Centímetros fica: {conversão22}cm')
        elif conversão1 == '6':
            conversão23 = (valor2 * 1000)
            print(f'{valor2}m em Milímetros fica: {conversão23}mm')
        elif conversão1 == '7':
            conversão31 = (valor2 / 100000)
            print(f'{valor2}cm em Kilometros fica: {conversão31}km')
        elif conversão1 == '8':
            conversão32 = (valor2 / 100)
            print(f'{valor2}cm em Metros fica: {conversão32}m')
        elif conversão1 == '9':
            conversão33 = (valor2 / 10)
            print(f'{valor2}mm em Centímetros fica: {conversão33}cm')
        elif conversão1 == '10':
            conversão41 = (valor2 / 1000000)
            print(f'{valor2}mm em Kilometros fica: {conversão41}km')
        elif conversão1 == '11':
            conversão42 = (valor2 / 1000)
            print(f'{valor2}mm em Metros fica: {conversão42}m')
        elif conversão1 == '12':
            conversão43 = (valor2 / 10)
            print(f'{valor2}mm em Centímetros fica: {conversão43}cm')
        else:
            print('Operação inválida.')


#Conversão de Temperatura
    elif conversão == '2':
        
        print('Escolha uma das opções:')
        print('"1" = Celcius -> Fahrenheit')
        print('"2" = Celcius -> Kelvin')
        print('"3" = Fahrenheit -> Celcius')
        print('"4" = Fahrenheit -> Kelvin')
        print('"5" = Kelvin -> Celcius')
        print('"6" = Kelvin -> Fahrenheit')
        escolha1 = input('Escolha umas das opções: ')
        valor3 = float(input('Coloque o valor: '))
        if escolha1 == '1':
            fart1 = (valor3 * 9/5) + 32
            print(f'{valor3}° Celcius equivale à {fart1}° Fahrenheit')
        elif escolha1 == '2':
            fart2 = (valor3 + 273.15)
            print(f'{valor3}° Celcius equivale à {fart2}° Kelvin')
        elif escolha1 == '3':
            fart3 = (valor3 - 32) * 5/9
            print(f'{valor3}° Fahrenheit equivale à {fart3}° Celcius')
        elif escolha1 == '4':
            fart4 = (valor3 - 32) * 5/9 + 273.15
            print(f'{valor3}° Fahrenheit equivale à {fart4}° Kelvin ')
        elif escolha1 == '5':
            fart5 = (valor3 - 275.15)
            print(f'{valor3}° Kelvin equivale à {fart5}° Celcius')
        elif escolha1 == '6':
            fart6 = (valor3 - 273.15) * 9/5 + 32
            print(f'{valor3}° Kelvin equivale à {fart6}° Fahrenheit')

        else:
            print('Operação Inválida')
        
    
#Conversão Angular    
    elif conversão == '3':
        import math

        def graus_para_radianos(graus):
            return graus * (math.pi / 180)

        def radianos_para_graus(radianos):
            return radianos * (180 / math.pi)

        
        print("Escolha uma opção:")
        print("1. Converter de Graus para Radianos")
        print("2. Converter de Radianos para Graus")
    
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            graus = float(input("Digite o valor em graus: "))
            radianos = graus_para_radianos(graus)
            print(f"{graus} graus equivalem a {radianos:.4f} radianos.")
    
        elif opcao == "2":
            radianos = float(input("Digite o valor em radianos: "))
            graus = radianos_para_graus(radianos)
            print(f"{radianos} radianos equivalem a {graus:.4f} graus.")
    
        else:
            print("Opção inválida. Tente novamente.")
        

#Conversão de tempo
    elif conversão == '4':
    
        
        
        print('Escolha uma das opções:')
        print('"1" de Hora para Minutos')
        print('"2" de Hora para Segundos')
        print('"3" de Hora para Milissegundos')
        print('"4" de Minutos para Horas')
        print('"5" de Minutos para Segundos')
        print('"6" de Minutos para Milissegundos')
        print('"7" de Segundos para Horas')
        print('"8" de Segundos para Minutos')
        print('"9" de Segundo para Milissegundos')
        print('"10" de Milissegundos para Horas')
        print('"11" de Milissegundos para Minutos')
        print('"12" de Milissegundos para Segundos')

        escolha2 = input('Escolha uma das opções: ')
        
        valor4 = float(input('Digite o tempo que desejas transformar: '))

        if escolha2 == '1':
            trans11 = (valor4 * 60)
            print(f'{valor4}h em Minutos fica: {trans11}m')
        elif escolha2 == '2':
            trans12 = (valor4 * 3600)
            print(f'{valor4}h em Segundos fica: {trans12}s')
        elif escolha2 == '3':
            trans13 = (valor4 * 3600000)
            print(f'{valor4}h em Milessegundos fica: {trans13}ms')
        elif escolha2 == '4':
            trans21 = (valor4/60)
            print(f'{valor4}m em Horas fica: {trans21}h')
        elif escolha2 == '5':
            trans22 = (valor4 * 60)
            print(f'{valor4}m em Segundos fica: {trans22}s')
        elif escolha2 == '6':
            trans23 = (valor4 * 60000)
            print(f'{valor4}m em Milessegundos fica: {trans23}ms')
        elif escolha2 == '7':
            trans31 = (valor4/3600)
            print(f'{valor4}s em Horas fica: {trans31}h ')
        elif escolha2 == '8':
            trans32 = (valor4/60)
            print(f'{valor4}s em Minutos fica: {trans32}m')
        elif escolha2 == '9':
            trans33 = (valor4 * 1000)
            print(f'{valor4}s em Milissegundos fica: {trans33}')
        elif escolha2 == '10':
            trans41 = (valor4/3600000)
            print(f'{valor4}ms em Horas fica: {trans41}')
        elif escolha2 == '11':
            trans42 = (valor4/60000)
            print(f'{valor4}ms em Minutos fica: {trans42}')
        elif escolha2 == '12':
            trans43 = (valor4/1000)
            print(f'{valor4}ms em Segundos fica: {trans43} ')
            print('Calculadora encerrada')
    
    elif conversão == '5':
  
        print('"1" de Tonelada para Quilograma')
        print('"2" de Tonelada para Grama')
        print('"3" de Toneladas para Miligrama')
        print('"4" de Quilograma para Tonelada')
        print('"5" de Quilograma para Grama')
        print('"6" de Quilograma para Miligrama')
        print('"7" de Grama para Tonelada')
        print('"8" de Grama para Quilograma')
        print('"9" de Grama para Miligrama')
        print('"10" de Miligrama para Tonelada')
        print('"11" de Miligrama para Quilograma')
        print('"12" de Miligrama para Grama')
        print('"13" de Tonelada para Libra')
        print('"14" de Quilograma para Libra')
        print('"15" de Grama para Libra')
        print('"16" de Miligrama para Libra')
        print('"17" de Libra para Tonelada')
        print('"18" de Libra para Quilograma')
        print('"19" de Libra para Grama')
        print('"20" de libra para Miligrama')
        
        escolha_peso = input('Escolha uma das opções: ')
        valor_peso = float(input('Digite o valor que deseja converter: '))

        if escolha_peso == '1':
            resultado = valor_peso * 1000
            print(f'{valor_peso} Tonelada(s) equivalem a {resultado} Quilograma(s).')
        elif escolha_peso == '2':
            resultado = valor_peso * 1000000
            print(f'{valor_peso} Tonelada(s) equivalem a {resultado} Grama(s).')
        elif escolha_peso == '3':
            resultado = valor_peso * 1000000000
            print(f'{valor_peso} Tonelada(s) equivalem a {resultado} Miligrama(s).')
        elif escolha_peso == '4':
            resultado = valor_peso / 1000
            print(f'{valor_peso} Quilograma(s) equivalem a {resultado} Tonelada(s).')
        elif escolha_peso == '5':
            resultado = valor_peso * 1000
            print(f'{valor_peso} Quilograma(s) equivalem a {resultado} Grama(s).')
        elif escolha_peso == '6':
            resultado = valor_peso * 1000000
            print(f'{valor_peso} Quilograma(s) equivalem a {resultado} Miligrama(s).')
        elif escolha_peso == '7':
            resultado = valor_peso / 1000000
            print(f'{valor_peso} Grama(s) equivalem a {resultado} Tonelada(s).')
        elif escolha_peso == '8':
            resultado = valor_peso / 1000
            print(f'{valor_peso} Grama(s) equivalem a {resultado} Quilograma(s).')
        elif escolha_peso == '9':
            resultado = valor_peso * 1000
            print(f'{valor_peso} Grama(s) equivalem a {resultado} Miligrama(s).')
        elif escolha_peso == '10':
            resultado = valor_peso / 1000000
            print(f'{valor_peso} Miligrama(s) equivalem a {resultado} Tonelada(s).')
        elif escolha_peso == '11':
            resultado = valor_peso / 1000
            print(f'{valor_peso} Miligrama(s) equivalem a {resultado} Quilograma(s).')
        elif escolha_peso == '12':
            resultado = valor_peso / 1000
            print(f'{valor_peso} Miligrama(s) equivalem a {resultado} Grama(s).')
        elif escolha_peso == '13':
            resultado = valor_peso * 2204.62
            print(f'{valor_peso} Tonelada(s) equivalem a {resultado} Libra(s).')
        elif escolha_peso == '14':
            resultado = valor_peso * 2.20462
            print(f'{valor_peso} Quilograma(s) equivalem a {resultado} Libra(s).')
        elif escolha_peso == '15':
            resultado = valor_peso / 453.592
            print(f'{valor_peso} Grama(s) equivalem a {resultado} Libra(s).')
        elif escolha_peso == '16':
            resultado = valor_peso / 453592
            print(f'{valor_peso} Miligrama(s) equivalem a {resultado} Libra(s).')
        elif escolha_peso == '17':
            resultado = valor_peso * 0.453592
            print(f'{valor_peso} Libra(s) equivalem a {resultado} Tonelada(s).')
        elif escolha_peso == '18':
            resultado = valor_peso * 0.453592
            print(f'{valor_peso} Libra(s) equivalem a {resultado} Quilograma(s).')
        elif escolha_peso == '19':
            resultado = valor_peso * 453.592
            print(f'{valor_peso} Libra(s) equivalem a {resultado} Grama(s).')
        elif escolha_peso == '20':
            resultado = valor_peso * 453592
            print(f'{valor_peso} Libra(s) equivalem a {resultado} Miligrama(s).')
        else:
            print('Operação inválida.')

print('Calculadora encerrada.')
