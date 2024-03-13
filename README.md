# COMO INICIAR O PROJETO EM AMBIENTE VIRTUAL!

  ### Abrir o terminal cmd do Visual Studio Code e executar o comando:
    python -m venv nome_do_projeto  
  ### Executar o comando e entrar no diretorio do nome_do_projeto:
    * Primeiro Comando
    .\nome_do_projeto\Scripts\Activate.ps1
    
    * Segundo Comando
    cd .\nome_do_projeto\
  ### Baixar o requirements.txt (no caso do AulaFlask) e colocar na pasta nome_do_projeto logo após executar o comando:
    pip install -r requirements.txt

# COMO EXECUTAR O REPOSITÓRIOS

  ### Procurar o arquivo chamado .env e alterar o nome do banco de dados
    DATABASE_URL=postgresql://postgres:postgres@localhost/(nome_do_banco_de_dados)

  ### Executar esses comandos em ordem para criação do banco de dados
    flask db init

    
  ### 
  ### 
  ### 

  
  ### Procurar o arquivo run.py e executar ele
