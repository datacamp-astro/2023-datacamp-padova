from regions import PointSkyRegion, CircleSkyRegion
from gammapy.maps import Map
from gammapy.makers import ReflectedRegionsFinder
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def create_fake_legend(ax):
    """Make a fake legend representing the ON and OFF regions."""
    on = Line2D(
        [0],
        [0],
        markeredgecolor="crimson",
        markerfacecolor="none",
        markeredgewidth=1.5,
        marker="o",
        markersize=14,
        ls="",
        label="on region",
    )
    off = Line2D(
        [0],
        [0],
        markeredgecolor="dodgerblue",
        markerfacecolor="none",
        markeredgewidth=1.5,
        marker="o",
        markersize=14,
        ls="",
        label="off regions",
    )
    pointing = Line2D(
        [0],
        [0],
        markeredgecolor="goldenrod",
        markerfacecolor="none",
        markeredgewidth=1.5,
        marker="+",
        markersize=14,
        ls="",
        label="pointing",
    )

    ax.legend(handles=[on, off, pointing], loc="lower left")


def plot_on_off_regions(observation, on_region, energies=None):
    """A function to plot a skymap of a particular observation and overplot
    the ON and OFF regions obtained with the reflected regions method."""
    fig = plt.figure()
    # let us make a countmap of the events in one of the observations
    region_finder = ReflectedRegionsFinder()

    counts = Map.create(skydir=observation.pointing_radec, binsz=0.06, width=4)
    # define wcs geom from the counts map
    wcs = counts.geom.wcs

    # fill the map and plot it, eventually cut in energy
    if energies is None:
        events = observation.events
    else:
        events = observation.events.select_energy(energies)
    counts.fill_events(events)

    ax = counts.plot(cmap="viridis", add_cbar=True)

    # plot pointing
    pointing = PointSkyRegion(observation.pointing_radec)
    pointing.to_pixel(wcs).plot(ax=ax, color="goldenrod", marker="+", markersize=14)
    # plot ON region
    on_region.to_pixel(wcs).plot(ax=ax, edgecolor="crimson", linewidth=2)
    # plot OFF regions
    off_regions, wcs = region_finder.run(
        region=on_region, center=observation.pointing_radec
    )
    for off_region in off_regions:
        off_region_circle = CircleSkyRegion(
            center=off_region.center, radius=on_region.radius
        )
        off_region_circle.to_pixel(ax.wcs).plot(
            ax=ax, edgecolor="dodgerblue", linewidth=2
        )

    ax.images[0].colorbar.set_label("counts", rotation=270, labelpad=12, fontsize=10)

    # add energies in the title, if an energy cut has been performed
    if energies is not None:
        ax.set_title(f"{energies[0].to('GeV'):.0f} < E' < {energies[1].to('GeV'):.0f}")

    create_fake_legend(ax)
    plt.show()