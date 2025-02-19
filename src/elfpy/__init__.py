"""Elfpy package"""

import shutil
import logging

import matplotlib as mpl

# Setup barebones logging without a handler for users to adapt to their needs.
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Logging defaults
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMATTER = "\n%(asctime)s: %(levelname)s: %(module)s.%(funcName)s:\n%(message)s"
DEFAULT_LOG_DATETIME = "%y-%m-%d %H:%M:%S"
DEFAULT_LOG_MAXBYTES = int(2e6)  # 2MB

# Plotting defaults
BLACK = "black"
CYCLE = "colorblind"
CMAPCYC = "twilight"
CMAPDIV = "BuRd"
CMAPSEQ = "viridis"
CMAPCAT = "colorblind10"
DIVERGING = "div"
FRAMEALPHA = 0.0  # legend and colorbar
FONTNAME = "sans-serif"
FONTSIZE = 9.0
GRIDALPHA = 0.1
GRIDBELOW = "line"
GRIDPAD = 3.0
GRIDRATIO = 0.5  # differentiated from major by half size reduction
GRIDSTYLE = "-"
LABELPAD = 4.0  # default is 4.0, previously was 3.0
LARGESIZE = "large"
LEGENDLOC = "best"
LINEWIDTH = 0.6
MARGIN = 0.05
MATHTEXT = shutil.which("latex") is not None  # True if latex is installed, as required by matplotlib
SMALLSIZE = "medium"
TITLEWEIGHT = "bold"
TICKDIR = "out"
TICKLEN = 4.0
TICKLENRATIO = 0.5  # very noticeable length reduction
TICKMINOR = True
TICKPAD = 2.0
TICKWIDTHRATIO = 0.8  # very slight width reduction
TITLEPAD = 5.0  # default is 6.0, previously was 3.0
WHITE = "white"
ZLINES = 2  # default zorder for lines
ZPATCHES = 1

# Overrides of matplotlib default style
rc_params = {
    "axes.axisbelow": GRIDBELOW,
    "axes.formatter.use_mathtext": MATHTEXT,
    "axes.grid": True,  # enable lightweight transparent grid by default
    "axes.grid.which": "major",
    "axes.edgecolor": BLACK,
    "axes.labelcolor": BLACK,
    "axes.labelpad": LABELPAD,  # more compact
    "axes.labelsize": SMALLSIZE,
    "axes.labelweight": "normal",
    "axes.linewidth": LINEWIDTH,
    "axes.titlepad": TITLEPAD,  # more compact
    "axes.titlesize": LARGESIZE,
    "axes.titleweight": TITLEWEIGHT,
    "axes.xmargin": MARGIN,
    "axes.ymargin": MARGIN,
    "errorbar.capsize": 3.0,
    "figure.autolayout": False,
    "figure.figsize": (4.0, 4.0),  # for interactife backends
    "figure.dpi": 100,
    "figure.facecolor": "#f4f4f4",  # similar to MATLAB interface
    "figure.titlesize": LARGESIZE,
    "figure.titleweight": TITLEWEIGHT,
    "font.family": FONTNAME,
    "font.size": FONTSIZE,
    "grid.alpha": GRIDALPHA,  # lightweight unobtrusive gridlines
    "grid.color": BLACK,  # lightweight unobtrusive gridlines
    "grid.linestyle": GRIDSTYLE,
    "grid.linewidth": LINEWIDTH,
    "hatch.color": BLACK,
    "hatch.linewidth": LINEWIDTH,
    "image.cmap": CMAPSEQ,
    "lines.linestyle": "-",
    "lines.linewidth": 1.5,
    "lines.markersize": 6.0,
    "legend.loc": LEGENDLOC,
    "legend.borderaxespad": 0,  # i.e. flush against edge
    "legend.borderpad": 0.5,  # a bit more roomy
    "legend.columnspacing": 1.5,  # a bit more compact (see handletextpad)
    "legend.edgecolor": BLACK,
    "legend.facecolor": WHITE,
    "legend.fancybox": True,  # i.e. BboxStyle 'square' not 'round'
    "legend.fontsize": SMALLSIZE,
    "legend.framealpha": FRAMEALPHA,
    "legend.handleheight": 1.0,  # default is 0.7
    "legend.handlelength": 1.0,  # default is 2.0
    "legend.handletextpad": 0.5,  # a bit more compact (see columnspacing)
    "mathtext.default": "it",
    "mathtext.fontset": "custom",
    "mathtext.bf": "regular:bold",  # custom settings implemented above
    "mathtext.cal": "cursive",
    "mathtext.it": "regular:italic",
    "mathtext.rm": "regular",
    "mathtext.sf": "regular",
    "mathtext.tt": "monospace",
    "patch.linewidth": LINEWIDTH,
    "savefig.bbox": None,  # do not use 'tight'
    "savefig.directory": "",  # use the working directory
    "savefig.dpi": 1000,  # use academic journal recommendation
    "savefig.facecolor": WHITE,  # use white instead of 'auto'
    "savefig.format": "pdf",  # use vector graphics
    "savefig.transparent": False,
    "text.usetex": MATHTEXT,
    "xtick.color": BLACK,
    "xtick.direction": TICKDIR,
    "xtick.labelsize": SMALLSIZE,
    "xtick.major.pad": TICKPAD,
    "xtick.major.size": TICKLEN,
    "xtick.major.width": LINEWIDTH,
    "xtick.minor.pad": TICKPAD,
    "xtick.minor.size": TICKLEN * TICKLENRATIO,
    "xtick.minor.width": LINEWIDTH * TICKWIDTHRATIO,
    "xtick.minor.visible": TICKMINOR,
    "ytick.color": BLACK,
    "ytick.direction": TICKDIR,
    "ytick.labelsize": SMALLSIZE,
    "ytick.major.pad": TICKPAD,
    "ytick.major.size": TICKLEN,
    "ytick.major.width": LINEWIDTH,
    "ytick.minor.pad": TICKPAD,
    "ytick.minor.size": TICKLEN * TICKLENRATIO,
    "ytick.minor.width": LINEWIDTH * TICKWIDTHRATIO,
    "ytick.minor.visible": TICKMINOR,
}
mpl.rcParams.update(rc_params)
