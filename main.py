import os
import logging
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound

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
        
        # Lire le fichier audio
        playsound(file_path)
        messagebox.showinfo("Succès", "Conversion réussie et fichier audio lu.")
        
    except Exception as e:
        logging.error(f"Erreur lors de la conversion du texte en parole : {e}")
        messagebox.showerror("Erreur", f"Erreur lors de la conversion du texte en parole : {e}")

# Fonction appelée lorsque l'utilisateur clique sur le bouton "Convertir"
def convert_text():
    texte = text_input.get("1.0", END).strip()
    langue = language_input.get()
    if texte:
        text_to_speech(texte, langue)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer du texte.")

# Interface graphique avec Tkinter
root = Tk()
root.title("Convertisseur Texte en Parole")
root.geometry("500x400")
root.config(bg="#f4f4f4")

# Cadre principal
frame = Frame(root, bg="#ffffff", bd=2, relief=SOLID)
frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=450, height=350)

# Titre
title_label = Label(frame, text="Convertisseur Texte en Parole", font=("Helvetica", 16, "bold"), bg="#ffffff", fg="#333")
title_label.pack(pady=20)

# Étiquette pour le champ texte
text_label = Label(frame, text="Entrez le texte à convertir :", font=("Helvetica", 12), bg="#ffffff")
text_label.pack(pady=5)

# Zone de texte
text_input = Text(frame, height=5, width=40, font=("Helvetica", 10), bd=2, relief=SOLID)
text_input.pack(pady=5)

# Étiquette pour le choix de la langue
language_label = Label(frame, text="Choisissez la langue (ex : 'fr' pour Français) :", font=("Helvetica", 12), bg="#ffffff")
language_label.pack(pady=5)

# Champ pour entrer le code langue
language_input = Entry(frame, width=10, font=("Helvetica", 10), bd=2, relief=SOLID)
language_input.pack(pady=5)
language_input.insert(0, 'en')  # Valeur par défaut

# Bouton pour convertir
convert_button = Button(frame, text="Convertir", command=convert_text, font=("Helvetica", 12), bg="#4CAF50", fg="white", bd=0, relief=RAISED, padx=10, pady=5, cursor="hand2")
convert_button.pack(pady=20)

# Lancer l'interface graphique
root.mainloop()
