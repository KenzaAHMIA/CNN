from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_directory, wav_directory):
    """Convertit tous les fichiers mp3 d'un dossier en fichiers wav
    et les enregistre dans un dossier spécifié.
    """
    for mp3_file in os.listdir(mp3_directory):
        if mp3_file.endswith(".mp3"): # On ne traite que les fichiers .mp3
            mp3_path = os.path.join(mp3_directory, mp3_file) # On crée le chemin du fichier mp3
            wav_file = os.path.splitext(mp3_file)[0] + ".wav" # On récupère le nom du fichier sans l'extension
            wav_path = os.path.join(wav_directory, wav_file) # On crée le chemin du fichier wav
            audio = AudioSegment.from_mp3(mp3_path) # On charge le fichier mp3
            audio.export(wav_path, format="wav") # On exporte le fichier au format wav

# Utilisation de la fonction de conversion
mp3_directory = "../corpus/fr/sons_mp3"
wav_directory = "../corpus/fr/sons_wav"
convert_mp3_to_wav(mp3_directory, wav_directory)