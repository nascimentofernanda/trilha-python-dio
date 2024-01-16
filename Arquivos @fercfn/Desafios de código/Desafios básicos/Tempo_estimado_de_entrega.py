#Desafio
#Imagine que você está criando um aplicativo de entrega de comida e precisa informar ao usuário o tempo estimado de entrega de um restaurante. A mensagem deve conter o nome do restaurante e o tempo estimado de entrega em minutos.

#Entrada
#A entrada deverá receber os valores abaixo:

#nomeRestaurante (string): o nome do restaurante desejado.
#tempoEstimadoEntrega (number): o tempo estimado de entrega em minutos.
#Saída
#Deverá retornar uma mensagem (string) informando ao usuário o tempo estimado de entrega do restaurante. Por exemplo, para o restaurante Bar do Zinho com o tempo estimado de entrega sendo 20, imprima:

nome_restaurante = input()
tempo_estimado_entrega = int(input())

tempo_entrega = str(tempo_estimado_entrega)

mensagem=f"O restaurante {nome_restaurante} entrega em {tempo_entrega} minutos."
print(mensagem)

#TODO: Imprimir a saída no padrão definido no enunciado deste desafio.
#Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings.