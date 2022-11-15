init python:

    # Módulos para manipulação de arquivos .zip
    import zipfile
    import zlib

    # Módulo para manipulação de recursos do SO
    import os

    # Caminho para o diretório em que será manipulado os arquivos .zip
    txt = open(renpy.loader.transfn("images/zips_path.txt"), "r")

    # Troque para o diretório informado
    os.chdir(str(txt.name).replace("zips_path.txt", ""))

    # Função que cria um arquivo .zip, onde precisamos passar um nome para o zip, o prefixo da imagem e a quantidade
    def compress(zip_name, image_prefix, image_range):
        # Crie o .zip em modo leitura com o tipo de compressão ZIP_DEFLATED
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

        # Pegue a referência do .zip em modo leitura
        zip = zipfile.ZipFile(zip_name + ".zip", "r")

        # Extraia tudo que está dentro desse .zip
        zip.extractall()

        # Feche o .zip
        zip.close()

        # Delete o .zip, pois não precisamos mais dele
        os.remove(zip_name + ".zip")

    # Função para verificar se um arquivo .zip existe, precisando informar o nome do .zip
    def zip_exists(zip_name):
        return zipfile.is_zipfile(zip_name)
