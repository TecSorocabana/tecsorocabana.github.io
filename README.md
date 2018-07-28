# Site colaborativo da TecSorocabana

TecSorocabana é a manifestação online de uma parcela da comunidade de
profissionais de tecnologia de Sorocaba.

## O Site

Atualmente o site colaborativo da TecSorocabana é um projeto Pelican.
Resumidamente o Pelican é um gerador de sites estáticos escrito em Python onde o
usuário pode escrever o conteúdo em arquivos de marcação e o Pelican gera os
arquivos estáticos (HTML) do site. Para saber mais consulte o [site oficial do
Pelican](https://getpelican.com).

## Como contribuir publicando

* Faça um fork desse repositório.
* Crie a sua publicação em formato [Markdown](https://en.wikipedia.org/wiki/Markdown) ou [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) dentro
  do diretório `content`.
* Faça um pull request e acompanhe a revisão / aprovação da sua publicação.

### Markdown

Caso tenha dificuldades para escrever Markdown, veja esses editores online que
auxiliam sua escrita:

* [StackEdit](https://stackedit.io/app).
* [Dillinger](https://dillinger.io).

## Como contribuir desenvolvendo

A maior parte do trabalho, considerando a geração dos arquivos estáticos, é
realizada pelo próprio Pelican. O que resta é o desenvolvimento do frontend do
site através do sistema de templates utilizado pelo Pelican, o
[Jinja2](http://jinja.pocoo.org/) e o tradicional HTML, CSS e Javascript.

Para ter o projeto rodando na própria máquina é necessário ter o Python
instalado. Após isso siga os passos:

* Faça um fork desse repositório.
* Clone o fork para a sua própria máquina.
* Instale as dependências do projeto. Dentro do diretório clonado execute `pip
  install -r requirements.txt`.
* Rode o projeto com o comando `make serve html && make serve`. Esse comando irá
  executar dois passos definidos no arquivo `Makefile`. Leia-o para saber mais.
  O site pode ser acessado então localmente através do endereço
  `http://localhost:8000`. Para encerrar a execução do servidor local basta
  interromper o processo com `Ctrl - C`.
* Todo o template do site fica no diretório `themes/pelican-alchemy/alchemy`.
  Trata-se, basicamente, do projeto
  [pelican-alchemy](https://nairobilug.github.io/pelican-alchemy/) com pequenos
  ajustes. O template utiliza Bootstrap. Para mais informações acesse o site
  oficial ou o repositório do projeto.
* Faça a alteração desejada e execute novamente `make html && make serve` para
  visualizar o resultado.
* Após concluído, faça um pull request e acompanhe a revisão / aprovação da sua
  contribuição.
