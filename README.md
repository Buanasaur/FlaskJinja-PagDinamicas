# Criação de Páginas Dinâmicas com Flask e Jinja - Visão Geral

Atividade criada com o proposito de ensinar a criar paginas dinamicas usando o Flask, entender a diferença em renderização no servidor e no cliente, aprender a linguagem de templates Jinja e como usar sua tags.
O site contém uma interface básica e páginas dinâmicas de navegação

## Tecnologias Utilizadas
* Python
* HTML
* CSS

## Como Executar
Para visualizar este exercício, certifique-se de ter o Python e o Flask instalados.
Depois execute o arquivo principal `app.py`

## Elementos principais implementados
* Herança de Templates de uma estrutura básica do HTML (`base.html`) e das tags Jinja `{% extends %}`, `{% block %}` e `{% endblock %}`
* Estrutura básica de um documento HTML (`<html>`, `<head>`, `<body>`).
* Utilização de diferentes tags de texto (`<h1>`,`<h2>`,`<p>`)
* Criação de links de navegação entre as páginas (`<a>`)
* Renderização no Servidor com o Flask
    * Função render_template(): (`render_template("index.html", titulo=titulo, conteudo=conteudo)`).
    * Template tags (`{% templante tag %}`,`{{ valor }}`,`{{ lista[] }}`)
* Estruturas de Controle (`{% if %}`,`{% endif %}`)
* Estilos para a estrutura principal da página (`header`,`body`,`footer`).

## Exemplo de Herança de Template Filho (index.html):
```{% extends "base.html" %}

{% block titulo %}
    <title>Página Inicial</title>
{% endblock %}

{% block conteudo %}
    <h1>{{ titulo }}</h1>
    <p>{{ conteudo}} </p>
    <p>{{ conteudo}} </p>
{% endblock %}``` 


