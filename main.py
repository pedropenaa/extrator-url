from extrator_url import ExtratorURl

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

extrator_url = ExtratorURl(url)
  
valor_quantidade = extrator_url.valor_parametro("quantidade")
valor_quantidade = extrator_url.valor_parametro("moedaOrigem")
print(valor_quantidade)












