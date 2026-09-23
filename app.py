from flask import Flask, render_template

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")

# Conteúdo da página — edite aqui para atualizar os textos sem mexer no HTML
CONTEXT = {
    "nome": "Carlos Alexandria",
    "cargo": "Desenvolvedor Web",
    "slogan": "Transformo ideias em sites reais, funcionais e profissionais.",
    "titulo": "Desenvolvimento de Sites e Sistemas Web",
    "descricao": (
        "Sites modernos, responsivos e sob medida para o seu negócio "
        "ou projeto pessoal."
    ),
    "frase_lateral": "Seu projeto, com qualidade e compromisso.",
    "servicos": [
        {
            "icone": "monitor",
            "titulo": "Sites institucionais",
            "texto": "Apresente sua marca na internet",
        },
        {
            "icone": "code",
            "titulo": "Landing pages",
            "texto": "Mais conversão para o seu negócio",
        },
        {
            "icone": "gear",
            "titulo": "Sistemas web personalizados",
            "texto": "Automatize e facilite seus processos",
        },
        {
            "icone": "phone",
            "titulo": "Sites responsivos",
            "texto": "Funcionam perfeitamente em qualquer dispositivo",
        },
        {
            "icone": "wrench",
            "titulo": "Manutenção e melhorias",
            "texto": "Seu site sempre atualizado",
        },
    ],
    "cta_texto": "Acesse meu portfólio",
    "cta_botao": "Ver meu site",
    "cta_link": "https://carloliveira1212.github.io/Portfolio-carlos-alexandria/",
    "cta_nota": "Meu portfólio mostra meus projetos, habilidades e mais sobre o meu trabalho.",
    "selos": [
        {"icone": "code", "texto": "HTML5, CSS3 e JavaScript"},
        {"icone": "layers", "texto": "Design limpo e funcional"},
        {"icone": "shield", "texto": "Código organizado e seguro"},
        {"icone": "bolt", "texto": "Entrega no prazo"},
    ],
    "curriculo": {
        "nome_completo": "Carlos Alexandria de Oliveira",
        "formacao": "Técnico em Informática, EEEP José de Barcelos (cursando)",
    },
}


@app.route("/")
def index():
    return render_template("index.html", **CONTEXT)


if __name__ == "__main__":
    app.run(debug=True)
