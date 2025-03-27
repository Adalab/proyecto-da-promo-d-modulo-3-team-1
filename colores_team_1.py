
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Paleta de colores personalizada - paleta team 1 (sin blanco ni negro)
paleta_team_1 = [
    "#DA878E",  # Rosa suave
    "#E99A7B",  # Salmón
    "#F1D09E",  # Beige
    "#9EBE99",  # Verde suave
    "#91B0BC",  # Azul grisáceo
    "#9E81BA",  # Morado pastel
    "#D994BF"   # Rosa pastel
]

def apply_team_palette():
    """
    Apply the base team palette to seaborn
    """
    sns.set_palette(paleta_team_1)
    print("Team palette applied (white and black removed)")

def get_gradient_cmap(name="team_palette_gradient", N=256):
    """
    Generate a gradient colormap from the base palette for heatmaps or large color needs
    """
    return LinearSegmentedColormap.from_list(name, paleta_team_1, N=N)
