# Atividade CI/CD com Python

Este projeto foi desenvolvido para uma atividade acadêmica utilizando Python, pytest e GitHub Actions. A atividade tinha como objetivo executar um teste automatizado e corrigir um erro que estava acontecendo durante a execução do projeto.

## O que foi feito

O projeto possui uma calculadora simples com as funções:

* `somar(a, b)`: realiza a soma de dois valores.
* `subtrair(a, b)`: realiza a subtração de dois valores.
* `multiplicar(a, b)`: realiza a multiplicação de dois valores.
* `dividir(a, b)`: realiza a divisão e não permite divisão por zero.

Também foi criado um teste para verificar se a função `somar` estava funcionando corretamente.

## Problema encontrado

Durante a execução do teste pelo GitHub Actions, apareceu um erro relacionado ao arquivo `app.py`.

O problema acontecia porque existia um arquivo chamado `app.py` dentro da pasta `tests`, e o Python estava confundindo esse arquivo com a pasta principal `app`, que contém o arquivo `calculadora.py`.

Por causa disso, o comando:

```python
from app.calculadora import somar
```

não conseguia encontrar corretamente o pacote `app`.

## Como o problema foi resolvido

Para resolver o problema, mantive o `app.py` que já tinha sido disponibilizado pelo professor, mas coloquei esse arquivo dentro de uma subpasta dentro de `tests`.

Com essa alteração, o Python deixou de confundir o arquivo `app.py` com a pasta `app` do projeto.

Depois disso, o teste conseguiu encontrar corretamente a função `somar` e foi executado pelo GitHub Actions.

## Teste

O teste utilizado foi:

```python
from app.calculadora import somar

def test_somar():
    resultado = somar(2, 3)

    assert resultado == 5
```

Para executar os testes, foi utilizado o **pytest**.

```bash
pytest -v
```

## GitHub Actions

Também foi utilizado o **GitHub Actions** para automatizar a execução dos testes.

O pipeline realiza as etapas de baixar o código, configurar o Python, instalar as dependências e executar os testes.

Depois da correção, os testes foram executados com sucesso e os dois jobs do GitHub Actions ficaram concluídos sem erros.

## Estrutura do projeto

```text
app/
├── __init__.py
└── calculadora.py

tests/
├── test_calculadora.py
└── test/
    └── app.py

.github/
└── workflows/
    └── cd-cd.yml
```

## Tecnologias utilizadas

* Python
* Pytest
* GitHub Actions
* GitHub
