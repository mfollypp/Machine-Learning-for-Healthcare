# Machine-Learning-for-Healthcare
Repositório para a optativa Tópicos II em IA (ML aplicada a saúde)

## Para executar qualquer atividade basta ter uma versão do Python >=3.4 instalada (pois já vem com pip) e realizar os seguintes passos:
0. Clone esse repositório na sua máquina
1. Entre no diretório principal do repositório `.\Machine-Learning-for-Healthcare`
2. Abra um terminal, digite `python -m venv ambiente_virtual` e de enter
    * Isso vai criar um ambiente virtual para instalar as bibliotecas do python sem conflitar com as suas do computador
3. Agora digite `.\ambiente_virtual\Scripts\activate` e de enter 
    * Note que no terminal vai ter algo como `(ambiente_virtual) C:\Users\seu_user\...`, isso quer dizer que foi ativado com sucesso
4. Agora digite `pip install -r requirements.txt` e de enter
    * Ele vai instalar todas as bibliotecas/dependências necessárias para o projeto
5. Agora basta escolher qual atividade deseja executar o python
    * Para a Atividade 1 seria acessar o diretório `cd '.\Atividade 1'` e executar `python regressao_logistica.py`
> Obs.: Para a Atividade 1, caso deseje gerar novas imagens execute `python regressao_logistica.py --generate-images` ou troque o `--generate-images` por `-g`