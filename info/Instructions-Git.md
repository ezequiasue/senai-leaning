
## Passos para Configuração e Uso do Git

### 1ª Etapa - Configuração Inicial

Antes de começar a usar o Git, configure seu nome e e-mail. Essas informações serão associadas aos commits realizados.


git config --global user.name "Ezequias S. Santos"
git config --global user.email "phd.esantos@gmail.com"


### 2ª Etapa - Inicializando o Repositório Git

Com a configuração feita, inicie o repositório Git no diretório do projeto. Se o repositório já foi clonado ou iniciado, esse passo pode ser pulado.


git init


### 3ª Etapa - Verificando Branches

Antes de criar uma nova branch ou fazer modificações, verifique quais branches existem no seu repositório.


git branch


Se estiver utilizando o branch `master` (o padrão no Git até algumas versões atrás), recomenda-se renomeá-lo para `main`:


git branch -m master main


### 4ª Etapa - Conectando ao Repositório Remoto

Agora, é hora de conectar o repositório local ao repositório remoto no GitHub.

git remote add origin git@github.com:ezequiasue/senai-leaning.git


Ou, se você já tiver clonado o repositório, você pode pular esta etapa. Para clonar o repositório, use:


git clone git@github.com:ezequiasue/senai-leaning.git


### 5ª Etapa - Criando e Trabalhando em Branches

Agora, crie uma nova branch para trabalhar em suas alterações. A prática comum é usar uma branch chamada `development` para o desenvolvimento das funcionalidades.


git checkout -b development       # Cria e muda para a branch development


Depois de fazer alterações no código, adicione os arquivos ao índice e faça o commit:


git add .                          # Adiciona todos os arquivos modificados ao índice
git status                         # Verifica o status dos arquivos
git commit -m "Mensagem do commit"  # Faz o commit com uma mensagem descritiva


### 6ª Etapa - Enviando Alterações para o Repositório Remoto

Agora, envie as alterações da branch `development` para o repositório remoto.

git push origin development         # Empurra as alterações da branch development para o remoto


### 7ª Etapa - Trabalhando com a Branch Principal (main)

Quando terminar o trabalho na branch `development`, mude para a branch `main` e faça o merge das alterações da `development` nela.


git checkout main                  # Muda para a branch main
git merge development               # Faz o merge da branch development na branch main
git push origin main                # Empurra as alterações da branch main para o remoto


### 8ª Etapa - Continuando o Ciclo de Trabalho

Para continuar trabalhando, crie uma nova branch de desenvolvimento, faça suas alterações, e repita o ciclo de commit, push e merge conforme necessário.



### Observações Finais:

- **Mensagens de Commit**: Sempre escreva mensagens de commit claras e concisas, explicando o que foi alterado.
- **Branches**: A prática recomendada é manter a branch `main` sempre estável e usar branches de desenvolvimento para novas funcionalidades ou correções.
- **Comandos Redundantes**: O comando `git init` foi mencionado duas vezes, e o `git remote add origin` também apareceu de forma duplicada. Um desses passos pode ser removido se já tiver sido executado.


