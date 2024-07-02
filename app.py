import os

# Caminho para o diretório onde os arquivos .txt estão localizados
arquivos_txt = r'C:\Users\Cliente\Documents\rename-archive\nomes-texto\\'

# Inicializa um contador para renomear os arquivos
count = 0

# Lista todos os arquivos no diretório especificado
for arquivo in os.listdir(arquivos_txt):
    # Incrementa o contador a cada iteração
    count += 1

    # Constrói o caminho completo para o arquivo antigo
    nome_antigo = os.path.join(arquivos_txt, arquivo)

    # Constrói o novo nome para o arquivo
    nome_novo = os.path.join(arquivos_txt, f'boletos-pagar{count}.txt')

    # Renomeia o arquivo antigo para o novo nome
    try:
        os.rename(nome_antigo, nome_novo)
        print(f'Renomeado: {nome_antigo} -> {nome_novo}')
    except Exception as e:
        print(f'Erro ao renomear {nome_antigo}: {e}')

# Lista e imprime todos os arquivos no diretório após a renomeação
print('Arquivos no diretório após a renomeação:')
print(os.listdir(arquivos_txt))
