# Criando calendário. Importar biblioteca
import calendar

# Gera calendário do mês desejado
mes = int(input("Informe o número do mês desejado (mês 1 a 12): "))
ano = int(input("Informe o ano desejado: "))

if mes > 0 and mes <= 12:
    print(calendar.month(ano, mes))
else:
    print("Mês inválido.")