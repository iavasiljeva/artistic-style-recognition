import os 
from os.path import join
PATH_ORIGIN = {
        "ICON" : '..\\Pandora_18k\\01_Byzantin_Iconography\\',
        "E_REN" : '..\\Pandora_18k\\02_Early_Renaissance\\',
        "N_REN" : '..\\Pandora_18k\\03_Northern_Renaissance\\',
        "H_REN" : '..\\Pandora_18k\\04_High_Renaissance\\',
        "BAR" : '..\\Pandora_18k\\05_Baroque\\',
        "ROC" : '..\\Pandora_18k\\06_Rococo\\',
        "ROM" : '..\\Pandora_18k\\07_Romanticism\\',
        "REAL" : '..\\Pandora_18k\\08_Realism\\',
        "IMPR" : '..\\Pandora_18k\\09_Impressionism\\',
        "P_IMPR" : '..\\Pandora_18k\\10_Post_Impressionism\\',
        "EXPR" : '..\\Pandora_18k\\11_Expressionism\\',
        "SYMB" : '..\\Pandora_18k\\12_Symbolism\\',
        "FAUV" : '..\\Pandora_18k\\13_Fauvism\\',
        "CUB" : '..\\Pandora_18k\\14_Cubism\\',
        "SUR" : '..\\Pandora_18k\\15_Surrealism\\',
        "ABSTRACT" : '..\\Pandora_18k\\16_AbstractArt\\',
        "NAIVE" : '..\\Pandora_18k\\17_NaiveArt\\',
        "POP" : '..\\Pandora_18k\\18_PopArt\\',      
       }
PATH_CROP = {
        "ICON" : '..\\Pandora_18k\\CROP\\01_Byzantin_Iconography\\',
        "E_REN" : '..\\Pandora_18k\\CROP\\02_Early_Renaissance\\',
        "N_REN" : '..\\Pandora_18k\\CROP\\03_Northern_Renaissance\\',
        "H_REN" : '..\\Pandora_18k\\CROP\\04_High_Renaissance\\',
        "BAR" : '..\\Pandora_18k\\CROP\\05_Baroque\\',
        "ROC" : '..\\Pandora_18k\\CROP\\06_Rococo\\',
        "ROM" : '..\\Pandora_18k\\CROP\\07_Romanticism\\',
        "REAL" : '..\\Pandora_18k\\CROP\\08_Realism\\',
        "IMPR" : '..\\Pandora_18k\\CROP\\09_Impressionism\\',
        "P_IMPR" : '..\\Pandora_18k\\CROP\\10_Post_Impressionism\\',
        "EXPR" : '..\\Pandora_18k\\CROP\\11_Expressionism\\',
        "SYMB" : '..\\Pandora_18k\\CROP\\12_Symbolism\\',
        "FAUV" : '..\\Pandora_18k\\CROP\\13_Fauvism\\',
        "CUB" : '..\\Pandora_18k\\CROP\\14_Cubism\\',
        "SUR" : '..\\Pandora_18k\\CROP\\15_Surrealism\\',
        "ABSTRACT" : '..\\Pandora_18k\\CROP\\16_AbstractArt\\',
        "NAIVE" : '..\\Pandora_18k\\CROP\\17_NaiveArt\\',
        "POP" : '..\\Pandora_18k\\CROP\\18_PopArt\\',      
       }
FEATURES = {
        "RF" : "..\\Features\\RandomForest\\",
        "RF_HoT" : "..\\Features\\RandomForest_HoT\\"
       }
def get_all_files(cropped=True):
    if cropped:
        path = PATH_CROP
    else:
        path = PATH_ORIGIN
    files = list()
    for genre in path.items():
        if genre[0] == "ABSTRACT":
            subgenres = [join(genre[1],folder) for folder in os.listdir(genre[1]) if folder[0] != "_"]
            for subgenre in subgenres:
                artists = os.listdir(subgenre)
                for artist in artists:
                    images = os.listdir(join(subgenre, artist))
                    for image in images:
                        files.append(join(subgenre, artist, image))
        else:
            artists = os.listdir(genre[1])
            for artist in artists:
                images = os.listdir(join(genre[1], artist))
                for image in images:
                    files.append(join(genre[1], artist, image))
    return sorted(files)

def get_genre_id(path):
    try:
        return int(path[15:17])
    except:
        return int(path[20:22])