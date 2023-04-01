<!--
# Boas-vindas ao repositório do projeto `Restaurant Orders`!

Para realizar o projeto, atente-se a cada passo descrito a seguir, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir deste repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

# Termos e acordos

Ao iniciar este projeto, você concorda com as diretrizes do Código de Conduta e do Manual da Pessoa Estudante da Trybe.

# Entregáveis

<details>
  <summary><strong>🤷🏽‍♀️ Como entregar</strong></summary><br />

  Para entregar o seu projeto você deverá criar um *Pull Request* neste repositório.

  Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://app.betrybe.com/course/4d67f5b4-34a6-489f-a205-b6c7dc50fc16/) e nosso [Blog - Git & GitHub](https://blog.betrybe.com/tecnologia/git-e-github/) sempre que precisar!
</details>

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />
A lanchonete :baguette_bread: :cook: Pão na Chapa :baguette_bread: :cook: possui um sistema de faturamento de pedidos de clientes que salva o nome da pessoa, o pedido realizado e o dia da semana do atendimento. A gerência da lanchonete quer aumentar suas vendas e melhorar sua gestão interna e, para isso, te contratou para implementar um projeto de melhorias, o Projeto `Restaurant Orders`. </br>
    Em um primeiro momento (requisitos obrigatórios), você deverá atuar para que o sistema gere relatórios com informações sobre os pedidos e as pessoas clientes que frequentam a lanchonete. Estes dados irão auxiliar o trabalho de uma agência de marketing com o objetivo de alavancar as vendas e o número de pessoas clientes. </br>
    Em um segundo momento (requisitos bônus), o foco do projeto deverá ser o controle do estoque de ingredientes para garantir que o cardápio digital da :baguette_bread: :cook: Pão na Chapa :baguette_bread: :cook: sempre ofereça produtos que estão disponíveis no estoque, evitando frustrações por parte das pessoas clientes. </br>
    O projeto está estruturado em duas etapas obrigatórias e duas etapas bônus, totalizando 4 requisitos. Foque nas etapas obrigatórias e resolva o projeto com o mesmo cuidado que teria com um cliente real: *código limpo, com boa manutenção e legibilidade. </br>
</br>
🚵 Habilidades exercitadas: </br>
  - Trabalhar com `Hashmap` e `Dict` e; </br>
  - Trabalhar com `Set`. </br>

</details>

<details>
  <summary><strong>🗓 Data de Entrega</strong></summary><br />
  
  * Este projeto é `individual`;
  * Serão `1` dias de projeto;
  * Data para entrega no prazo regular: `17/02/2023 14:00`.

</details>

# Orientações
<details>
  <summary><strong>⚠️ Antes de começar a desenvolver</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-020-a-restaurant-orders.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-0x-project-restaurant-orders`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `master`

  - Verifique que você está na branch `master`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `master`
    - Exemplo: `git checkout master`
  - Crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-de-usuario-nome-do-projeto`
    - Exemplo: `git checkout -b joaozinho-sd-0x-project-restaurant-orders`

  5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

  - Verifique que as mudanças ainda não estão no _stage_
    - Exemplo: `git status` (deve aparecer listada a pasta _joaozinho_ em vermelho)
  - Adicione o novo arquivo ao _stage_ do Git
    - Exemplo:
      - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
      - `git status` (deve aparecer listado o arquivo _joaozinho/README.md_ em verde)
  - Faça o `commit` inicial
    - Exemplo:
      - `git commit -m 'iniciando o projeto x'` (fazendo o primeiro commit)
      - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

  6. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin joaozinho-sd-0x-project-restaurant-orders`

  7. Crie um novo `Pull Request` _(PR)_

  - Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-project-restaurant-orders/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  - Coloque um título para a sua _Pull Request_
    - Exemplo: _"Cria tela de busca"_
  - Clique no botão verde _"Create pull request"_
  - Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  - **Não se preocupe em preencher mais nada por enquanto!**
  - Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-project-restaurant-orders/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><strong>⌨️ Durante o desenvolvimento</strong></summary><br />

  - Faça `commits` das alterações que você fizer no código regularmente

  - Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

  - Os comandos que você utilizará com mais frequência são:
    1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
    2. `git add` _(para adicionar arquivos ao stage do Git)_
    3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
    4. `git push -u origin nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
    5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_

</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />

  No diretório `src/` você vai encontrar os arquivos em que devem ser implementadas todas as classes e métodos que você considerar importantes para resolver cada etapa do projeto.

  No diretório `data/` você vai encontrar os arquivos de log que deverão ser utilizados em cada etapa.

  Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  .
  ├── data
  │   ├──🔸 orders_1.csv
  │   └──🔸 orders_2.csv
  ├── src
  │   ├──🔹 analyze_log.py
  │   ├──🔹 inventory_control.py
  │   ├──🔹 main.py
  │   └──🔹 track_orders.py
  ├──tests
  │   ├──🔸 test_analyze_log.py
  │   ├──🔸 test_inventory_control.py
  │   └──🔸 test_track_orders.py
  ├──🔸 dev-requirements.txt
  ├──🔸 pyproject.toml
  ├──🔸 README.md
  ├──🔸 requirements.txt
  ├──🔸 setup.cfg
  ├──🔸 setup.py
  └──🔸 trybe.yml

Legenda:
  🔸 Arquivos que não podem ser alterados.
  🔹 Arquivos a serem alterados para realizar os requisitos.
```

  Na estrutura deste _template_, você deve implementar as funções necessárias. Novos arquivos e funções podem ser criados conforme a necessidade da sua implementação, porém não remova arquivos já existentes.
</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

  ⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS. ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

  ```bash
  pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>

<details>
  <summary><strong>🤝 Depois de terminar o desenvolvimento (opcional)</strong></summary><br />

  Para sinalizar que o seu projeto está pronto para o _"Code Review"_, faça o seguinte:

  - Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

    - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

    - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

    - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-020-a`.

  Caso tenha alguma dúvida, veja o [video explicativo](https://vimeo.com/362189205).

</details>

<details>
  <summary><strong>🕵🏿 Revisando um pull request</strong></summary><br />

  Use o conteúdo sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os _Pull Requests_.
</details>

<details>
  <summary><strong>🗣 Nos dê feedbacks sobre o projeto!</strong></summary><br />

Ao finalizar e submeter o projeto, não se esqueça de avaliar sua experiência preenchendo o formulário. 
**Leva menos de 3 minutos!**

[FORMULÁRIO DE AVALIAÇÃO DE PROJETO](https://be-trybe.typeform.com/to/ZTeR4IbH)

</details>

<details>
  <summary><strong>🗂 Compartilhe seu portfólio!</strong></summary><br />

  Agora que você finalizou os requisitos, chegou a hora de mostrar ao mundo que você aprendeu algo novo! 🚀

  Siga esse [**guia que preparamos com carinho**](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/a3cac6d2-5060-445d-81f4-ea33451d8ea4/section/d4f5e97a-ca66-4e28-945d-9dd5c4282085/day/eff12025-1627-42c6-953d-238e9222c8ff/lesson/49cb103b-9e08-4ad5-af17-d423a624285a) para disponibilizar o projeto finalizado no seu GitHub pessoal.

  Esse passo é super importante para ganhar mais visibilidade no mercado de trabalho, mas também é útil para manter um back-up do seu trabalho.

  E você sabia que o LinkedIn é a principal rede social profissional e compartilhar o seu aprendizado lá é muito importante para quem deseja construir uma carreira de sucesso? Compartilhe esse projeto no seu LinkedIn, marque o perfil da Trybe (@trybe) e mostre para a sua rede toda a sua evolução.

</details>

# Requisitos obrigatórios

## 1 - Campanha de publicidade

> Implemente um método chamado `analyze_log` no módulo `src/analyze_log.py` que gere informações de uma lanchonete.

A lanchonete quer promover ações de marketing e, para isso, a agência de publicidade precisa das informações abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi à lanchonete?

#### Dados

O atual sistema da lanchonete 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳  guarda os `logs` de todos os pedidos feitos em um arquivo _csv_, contendo o formato `cliente, pedido, dia`, um por linha e sem nome das colunas (a primeira linha já é um pedido).

O `log` a ser utilizado é o arquivo `data/orders_1.csv`. Todas as informações são _strings_ com letras minúsculas. O histórico contém pedidos feitos em todos os dias da semana que a lanchonete abre, e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio e agenda completos. Os dias da semana estão no formato `"...-feira", "sabado" ou "domingo"`, e **não nos interessa informações sobre os dias que a lanchonete não abre**.

#### Implementação

No arquivo `analyze_log.py`, escreva uma função que responda às seguintes perguntas abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi à lanchonete?

A função não retornará nada e deverá apenas salvar as respostas no arquivo `data/mkt_campaign.txt`, na mesma ordem das peguntas acima.

<details>
<summary><b>Clique aqui para ver a assinatura da função.</b></summary>

```python
def analyze_log(path_to_file):
    # Código vem aqui
```

</details>

<details>
<summary><b>Clique aqui para ver saída correta da função.</b></summary>

```
hamburguer
1
{'pizza', 'coxinha', 'misto-quente'}
{'sabado', 'segunda-feira'}
```
</details>

:eyes: _De olho na Dica:_ a ordem dos pedidos, bem como dos dias da semana não precisa ser exatamente a apresentada no exemplo.

- No arquivo `analyze_log.py` deve estar implementada a função `def analyze_log(path_to_file)`;

- A função deve realizar a leitura do `log` e salvar em um arquivo `txt` as informações solicitadas;

- Utilização correta de `Dict/Set`, vistos no módulo;

- Código legível e modularizado, quando for o caso.

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 1.1 - Será validado se, ao executar o método `analyze_log`, os dados são preenchidos de forma correta no arquivo `data/mkt_campaign.txt`;

- 1.2 - Será validado se, ao executar o método `analyze_log` com um arquivo inexistente, o método retorna um erro `FileNotFoundError` com a mensagem de erro abaixo:
  ```
  "Arquivo inexistente: '{nome_do_arquivo}'"
  ```
- 1.3 - Será validado se, ao executar o método `analyze_log` com uma extensão inválida, o método retorna um erro com a mensagem abaixo:
  ```
  "Extensão inválida: '{nome_do_arquivo}'"
  ```
</details>

## 2 - Análises contínuas

> Implemente a classe `TrackOrders` que gere informações contínuas da 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 .

A campanha de marketing foi um sucesso! A gerência da 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 deseja agora um sistema que mantenha um registro contínuo dessas informações. Mais especificamente, deseja que o sistema permita, a qualquer momento, a extração das seguintes informações:

- Prato favorito por cliente;

- Pratos nunca pedidos por cada cliente;

- Dias nunca visitados por cada cliente;

- Dia mais movimentado;

- Dia menos movimentado.

Para isso, você deverá implementar uma classe que entregue as informações acima.

#### Implementação

**Arquivos**

- Implemente a classe `TrackOrders` no arquivo `track_orders.py`;

- O arquivo `src/main.py` é apenas auxiliar e faz a leitura do arquivo `csv` especificado e envia, ao mesmo tempo, a informação de cada pedido para as classes `TrackOrders` e para a classe `InventoryControl`;

:eyes: _De olho na Dica:_ não se preocupe ainda com o arquivo `inventory_control.py` (classe InventoryControl), pois ele é necessário apenas para a realização dos requisitos bônus.

- No arquivo `src/main.py` algumas informações são impressas na tela para que você observe o comportamento das classes após a leitura completa do arquivo `csv`,


**Teste o comportamento do arquivo `main.py`**.

Abra o arquivo `main.py` e complete a variável _path_ com `data/orders_1.csv`. Rode o arquivo `main.py`. Quatro linhas de `None` devem ser impressas. Isso acontece, porque as funções não estão devidamente implementadas ainda.

**Implemente a solução**

<details>
<summary><b>No arquivo <code>track_orders.py</code>, implemente a classe <code>TrackOrders</code>. Clique aqui para ver os métodos que devem ser implementados.</b></summary>

```python
class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        pass

    def add_new_order(self, customer, order, day):
        pass

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
```

:eyes: _De olho nas Dicas:_ você é livre para criar os atributos e métodos necessários; crie uma classe legível e bem modularizada; não implemente funcionalidades que ainda não são necessárias, nem coloque atributos do tipo "vai que um dia precisa"; sempre rode o arquivo `main.py` para verificar o comportamento da sua classe.

</details>


- Classe `TrackOrders` implementada;

- A classe está devidamente modularizada;

- Os métodos fazem uso das técnicas de `Dict` e `Set` vistos no módulo;

- Os métodos atingem complexidade ótima (geralmente `O(1)` ou `O(n)`, em alguns métodos que usam `Set`).

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 2.1 - Será validado se, ao instanciar a classe `TrackOrders` pela primeira vez, o método `len()` retorna a quantidade de pedidos igual a zero;

- 2.2 - Será validado se, ao executar o método `add_new_order`, o método registra um pedido na instância;

- 2.3 - Será validado se, ao executar `get_most_ordered_dish_per_customer`, o método retorna o prato mais pedido;

- 2.4 - Será validado se, ao executar `get_never_ordered_per_customer`, o método retorna o conjunto de pratos que a pessoa nunca pediu;

- 2.5 - Será validado se, ao executar `get_days_never_visited_per_customer`, o método retorna o conjunto de dias que a pessoa nunca visitou;

- 2.6 - Será validado se, ao executar o método `get_busiest_day`, o método retorna o dia mais movimentado e;

- 2.7 - Será validado se, ao executar o método `get_least_busy_day`, o método retorna o dia menos movimentado.
</details>

---
# Requisitos bônus:

## 3 - Controle de estoque

Atualmente o controle de estoque de ingredientes da 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 é feito em um caderno. Ao final da semana, uma pessoa conta quantas unidades de cada ingrediente ainda restam no estoque e anota quantas unidades precisam ser compradas para completar o estoque mínimo de cada ingrediente.

A 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳  deseja automatizar esse controle: no final da semana, a gerência irá imprimir uma lista de compras com as respectivas quantidades.

#### Dados

O `log` a ser utilizado é o arquivo `data/orders_1.csv`. É garantido que os pedidos da semana não irão zerar nenhum dos estoques.

#### Implementação

No arquivo `inventory_control.py` você deve implementar a classe `InventoryControl` que retorna a lista de compras da semana, a partir da informação de cada pedido. É importante que a lista seja atualizada a cada pedido, e não apenas ao final de semana, pois a gerência quer ter a liberdade de imprimir a lista de compras a qualquer momento.

<details>
<summary><b>Clique aqui para ver a estrutura básica da classe. Lá já contém as informações dos ingredientes, bem como o estoque mínimo de cada um. O método <code>get_quantities_to_buy</code> deve retornar um <code>Dict</code> que mapeia o ingrediente para a quantidade a ser comprada.</b></summary>

```python
class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho', 'tomate'],
        'queijo-quente': ['pao', 'queijo', 'queijo'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'bauru': ['pao', 'queijo', 'presunto', 'tomate'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        pass

    def add_new_order(self, customer, order, day):
        pass

    def get_quantities_to_buy(self):
        pass
```

</details>

- Classe `InventoryControl` implementada;

- A classe está devidamente modularizada;

- Garanta que todos os ingredientes e pratos foram testados;

- Os métodos devem fazer uso das técnicas de `Dict` e `Set` vistos no módulo;

- Os métodos atingem complexidade ótima, geralmente `O(1)` ou `O(n)`, em alguns métodos que usam `Set`.

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 3.1 - Será validado se, ao executar o método `get_quantities_to_buy`, o método retorna a quantidade de ingredientes que precisam ser comprados;

- 3.2 - Será validado se, ao executar o método `get_quantities_to_buy` para todos os hambúrgueres, o método retorna a quantidade de ingredientes que precisam ser comprados;

- 3.3 - Será validado se, ao executar o método `get_quantities_to_buy` para receitas diferentes, o método retorna a quantidade de ingredientes que precisam ser comprados.
</details>

## 4 - Estoque pode acabar

As campanhas de marketing tiveram sucesso novamente e atraíram muitas novas pessoas clientes para a 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 . Se antes os estoques mínimos eram sempre suficientes para uma semana, agora não são mais.


<b>Suponha os seguintes estoques:</b>

```md
- Pao: 1;
- Queijo: 5;
- Presunto: 3.
```

Se uma pessoa pedir um misto-quente, será possível atendê-la. Porém o pão irá acabar. Se a próxima pessoa pedir hamburguer, não será possível atendê-la. Sua missão é implementar um código que, caso algum ingrediente acabe, todos os pratos que usam aquele ingrediente devem ser imediatamente removidos do cardápio eletrônico, evitando gerar frustração em clientes.

#### Dados

O `log` a ser utilizado é o arquivo `data/orders_2.csv`. Se quiser testar pelo arquivo `main.py`, não se esqueça de alterar a variável `path`.

#### Implementação

:eyes: _De olho na Dica:_ Você fez commit do requisito `3 - Controle de estoque`? Se não, faça, pois agora você vai alterar o seu código!

Implemente um novo método na classe `InventoryControl` que retorne um conjunto com todos os pratos disponíveis, ou seja, pratos que utilizam os ingredientes disponíveis em quantidade suficiente no estoque.


<details>
<summary><b>Clique aqui para ver a assinatura da função.</b></summary>

```python
def get_available_dishes():
    # retorno: um conjunto de pratos que ainda têm ingredientes disponíveis no estoque
```
</details>

Garanta que:

- O método `get_available_dishes` está implementado e funcionando corretamente;

- O método `add_new_order` retorne `False` para um pedido que não tem ingredientes disponíveis no estoque;

- As classes/métodos estão devidamente modularizadas;

- Os métodos fazem uso das técnicas de `Dict` e `Set` vistos no módulo.

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 4.1 - Será validado se, ao executar o método `add_new_order` para um pedido com prato que não possui ingrediantes suficientes em estoque, o método retorna `False` sem registrar o pedido;

- 4.2 - Será validado se, ao executar o método `get_available_dishes`, o método retorna todos os pratos que possuem ingredientes suficientes para seu preparo;

- 4.3 - Será validado se, ao executar o método `get_available_dishes`, o método não retorna os pratos cujos ingredientes não sejam suficientes para seu preparo.
</details>

---

-->