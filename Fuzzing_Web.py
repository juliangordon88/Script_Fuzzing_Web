import argparse # sirve para pasar pasametros a nuestro script
import requests # sirve para hacer peticiones http 
from tqdm import tqdm # sirve para generar una barra de progreso del script

parser = argparse.ArgumentParser(description='Script de fuzzing de directorios web')
parser.add_argument("url", type=str, help='Direccion URL a fuzzear')
parser.add_argument("diccionario", type=str, help='Archivo de palabras a fuzzear')
args = parser.parse_args()

with open (args.diccionario) as file:
    wordlist = file.read().splitlines()

try:

        barrita = tqdm(total=len(wordlist), desc="Progreso", unit="urls", dynamic_ncols=True)
        
        for linea in wordlist:
            url_completa = args.url + linea
            response = requests.get(url_completa)
            if response.status_code == 200:
                    tqdm.write(f"URL encontrada: {url_completa}")
            barrita.update(1)

        
except KeyboardInterrupt:
        print("\n Se ha interrumpido el script por pulstar Ctrl+C")
    

finally: 
        barrita.close()


