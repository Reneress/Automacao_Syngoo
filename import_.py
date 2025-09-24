from config import pasta
import zipfile
import os
import glob
import shutil

def executar_import():
    # Procurar arquivos .zip dentro da pasta "pasta"
    # Procurar especificamente pelo ZIP desejado
    zip_files = glob.glob(os.path.join(pasta, "relatorio-de-variaveis-*.zip"))

    if zip_files:
        zip_path = zip_files[0]  # pega o primeiro que bater com o padrão
        print("Arquivo encontrado:", zip_path)

        # Pasta de destino
        dest_folder = "arquivos"
        os.makedirs(dest_folder, exist_ok=True)

        # Extrair o conteúdo do ZIP
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dest_folder)

        # Listar arquivos extraídos
        arquivos_extraidos = os.listdir(dest_folder)
        print("Arquivos extraídos:", arquivos_extraidos)

        if arquivos_extraidos:
            origem = os.path.join(dest_folder, arquivos_extraidos[0])
            destino = os.path.join(dest_folder, "notas.xlsx")
            shutil.move(origem, destino)
            print(f"Arquivo renomeado para: {destino}")
    else:
        print("Nenhum arquivo ZIP com o nome esperado encontrado.")


# executar_import()