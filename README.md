# Mago Games - Back-end

## Descrição do site:

#### O mago games é um site de consulta dos melhores preços e promoções do mundo dos jogos. Nele é possível ver e pesquisar jogos e suas promoções em uma série de lojas.

## API utilizada:
#### Para o desenvolvimento do Mago Games a seguinte API foi utilizada: 
* https://apidocs.cheapshark.com/ 

## API Rest desenvolvida:
#### Para o Mago Games, foi desenvolvida uma API REST em Django, com as seguintes urls: 
* externalAPI/home (GET - retorna as ofertas mostradas na página inicial)
* externalAPI/store (GET - retorna as lojas das ofertas mostradas)
* externalAPI/gameLookup/<int:id> (GET - retorna as informações de um jogo específico)
* externalAPI/dealLookup/<slug:deal> (GET - retorna as informações de uma oferta específico)
* externalAPI/search/<str:title> (GET - retorna as ofertas de um jogo específico sem restrição de preço)
* externalAPI/search/min/<str:title>/<int:minprice> (GET - retorna as ofertas de um jogo específico com restrição de preço minímo)
* externalAPI/search/max/<str:title>/<int:maxprice> (GET - retorna as ofertas de um jogo específico com restrição de preço máximo)
* externalAPI/search/min/<int:minprice> (GET - retorna as ofertas com restrição de preço mínimo)
* externalAPI/search/max/<int:maxprice> (GET - retorna as ofertas com restrição de preço máximo)
* externalAPI/search/<int:minprice>/<int:maxprice> (GET - retorna as ofertas com restrição de preço mínimo e máximo)
* externalAPI/search/<str:title>/<int:minprice>/<int:maxprice> (GET - retorna as ofertas de um jogo específico com restrição de preço mínimo e máximo)
* API/register/ (POST - cria um novo usuário no banco de dados)
* API/login/ (POST - faz o login de um usuário)
* API/logout/ (POST - faz o logout de um usuário)
* API/favorite/<str:user_name>/ (GET - retorna uma lista dos favoritos daquele usuário salvos no banco de dados)
* API/favorite (POST - posta um favorito ligado a um usuário)

## Uso da API no backend:
#### Foram criadas urls no backend para utilizar a API cheapshark por conta de um erro ao tentar realizar as requisições no frontend. Dessa forma, conversamos com a professora Barbara e ela nos indicou essa solução.  

## Acesso ao backend:
#### É possível acessar o site na seguinte url:
* https://magogames-backend.herokuapp.com/

## Alunos:
* José Rafael Martins Fernandes
* Lucca Barufatti Velini Sanches
