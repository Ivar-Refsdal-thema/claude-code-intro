import matplotlib as mpl
from cycler import cycler
from matplotlib.colors import LinearSegmentedColormap
import colorsys


# Theme colors
theme_colors = {
    'teal': (40 / 255, 80 / 255, 100 / 255),
    'blue': (151 / 255, 213 / 255, 255 / 255),
    'dark green': (80 / 255, 120 / 255, 100 / 255),
    'yellow': (253 / 255, 220 / 255, 115 / 255),
    'light green': (164 / 255, 203 / 255, 141 / 255),
    'purple': (162 / 255, 98 / 255, 132 / 255),
    'red': (226 / 255, 138 / 255, 118 / 255),
    'brown': (150 / 255, 140 / 255, 109 / 255),
}
# Variations for color shades
shades = {1: 0.8, 2: 0.6, 3: 0.4, 4: 0.2, 5: -0.25, 6: -0.5}

# Generate color variations directly
theme_colors.update({
    f"{name}{version}": colorsys.hls_to_rgb(
        *(lambda h, l, s, v=variation: (h, l * (1 + v) if v < 0 else l + (1 - l) * v, s))
        (*colorsys.rgb_to_hls(*rgb), variation)
    )
    for version, variation in shades.items()
    for name, rgb in theme_colors.items()
})
# Base colors with additional grid color
theme_colors = {**theme_colors, 'gridColor': (0.827, 0.827, 0.827)}

#%% Functions to set the matplotlib theme
def set_matplotlib_theme(background='white'):
    colors = theme_colors
    
    if background == 'white':
        mpl.rcParams["axes.prop_cycle"] = cycler(
                        color =
                        theme_colors.values()
                        )
        
        # === THEMA Light Theme Configuration ===

        # ---------------------------------------------------------------------
        # FONT & TEXT
        # ---------------------------------------------------------------------
        mpl.rcParams["font.family"] = "sans"
        mpl.rcParams["font.size"] = 14
        mpl.rcParams["text.color"] = colors["teal"]

        # ---------------------------------------------------------------------
        # AXES & TICKS
        # ---------------------------------------------------------------------
        mpl.rcParams["axes.labelcolor"] = colors["teal"]
        mpl.rcParams["axes.edgecolor"] = colors["teal"]
        mpl.rcParams["axes.linewidth"] = 0.8
        mpl.rcParams["axes.xmargin"] = 0.0000001  # almost no margin but nice tick spacing

        # Ticks
        mpl.rcParams["xtick.color"] = colors["teal"]
        mpl.rcParams["xtick.major.width"] = 1.5
        mpl.rcParams["xtick.major.size"] = 8
        mpl.rcParams["ytick.color"] = colors["teal"]
        mpl.rcParams["ytick.major.width"] = 1.5
        mpl.rcParams["ytick.major.size"] = 8

        # ---------------------------------------------------------------------
        # GRID
        # ---------------------------------------------------------------------
        mpl.rcParams["axes.grid"] = True
        mpl.rcParams["grid.color"] = colors["gridColor"]
        mpl.rcParams["grid.linestyle"] = "--"
        mpl.rcParams["grid.linewidth"] = 1
        # mpl.rcParams["grid.alpha"] = 0.4  # optional subtlety if desired
        mpl.rcParams["axes.axisbelow"] = "line"  # grid behind plot elements

        # ---------------------------------------------------------------------
        # FIGURE & CANVAS
        # ---------------------------------------------------------------------
        mpl.rcParams["figure.facecolor"] = "white"
        mpl.rcParams["axes.facecolor"] = "white"
        mpl.rcParams["figure.figsize"] = [7, 10]

        # ---------------------------------------------------------------------
        # LINES
        # ---------------------------------------------------------------------
        mpl.rcParams["lines.linewidth"] = 2

        # ---------------------------------------------------------------------
        # LEGEND
        # ---------------------------------------------------------------------
        mpl.rcParams["legend.fontsize"] = 12
        mpl.rcParams["legend.loc"] = "upper right"
        mpl.rcParams["legend.handlelength"] = 1
        mpl.rcParams["legend.frameon"] = True

        # ---------------------------------------------------------------------
        # SAVE / EXPORT
        # ---------------------------------------------------------------------
        mpl.rcParams["savefig.transparent"] = False
        mpl.rcParams["figure.dpi"] = 100
        mpl.rcParams["savefig.dpi"] = 100
    
    elif background == 'dark':
        white = (1, 1, 1)
        
        mpl.rcParams["axes.prop_cycle"] = cycler(
                        color =
                        colors.values()
                        )
                        
        # ---------------------------------------------------------------------
        # FONT & TEXT
        # ---------------------------------------------------------------------
        mpl.rcParams["font.family"] = "sans"
        mpl.rcParams["font.size"] = 14
        mpl.rcParams["text.color"] = white

        # ---------------------------------------------------------------------
        # AXES & TICKS
        # ---------------------------------------------------------------------
        mpl.rcParams["axes.labelcolor"] = white
        mpl.rcParams["axes.edgecolor"] = "white"
        mpl.rcParams["axes.linewidth"] = 1.5
        mpl.rcParams["axes.xmargin"] = 0.0000001  # almost no margin but nice tick spacing

        # Hide top and right borders
        mpl.rcParams["axes.spines.top"] = False
        mpl.rcParams["axes.spines.right"] = False

        # Ticks
        mpl.rcParams["xtick.color"] = white
        mpl.rcParams["xtick.major.width"] = 1.5
        mpl.rcParams["xtick.major.size"] = 8
        mpl.rcParams["ytick.color"] = white
        mpl.rcParams["ytick.major.width"] = 1.5
        mpl.rcParams["ytick.major.size"] = 8

        # ---------------------------------------------------------------------
        # GRID
        # ---------------------------------------------------------------------
        mpl.rcParams["axes.grid"] = True
        mpl.rcParams["grid.color"] = white
        mpl.rcParams["grid.linestyle"] = "--"
        mpl.rcParams["grid.linewidth"] = 0.8
        mpl.rcParams["grid.alpha"] = 0.2   # faint grid lines
        mpl.rcParams["axes.axisbelow"] = "line"  # grid behind plot elements

        # ---------------------------------------------------------------------
        # FIGURE & CANVAS
        # ---------------------------------------------------------------------
        mpl.rcParams["figure.facecolor"] = colors["teal"]
        mpl.rcParams["axes.facecolor"] = colors["teal"]
        mpl.rcParams["figure.figsize"] = [12, 6]

        # ---------------------------------------------------------------------
        # LINES
        # ---------------------------------------------------------------------
        mpl.rcParams["lines.linewidth"] = 2.5

        # ---------------------------------------------------------------------
        # LEGEND
        # ---------------------------------------------------------------------
        mpl.rcParams["legend.fontsize"] = 12
        mpl.rcParams["legend.loc"] = "upper left"
        mpl.rcParams["legend.handlelength"] = 1
        mpl.rcParams["legend.frameon"] = False

        # ---------------------------------------------------------------------
        # SAVE / EXPORT
        # ---------------------------------------------------------------------
        mpl.rcParams["savefig.transparent"] = False
        mpl.rcParams["figure.dpi"] = 150
        mpl.rcParams["savefig.dpi"] = 150


def create_cmap(colors):
    return LinearSegmentedColormap.from_list(
        "custom_cmap", colors, N=256)

def get_plot_color(key):
    # Consolidate all color mappings into a list of dictionaries
    color_maps = [
        # Zone Colors
        {
            'DEU': theme_colors['dark green'],
            "FRA": theme_colors['blue'],
            "DK1": theme_colors['red'],
            "DK2": theme_colors['red3'],
            "AUT": theme_colors['teal2'],
            "BEL": theme_colors['yellow3'],
            "NLD": theme_colors['dark green2'],
            "NO1": theme_colors['teal'],
            "NO2": theme_colors['teal4'],
            "NO3": theme_colors['blue'],
            "NO4": theme_colors['blue3'],
            "NO5": theme_colors['blue2'],
            "SE1": theme_colors['yellow2'],
            "SE2": theme_colors['yellow4'],
            "SE3": theme_colors['yellow'],
            "SE4": theme_colors['yellow5'],
            "FIN": theme_colors['dark green']
        }, 
        # Country Colors
        {
            "Norway": theme_colors['teal3'],
            "Sweden": theme_colors['yellow'],
            "Denmark": theme_colors['red'],
            "Finland": theme_colors['dark green'],
        },
        # Scenario Colors
        {
            "REF": theme_colors['teal4'],
            "HIG": theme_colors['yellow'],
            "LOW": theme_colors['blue3'],
        },  
        # Year Colors
        {
            2025: theme_colors['blue'],
            2030: theme_colors['teal'],
            2035: theme_colors['yellow5'],
            2040: theme_colors['dark green'],
            2050: theme_colors['light green'],
        },  
        # Technology Colors
        {
            # Renewables - Solar & Wind (various naming variants)
            "Solar": theme_colors['yellow'],
            "Wind_Onshore": theme_colors['teal3'],
            "Wind Onshore": theme_colors['teal3'],
            "Onshore Wind": theme_colors['teal3'],
            "Wind_Offshore": theme_colors['teal2'],
            "Wind Offshore": theme_colors['teal2'],
            "Offshore Wind": theme_colors['teal2'],
            "Intermittent Renewables": theme_colors['light green'],

            # Hydro family
            "Hydro": theme_colors['teal'],
            "Hydro_PHS": theme_colors['teal5'],
            "Hydro_Res": theme_colors['teal'],
            "Hydro_RoR": theme_colors['teal4'],
            "Flexible non-emitting": theme_colors['teal2'],

            # Battery / Storage
            "Battery": theme_colors['yellow5'],
            "Battery discharge": theme_colors['yellow5'],

            # Nuclear
            "Nuclear": theme_colors['purple4'],

            # Bio / Waste / BECCS
            "Bio": theme_colors['dark green'],
            "Waste": theme_colors['dark green5'],
            "BECCS": theme_colors['light green3'],

            # Fossil / Thermal / Gas / Oil / Coal / HFO / CHP
            "Gas": theme_colors['red'],
            "Gas carbon capture": theme_colors['red2'],
            "Fossil thermal": theme_colors['red'],
            "Coal": theme_colors['brown5'],
            "Oil": theme_colors['brown4'],
            "HFO": theme_colors['brown'],
            "CHP": theme_colors['red3'],

            # Carbon / Emissions related
            "CO2": theme_colors['yellow5'],

            # Other / residuals
            "Other": (0.87, 0.87, 0.87),
            "Other_Res": theme_colors['light green2'],
        },   
        # Demand Colors
        {   
            "Hydrogen": theme_colors['yellow5'],
            "Conventional": theme_colors['dark green'],
            "Industry": theme_colors['dark green'],
            "Households and services": theme_colors['teal3'],
            "Heating": theme_colors['red'],
            "Transport": theme_colors['dark green3'],
            "Data centers": theme_colors['purple4'],
        },   
        # Other Colors
        {
            "Zero price": "#1e4b50",
            "Positive price": "#333f4f",
        },  
    ]

    # Search in each dictionary and return the color if found
    for color_map in color_maps:
        if key in color_map:
            return color_map[key]

    # Return a default color or raise an error if key not found
    return theme_colors.get('default', '#000000')  # Default color: black
