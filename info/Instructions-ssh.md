# Gerar chave SSH
ssh-keygen -t ed25519 -C "phd.esantos@gmail.com"

# Ativar agente SSH e adicionar chave
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copiar chave pública
cat ~/.ssh/id_ed25519.pub

# Testar conexão
ssh -T git@github.com

# Alterar URL remota para SSH
git remote add origin git@github.com:ezequiasue/senai-leaning.git

git remote set-url origin git@github.com:ezequiasue/senai-leaning.git # Atualiza o remote ja existente
