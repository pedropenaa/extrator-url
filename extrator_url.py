class ExtratorURl:
    def __init__(self, url):
        self.url = url
    

    def sanatiza(url):
        if type(url) == str:
            return url.strip
        else:
            return ""



    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
    @property
    def url_base(self):
      indice_interrogacao = self.url.find("?")
      url_base = self.url[ :indice_interrogacao]
      return url_base

    @property
    def url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros  = self.url[indice_interrogacao + 1 : ]
        return url_parametros

    @property
    def valor_parametro(self, parametro_busca):
        indice_parametro    = self.url_parametros.find(parametro_busca)
        indice_valor        = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial  = self.url_parametros.find("&", indice_valor)

        if indice_e_comercial == -1:
            valor  = self.url_parametros[indice_valor : ]
        else: 
            valor = self.url_parametros[indice_valor : indice_e_comercial]
        
        return valor
