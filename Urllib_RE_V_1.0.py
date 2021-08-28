#!/usr/bin/env python
# coding: utf-8

# ## Expressões Regulares e Urllib3
# ---
# ### Extração de SubLinks
# 
# ---
# ### References
# > ##### [Urllib3](https://urllib3.readthedocs.io/en/stable/reference/index.html)
#  >##### [RE(Exppressões Regulares)](https://docs.python.org/3/library/re.html)
# 
# ##### [⚡️⚡️⚡️⚡️⚡️ Leia  - Robots.txt](https://pt.wikipedia.org/wiki/Protocolo_de_exclus%C3%A3o_de_rob%C3%B4s)

# In[ ]:


import urllib3
import re


# In[ ]:


class Get_links():
    '''
    links_list -> retorna os links extraídos
    ex.:
        variavel = Get_links() -> encapsulamento da classe
        variavel.links_list() --> imprimi os links extraídos
        
    '''
    def links_list(self,url):
        """
        url = string 
            ex:'http://www.site.com'
        """
    #Realizar conexões com os sites
        hosts = urllib3.PoolManager()
        
    
    # Recebe dados do host via GET
        
        html = hosts.request('GET',url)
    
    # Verifica o Status da conexão
        if html.status == 200:
            print('Conexão realizada com sucesso!!')
        else:
            print(f'Conexão retornou:{html.status}')
        
    # Extração dos links e armazenamento na variável
        armazena = set() # armazena dados não repetidos
        links = re.findall('."(htt.*?)"',str(html.data))  
        for x in links:
            if not " " in x: # Exclui links com espaço em branco
                armazena.add(x)
    
    # Retorna os Links extraídos
    
        return armazena
    


# In[ ]:


# Imprimir os Links
dados = Get_links()


# In[ ]:


url = 'http://www.sorria.com.br'
subLinks = dados.links_list(url)


# In[ ]:


# Impressão dos Links encontrados
for x in subLinks:
    print(x)


# In[ ]:


# Quantidade de Links
print(f'Foran localizados {len(subLinks)} link(s)!')


# In[ ]:




