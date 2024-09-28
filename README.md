
# Projet Text-to-Speech en Python avec Tkinter

## Description
Ce projet permet de convertir du texte en parole en utilisant la bibliothèque `gTTS` (Google Text-to-Speech), de lire le fichier audio généré avec `playsound`, et d'interagir avec une interface graphique créée à l'aide de `Tkinter`. L'application propose une interface simple permettant de saisir du texte, de choisir la langue de sortie et de générer un fichier audio.

## Fonctionnalités
- Conversion de texte en fichier audio (.mp3).
- Interface graphique améliorée avec Tkinter.
- Support multilingue (par exemple, anglais, français, espagnol).
- Lecture automatique du fichier audio généré.
- Journalisation des événements pour le suivi des opérations (logs).

## Prérequis
Avant d'exécuter ce projet, vous devez vous assurer que Python est installé sur votre machine. Vous pouvez télécharger Python [ici](https://www.python.org/downloads/).

### Bibliothèques Python nécessaires :
- **gTTS** (Google Text-to-Speech)
- **playsound** (pour lire le fichier audio)
- **Tkinter** (pour créer l'interface graphique)
- **logging** (intégré dans Python pour gérer les logs)

Vous pouvez installer ces bibliothèques en utilisant la commande suivante :

```bash
pip install -r requirements.txt
```

## Installation

1. **Cloner le projet :**
   Clonez le projet depuis un dépôt Git (ou téléchargez le dossier) :
   
   ```bash
   git clone <url-du-repo>
   cd text_to_speech_project
   ```

2. **Installer les dépendances :**
   Une fois le projet cloné, installez les dépendances avec `pip` :

   ```bash
   pip install -r requirements.txt
   ```

3. **Structure des fichiers :**
   Le projet doit être organisé de la manière suivante :
   ```
   text_to_speech_project/
   │
   ├── main.py               # Script principal avec Tkinter
   ├── README.md             # Documentation du projet
   ├── requirements.txt      # Liste des dépendances
   ├── output/               # Dossier pour stocker les fichiers audio générés
   │   └── speech.mp3
   └── logs/                 # Dossier pour stocker les logs
       └── app.log
   ```

## Utilisation

1. **Exécution du script :**
   Pour lancer l'application de conversion de texte en parole avec l'interface graphique, exécutez la commande suivante dans le terminal :

   ```bash
   python main.py
   ```

2. **Utilisation de l'interface :**
   - Saisissez le texte dans le champ prévu à cet effet.
   - Choisissez la langue de conversion (par défaut : anglais).
   - Cliquez sur "Convertir" pour générer et lire le fichier audio.

3. **Résultat :**
   Le fichier audio sera généré dans le dossier `output` et sera automatiquement lu après la conversion. Le chemin du fichier audio sera affiché dans le terminal.

   Exemple de sortie :
   ```
   Le fichier audio est sauvegardé à : output/speech.mp3
   ```

## Journalisation (Logs)

Le programme crée un fichier de log dans le répertoire `logs/app.log`, qui enregistre les événements comme la génération de fichiers ou les erreurs. Vous pouvez consulter ce fichier pour des informations sur l'exécution du programme.

## Personnalisation

- **Changer la langue par défaut :**
  Vous pouvez spécifier différentes langues en changeant le code de la langue dans l'interface graphique. Par exemple, pour convertir en français, utilisez `fr`, pour l'espagnol `es`, etc. Voici quelques codes de langue courants :
  - `en` : Anglais
  - `fr` : Français
  - `es` : Espagnol
  - `de` : Allemand
  - [Voir la liste complète des langues prises en charge par gTTS ici](https://gtts.readthedocs.io/en/latest/module.html#languages).

- **Ajouter plus de fonctionnalités (facultatif) :**
  Vous pouvez étendre ce projet en ajoutant d'autres fonctionnalités telles que :
  - **Historique des conversions**.
  - **Interface personnalisée** avec d'autres composants graphiques (menus, boîtes de dialogue).

## Problèmes fréquents

- **Problème avec `playsound` :**
  Si vous rencontrez des problèmes avec la bibliothèque `playsound` (notamment sur certaines plateformes), essayez d'utiliser un autre lecteur audio, comme `Pygame` ou `pydub`.

## Auteurs

- **EL BAHRAOUI HASSAN**
  - Étudiant en Data Science, A.I & Digital Health Engineering

## Licence
Ce projet est sous licence MIT. Vous êtes libre de le modifier et de l'utiliser comme bon vous semble.