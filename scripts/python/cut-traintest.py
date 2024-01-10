import os
import random
import shutil

# Chemin vers le répertoire contenant vos fichiers de données
data_directory = "/Users/kenza/Documents/etudes/M2_TAL/semestre1/CNN/RNN/corpus/fr/spectr-img"

# Charger les noms de fichiers dans le répertoire
file_names = os.listdir(data_directory)

# Liste pour stocker les noms de fichiers d'images
image_files = [f for f in os.listdir(data_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Mélanger les noms de fichiers
random.shuffle(image_files)

# Calculer la taille du corpus de test
test_size = int(len(image_files) * 0.1)

# Diviser les noms de fichiers en corpus de test et d'entraînement
train_image_files = image_files[:-test_size]
test_image_files = image_files[-test_size:]

# Afficher les tailles des corpus
print("Taille du corpus d'entraînement :", len(train_image_files))
print("Taille du corpus de test :", len(test_image_files))

# Copier les fichiers dans les répertoires d'entraînement et de test
train_directory = "/Users/kenza/Documents/etudes/M2_TAL/semestre1/CNN/RNN/corpus/corpus-traintest/fr/train"
test_directory = "/Users/kenza/Documents/etudes/M2_TAL/semestre1/CNN/RNN/corpus/corpus-traintest/fr/test"

# Créer les répertoires s'ils n'existent pas
os.makedirs(train_directory, exist_ok=True)
os.makedirs(test_directory, exist_ok=True)

# Copier les fichiers dans les répertoires respectifs
for train_file in train_image_files:
    shutil.copy(os.path.join(data_directory, train_file), os.path.join(train_directory, train_file))

for test_file in test_image_files:
    shutil.copy(os.path.join(data_directory, test_file), os.path.join(test_directory, test_file))
