print ("Campanha de Conscientização Ambienteal!")

tipo_imovel = (input("Digite qual o seu tipo de imóvel (casa, comercio ou apartamento): "))
consumo_agua = float(input("Digite qual o seu consumo mensal de água em m³: "))

if tipo_imovel == "comercio": 
    print ("Tarifa comercial aplicada. Consulte o plano corporativo!")
elif tipo_imovel == "apartamento" and consumo_agua < 10:
    print ("Consumo econômico - excelente controle de água!")
elif (tipo_imovel == "apartamento" or "casa") and consumo_agua <= 25:
    print ("Consumo moderado - dentro do padrão residencial.")
else:
    print ("Consumo excessivo - adote medidas de economia e verifique vazamentos.")





