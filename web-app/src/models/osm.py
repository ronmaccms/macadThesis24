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
    multip = multip.simplify(tolerance=1.0)  # Increase tolerance to simplify further

    # Plot the minimum rotated rectangles for each geometry
    for simrec in simrec_list:
        x, y = simrec.exterior.xy
        plt.plot(x, y, color='red')

    plt.title("Simplified Footprints and Their Minimum Rotated Rectangles")
    plt.show()

    return simrec_list

# Function to extract corner points of rectangles as a list of tuples and plot them
def plot_rectangle_points(simrec_list):
    """
    Extracts the corner points of each rectangle in the list and plots them.

    Args:
        simrec_list (list): List of minimum rotated rectangles (shapely.geometry.Polygon).

    Returns:
        rectangle_points (list): List of tuples representing the corner points of each rectangle.
    """
    rectangle_points = []

    plt.figure()
    for i, simrec in enumerate(simrec_list):
        # Extract the exterior coordinates of the polygon
        coords = list(simrec.exterior.coords)
        # Convert to a list of tuples
        rectangle_points.append(coords)

        # Plot the rectangle
        x, y = simrec.exterior.xy
        plt.plot(x, y, color='red')

        # Plot the corner points
        for j, (px, py) in enumerate(coords):
            plt.plot(px, py, 'bo')  # Plot the points in blue
            plt.text(px, py, f'{i+1}-{j+1}', fontsize=8, ha='center')  # Label the points

    plt.title("Corner Points of Rectangles")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()

    return rectangle_points

def extract_rectangle_points(simrec_list):
    """
    Extracts the corner points of each rectangle in the list.

    Args:
        simrec_list (list): List of minimum rotated rectangles (shapely.geometry.Polygon).

    Returns:
        rectangle_points_list (list of lists): List where each inner list contains tuples 
                                               representing the corner points of a rectangle.
    """
    rectangle_points_list = []

    for simrec in simrec_list:
        # Extract the exterior coordinates of the polygon
        coords = list(simrec.exterior.coords)
        rectangle_points_list.append(coords)

    return rectangle_points_list