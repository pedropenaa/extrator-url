from extrator_url import ExtratorURl

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

extrator_url = ExtratorURl(url)
print(extrator_url)
valor_quantidade = extrator_url.valor_parametro("quantidade")
#print(valor_quantidade)












