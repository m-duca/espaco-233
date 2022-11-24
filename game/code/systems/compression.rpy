init python:

    # Módulos para manipulação de arquivos .zip
    import zipfile
    import zlib

    # Módulo para manipulação de caminhos
    from pathlib import Path

    # Módulo para manipulação de recursos do SO
    import os

    # Caminho para o diretório em que será manipulado os arquivos .zip
    txt = open(renpy.loader.transfn("images/zips_path.txt"), "r")

    # Troque para o diretório informado
    os.chdir(str(txt.name).replace("zips_path.txt", ""))

    # Função que cria um arquivo .zip, onde precisamos passar um nome para o zip, o prefixo da imagem e a quantidade
    def compress(zip_name, image_prefix, image_range):
        if zip_exists(zip_name) == False:
            # Crie o .zip em modo escrita com o tipo de compressão ZIP_DEFLATED
            zip = zipfile.ZipFile(zip_name + ".zip", "w", compression=zipfile.ZIP_DEFLATED)

            # Adicione as imagens no .zip a partir da quantidade informada
            for i in range(0, image_range):
                zip.write(image_prefix + str(i) + ".png")

                # Delete a imagem original, pois não queremos mais ela
                os.remove(image_prefix + str(i) + ".png")

            # Feche o .zip
            zip.close()

    # Função que faz a descompressão de um arquivo .zip, onde precisamos passar o nome do .zip
    def decompress(zip_name):
        if zip_exists(zip_name) == True:
            # Pegue a referência do .zip em modo leitura
            zip = zipfile.ZipFile(zip_name + ".zip", "r")

            # Extraia tudo que está dentro desse .zip
            zip.extractall()

            # Feche o .zip
            zip.close()

            # Delete o .zip, pois não precisamos mais dele
            os.remove(zip_name + ".zip")

    # Função para verificar se um arquivo .zip existe
    def zip_exists(zip_name):

        # Usando a classe Path e o .txt de refêrencia para a pasta imagem, informamos o caminho do .zip
        zip_path = Path(str(txt.name).replace("zips_path.txt", zip_name + ".zip"))

        # Caso o arquivo realmente existir no caminho informado, irá então retornar True se não
        # retorne False
        return zip_path.is_file()
