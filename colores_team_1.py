
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# DEfinimos los colores que forman parte de la paleta personalizada
paleta_team_1 = [
    "#DA878E",  # Rosa suave
    "#E99A7B",  # Salmón
    "#F1D09E",  # Beige
    "#9EBE99",  # Verde suave
    "#91B0BC",  # Azul grisáceo
    "#9E81BA",  # Morado pastel
    "#D994BF"]   # Rosa pastel

#creamos la funcion para decirle a seaborn que use la pelatela personalizada por defecto.
def apply_team_palette():
    sns.set_palette(paleta_team_1)
    print("Team palette applied")

#en los casos en los que necesitemos más colores de los 7 colores que tiene la paleta personaliza, 
#creamos un degradado de colores con una trancision suave (N=256 como parametro)
def get_gradient_cmap(name="team_palette_gradient", N=256):
    return LinearSegmentedColormap.from_list(name, paleta_team_1, N=N)
