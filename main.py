
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"


#Separa a base e os parâmentros 
indice_interrogacao = url.find("?")
url_base            = url[ :indice_interrogacao]
url_parametros      = url[indice_interrogacao + 1 : ]


#Busca o valor de um parâmetro
parametro_de_busca  = "moedaOrigem"
indice_parametro    = url_parametros.find(parametro_de_busca)
tamanho_parametro   = len(parametro_de_busca)
indice_valor        = indice_parametro + tamanho_parametro + 1
indice_e_comercial  = url_parametros.find("&", indice_valor)

if indice_e_comercial == -1:
   valor  = url_parametros[indice_valor : ]
else: 
   valor = url_parametros[indice_valor : indice_e_comercial]


print(valor)










