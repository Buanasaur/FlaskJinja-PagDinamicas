from flask import Flask, render_template
from classes.curso import Curso

app = Flask (__name__)


@app.route('/')
def index():
    titulo = 'Página Inicial'
    conteudo = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut voluptatibus corrupti quis obcaecati adipisci natus modi totam officia voluptatum vero, recusandae sapiente, facilis delectus? Eum, laboriosam? Dolore unde exercitationem temporibus. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut voluptatibus corrupti quis obcaecati adipisci natus modi totam officia voluptatum vero, recusandae sapiente, facilis delectus? Eum, laboriosam? Dolore unde exercitationem temporibus.'
    return render_template("index.html", titulo=titulo, conteudo=conteudo)

@app.route('/cursos')
def curso():
    lista_de_cursos = ['Desenvolvimento Web', 'Programação Orientada a Objeto']
    return render_template("cursos.html", lista=lista_de_cursos)

@app.route('/cursos/<nome>')
def curso_por_nome(nome):
    if nome == 'devweb':
        info = Curso ("Desenvolvimento Web", "Disciplina que ensina a criação e manutenção de websites e aplicações que rodam na internet.")
        habilidades = ['HTML','CSS', 'JavaScript']
        return render_template("info_curso.html", nome_curso="Desenvolvimento Web", objeto=info, dificuldade=1, habilidades=habilidades)
    elif nome == 'poo':
        info = Curso ("Programação Orientada a Objetos","Disciplina que ensina paradigma de programação que organiza o software em torno de objetos.")
        habilidades = ['Dicionários','Tratamento de exeções', 'Classes','Herança']
        return render_template("info_curso.html", nome_curso="Programação Orientada a Objetos", objeto=info, dificuldade=2, habilidades=habilidades)
    else:
        return "Curso inexistente!"
    

if __name__ == '__main__':
    app.run()