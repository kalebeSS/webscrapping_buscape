import requests
from bs4 import BeautifulSoup
import pandas as pd
import yagmail
import os

#link do site buscape a ser raspado
link = r'https://www.buscape.com.br/search?q=tv%20led%2050%20polegadas%204k'

response = requests.get(link)

if response.status_code == 200:
    #pegando o content da pagina para usar a biblioteca soup
    soup = BeautifulSoup(response.content, 'html.parser')

    #listas vazias para pegar as informações
    title_product = []
    price_product = []

    quantidade_produtos = soup.find_all('div', 'Hits_ProductCard__Bonl_')

    title = soup.find_all('h2', 'ProductCard_ProductCard_Name__U_mUQ')
    price = soup.find_all('p', 'Text_Text__ARJdp Text_MobileHeadingS__HEz7L')

    for i in range(len(quantidade_produtos)):
        title_product.append(title[i].text)
        price_product.append(price[i].text)

    #colocandos os dois valores adquiridos em uma lista zipada para facil manuseio
    dados = list(zip(title_product, price_product))
    
    df = pd.DataFrame(dados, columns=['Produto', 'Preço'])

    df.to_csv('produtos.csv', index=False, encoding='utf-8')

    print('Dados salvos')

    # Configurações do email
    email_usuario = 'seuemail@gmail.com'
    email_senha = 'sua senha gerada'

    # Conectando ao servidor SMTP usando yagmail
    yag = yagmail.SMTP(user=email_usuario, password=email_senha)

    #caminho do arquivo gerado
    caminho = os.getcwd()

    # Informações do email
    destinatario = 'Email do destinatario'
    assunto = 'Assunto a ser enviado'
    mensagem = 'Mensagem a ser escrita'
    anexo = os.path.join(caminho, 'produtos.csv')

    try:
        # Enviando email
        yag.send(to=destinatario, subject=assunto, contents=mensagem)
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar o email: {e}')

else:
    print('Erro na requisição')