import os
import pyaes


## pega todos os arquivos do diretório teste
arquivos = os.listdir("./teste")
##Looping dos arquivos
for arquivo in arquivos:
    filename, file_extension = os.path.splitext(arquivo)
    file_name= "./teste/" + str(filename +file_extension)
    
    ## abrir o arquivo criptografado
    file_name = file_name
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    ## chave para descriptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    ## remover o arquivo criptografado
    os.remove(file_name)

    ## criar o arquivo descriptografado
    new_file = "./teste/" +str(filename)+".txt"
    new_file = open(f'{new_file}', "wb")
    new_file.write(decrypt_data)
    new_file.close()
