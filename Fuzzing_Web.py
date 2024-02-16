import argparse # sirve para pasar pasametros a nuestro script
import requests # sirve para hacer peticiones http 
from tqdm import tqdm # sirve para generar una barra de progreso del script

parser = argparse.ArgumentParser(description='Script de fuzzing de directorios web')
parser.add_argument("url", type=str, help='Direccion URL a fuzzear')
parser.add_argument("wordlist", type=str, help='Archivo de palabras a fuzzear')
args = parser.parse_args()

