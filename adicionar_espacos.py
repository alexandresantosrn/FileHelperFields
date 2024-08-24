# Definir o número de colunas desejadas
colunas_desejadas = 176

# Abra o arquivo de entrada e leia o conteúdo linha por linha
with open('arquivo_entrada.txt', 'r') as file:
    linhas = file.readlines()

# Abra o arquivo de saída para escrever o conteúdo modificado
with open('arquivo_saida.txt', 'w') as file:
    for linha in linhas:
        # Remove espaços em branco à direita e ajusta o comprimento da linha
        linha = linha.rstrip()
        if len(linha) < colunas_desejadas:
            # Adiciona espaços até completar 177 colunas
            linha = linha + ' ' * (colunas_desejadas - len(linha))
        file.write(linha + '\n')

