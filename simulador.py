while True:
    print("---------------------------------")
    print("  Seja bem-vindo(a) ao MyBank  ")
    print("   SIMULADOR DE INVESTIMENTO   ")
    print("---------------------------------")

    print("Títulos disponíveis para seu investimento:")
    print("1 - Tesouro PREFIXADO 2024")
    print("2 - Tesouro PREFIXADO 2026")

    titulo = int(input("Escolha um título: "))
    v_ir = 0
    ano24 = 32
    ano26 = 50
    val1 = float(input("\n Valor inicial: "))
    val2 = float(input("Valor investido mensalmente: "))

    if titulo == 1:

        resultado = val2 * ano24 + val1

        val3 = resultado * 12.33/100
        b3 = resultado * 2.5/100
        valbruto = resultado + val3 + b3
        print(f"\n {valbruto}")

#imposto de 7,5%
        if valbruto > 1903.98 and valbruto < 2826.66:
            ir = valbruto * 7.5/100
            v_ir = valbruto + ir

#imposto de 15%
        elif valbruto> 2826.65 and valbruto < 3751.06:
            ir = valbruto * 15/100
            v_ir = valbruto + ir

        #imposto de 22,5%
        elif valbruto > 3751.05 and valbruto < 4664.69:
            ir = valbruto * 22.5/100
            v_ir = valbruto + ir

        # imposto de 27,5%
        elif valbruto > 4664.68:
            ir = valbruto * 27.5/100
            v_ir = valbruto + ir
        liquido = v_ir - ir - b3

    else:
        val1 = val2 * ano26 + val1
        val3 = resultado * 12.21/100
        b3 = resultado * 2.5/100
        valbruto = resultado + val3 + b3

#imposto de 7,5%
        if valbruto > 1903.98 and valbruto < 2826.66:
            ir = valbruto * 7.5/100
            v_ir = valbruto + ir

#imposto de 15%
        elif valbruto> 2826.65 and valbruto < 3751.06:
            ir = valbruto * 15/100
            v_ir = valbruto + ir

        #imposto de 22,5%
        elif valbruto > 3751.05 and valbruto < 4664.69:
            ir = valbruto * 22.5/100
            v_ir = valbruto + ir

        # imposto de 27,5%
        elif valbruto > 4664.68:
            ir = valbruto * 27.5/100
            v_ir = valbruto + ir
        liquido = v_ir - ir - b3
    print("------------------------------")
    print("    RESULTADO DA SIMULAÇÃO    ")
    print("------------------------------")
    print(f"Valor inicial: {val1}")
    if titulo == 1:
        print(f"Aportes de {val2}  por {ano24} meses")
    else:
        print(f"Aportes de {val2}  por {ano26} meses")
    print(f"Valor total investido {resultado}")
    print("------------------------------")
    print(f"Valor total: {v_ir}")
    print(f"I.R.: {ir}")
    print(f"Taxa da B3: {b3}")
    print(f"Valor líquido: {liquido}")
    print("------------------------------")
    opcao = str(input("\n Deseja continuar a simulação? [s/n]: "))
    if opcao == 'n':
        break
