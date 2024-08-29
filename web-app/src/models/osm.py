# Import necessary libraries
import phi.jax.flow as phi  # Import PhiFlow with JAX backend
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon
import shapely.ops
import shapely
from jax import jit
from shapely import ops

# Set OSMnx SSL cert verification to off (useful for certain work environments)
ox.settings.requests_kwargs['verify'] = False

# Function to fetch and process building footprints
def fetch_building_footprints(location_point, radius=100, res=200):
    """
    Fetches and processes building footprints within a specified radius from a location point.

    Args:
        location_point (tuple): A tuple containing the latitude and longitude of the location point.
        radius (int, optional): Radius in meters for the area of interest. Default is 100 meters.
        res (int, optional): Resolution for the plot. Default is 200.

    Returns:
        multip (shapely.geometry.MultiPolygon): Simplified union of building footprints.
    """

    # Fetch building footprints within the specified radius
    buildings = ox.features_from_point(location_point, tags={'building': True}, dist=radius)

    # Plot to visualize the area
    fig, ax = ox.plot_footprints(buildings, color='cyan', dpi=res)
    # plt.show()

    # Transform the footprints from coordinates to meters on the ground
    footprints = shapely.transform(
        buildings['geometry'], 
        lambda x: (x - location_point[::-1]) * 111139
    )

    # Use a unary union operation to remove interior boundaries
    multip = shapely.ops.unary_union(footprints)

    # Initialize a list to hold the minimum rotated rectangles
    simrec_list = []

    # Iterate through each geometry in the unified multipolygon
    for geom in multip.geoms:
        if isinstance(geom, (Polygon, MultiPolygon)):
            # Calculate the minimum rotated rectangle for each geometry
            simrec = geom.minimum_rotated_rectangle
            simrec_list.append(simrec)

    # Simplify the geometry
    multip = multip.simplify(tolerance=3.0)  # Increase tolerance to simplify further

    # Plot the simplified footprints
    for footprint in multip.geoms:
        plt.plot(*footprint.exterior.xy)

    # Plot the minimum rotated rectangles for each geometry
    for simrec in simrec_list:
        x, y = simrec.exterior.xy
        plt.plot(x, y, color='red')

    plt.title("Simplified Footprints and Their Minimum Rotated Rectangles")
    plt.show()

    return multip
