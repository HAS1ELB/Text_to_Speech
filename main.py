from gtts import gTTS
from playsound import playsound
import os
import logging

# Configurer le logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fonction pour convertir du texte en parole
def text_to_speech(text, lang='en'):
    try:
        # Création de l'objet gTTS
        tts = gTTS(text=text, lang=lang)
        
        # Définir le chemin du fichier audio
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        file_path = os.path.join(output_dir, "speech.mp3")
        
        # Sauvegarder le fichier audio
        tts.save(file_path)
        logging.info(f"Le fichier audio est sauvegardé à : {file_path}")
        print(f"Le fichier audio est sauvegardé à : {file_path}")
        
        # Lire le fichier audio
        playsound(file_path)
        
    except Exception as e:
        logging.error(f"Erreur lors de la conversion du texte en parole : {e}")
        print(f"Erreur lors de la conversion du texte en parole : {e}")

# Point d'entrée principal du script
if __name__ == "__main__":
    try:
        # Demander à l'utilisateur d'entrer un texte et la langue
        texte = input("Entrez le texte que vous voulez convertir en parole : ")
        langue = input("Entrez le code de la langue (par défaut 'en' pour l'anglais) : ") or 'en'
        
        # Appeler la fonction pour convertir le texte en parole
        text_to_speech(texte, langue)
    
    except KeyboardInterrupt:
        print("\nExécution interrompue par l'utilisateur.")
        logging.info("Exécution interrompue par l'utilisateur.")
