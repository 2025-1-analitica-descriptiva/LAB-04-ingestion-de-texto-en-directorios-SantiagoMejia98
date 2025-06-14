# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import zipfile
import os
import glob
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    with zipfile.ZipFile("files/input.zip", 'r') as zip:
        zip.extractall("files")

    ruta_base = 'files/input'
    ruta_final = 'files/output'

    train_dataset = {
        'phrase' : [],
        'target' : []
        }
    test_dataset = {
        'phrase' : [],
        'target' : []
        }
    
    if os.path.exists(ruta_final):
        for file in glob.glob(f"{ruta_final}/*"):
            os.remove(file)
        os.rmdir(ruta_final)
    os.makedirs(ruta_final)  

    files = glob.glob(f"{ruta_base}/**/*", recursive=True)
    files = [f for f in files if os.path.isfile(f)]
    for file in files:
        etiqueta = os.path.basename(os.path.dirname(file))
        conjunto = os.path.basename(os.path.dirname(os.path.dirname(file)))
        with open(file, 'r', encoding="utf-8") as f:
            for linea in f:
                frase = linea.strip()
        if conjunto == "train":
            train_dataset["phrase"].append(frase)
            train_dataset["target"].append(etiqueta)
        else:
            test_dataset["phrase"].append(frase)
            test_dataset["target"].append(etiqueta)

    df_train = pd.DataFrame(train_dataset)
    df_test = pd.DataFrame(test_dataset)
    df_train.to_csv(os.path.join(ruta_final, "train_dataset.csv"), index=False, encoding="utf-8")
    df_test.to_csv(os.path.join(ruta_final, "test_dataset.csv"), index=False, encoding="utf-8")
    
pregunta_01()