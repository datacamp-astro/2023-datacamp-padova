"""draw the unified AGN scheme"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.lines as lines
from scipy import ndimage
import numpy.random as rnd

# defining the aspect ratio for the curves
# background = plt.imread("../figures/CenA_composite.jpg")
# rotated_background = ndimage.rotate(background, -50)

fig, ax = plt.subplots()
##ax.imshow(rotated_background, extent=[-30, 6, -30, 6])

# let's plot the black hole
bh = patches.Ellipse(xy=[-6.0, -6], width=2.0, height=1.5, facecolor="black")
ax.add_artist(bh)
# let's plot the jet
verts_jet = [
    (-6.25, -5.0),  # left, bottom
    (-7.0, 4.0),  # left, top
    (-5.0, 4.0),  # right, top
    (-5.75, -5.0),  # right, bottom
    (0.0, 0.0),  # ignored
]

codes_jet = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]

path_jet = Path(verts_jet, codes_jet)
patch_jet = patches.PathPatch(path_jet, facecolor="goldenrod", hatch="\\")
ax.add_patch(patch_jet)

# let's plot the first half of the accretion disk
verts_disk1 = [
    (-5.0, -6.0),  # left, bottom
    (-5.0, -5.6),  # left, top
    (-3.0, -5.3),  # right, top
    (-3.0, -6.0),  # right, bottom
    (0.0, 0.0),  # ignored
]

codes_disk1 = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]

path_disk1 = Path(verts_disk1, codes_disk1)
patch_disk1 = patches.PathPatch(
    path_disk1, facecolor="#5D8AA8", linewidth=0.1, hatch="."
)
ax.add_patch(patch_disk1)

# let's plot the second half of the accretion disk
verts_disk2 = [
    (-7.0, -6.0),  # left, bottom
    (-7.0, -5.6),  # left, top
    (-9.0, -5.3),  # right, top
    (-9.0, -6.0),  # right, bottom
    (0.0, 0.0),  # ignored
]

codes_disk2 = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]

path_disk2 = Path(verts_disk2, codes_disk2)
patch_disk2 = patches.PathPatch(
    path_disk2, facecolor="#5D8AA8", linewidth=0.1, hatch="."
)
ax.add_patch(patch_disk2)

# let's plot the broad line region
# generate random ellipse a t a certain radius
# set the seed such that figures are reproducible
rnd.seed(6)
ells = []

for i in range(250):
    x = rnd.rand() * -10
    y = rnd.rand() * -6
    if (x + 6) ** 2 + (y + 6) ** 2 > 9.0 and (x + 6) ** 2 + (y + 6) ** 2 < 16.0:
        ells.append(
            patches.Ellipse(
                xy=[x, y],
                width=0.15,
                height=0.35,
                angle=rnd.rand() * 360,
                facecolor="#1E90FF",
            )
        )

for ellipse in ells:
    ax.add_artist(ellipse)

# let's plot the narrow line region
ells2 = []

for i in range(75):
    x = rnd.rand() * -11
    y = rnd.rand() * 3

    ells2.append(
        patches.Ellipse(
            xy=[x, y], width=0.18, height=0.18, angle=rnd.rand() * 360, facecolor="teal"
        )
    )

for ellipse in ells2:
    ax.add_artist(ellipse)

# let's plot the torus
torus1 = patches.Ellipse(
    xy=[3.0, -6.0], width=6.0, height=12.0, facecolor="#BE0032", hatch="O"
)
torus2 = patches.Ellipse(
    xy=[-15.0, -6.0], width=6.0, height=12.0, facecolor="#BE0032", hatch="O"
)

ax.add_artist(torus1)
ax.add_artist(torus2)

# add the blob
blob = patches.Ellipse(xy=[-6.0, 3], width=1.3, height=1., facecolor="maroon")
ax.add_artist(blob)

legend = ax.legend(
    [
        lines.Line2D([0], [0], marker="o", color="k", ls="", markersize=13),
        patch_disk1,
        patch_jet,
        lines.Line2D([0], [0], marker="o", color="#1E90FF", ls=""),
        lines.Line2D([0], [0], marker="o", color="teal", ls=""),
        torus1,
        lines.Line2D([0], [0], marker="o", color="maroon", ls="", markersize=13)
    ],
    ["Black Hole", "Disk", "Jet", "Broad Lines", "Narrow Lines", "Torus", "Blob"],
    loc="best",
    framealpha=1.0,
    fontsize=14
)
ax.set_xticks((-5, -3, -1, 1))
ax.minorticks_off()
ax.set_ylim([-6.0, 4.0])
ax.set_xlim([-14.0, 2.0])

ax.set_xlabel(r"$\log_{10}(r\,/\,\mathrm{pc})$")
ax.set_ylabel(r"$\log_{10}(z\,/\,\mathrm{pc})$")
box = ax.get_position()
plt.show()
fig.savefig("AGN_scheme.png")
fig.savefig("AGN_scheme.pdf")

