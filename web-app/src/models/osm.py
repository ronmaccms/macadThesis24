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
from shapely.geometry import Polygon as ShapelyPolygon, box
from shapely.affinity import scale

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
        simrec_list (list): List of minimum rotated rectangles (shapely.geometry.Polygon)
        minun_rectangle_all (Polygon): A single minimum rotated rectangle encompassing all building footprints.
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
    if isinstance(multip, Polygon):
        # Single polygon case
        geom = multip
        simrec = geom.minimum_rotated_rectangle
        simrec_list.append(simrec)
    elif isinstance(multip, MultiPolygon):
        for geom in multip.geoms:
            if isinstance(geom, Polygon):
                # Calculate the minimum rotated rectangle for each geometry
                simrec = geom.minimum_rotated_rectangle
                simrec_list.append(simrec)

    # Calculate the minimum rotated rectangle for the entire multipolygon
    minun_rectangle_all = multip.minimum_rotated_rectangle

    # Simplify the geometry (optional)
    multip = multip.simplify(tolerance=1.0)  # Increase tolerance to simplify further

    return simrec_list, minun_rectangle_all

# Function to extract corner points of rectangles as a list of tuples and plot them
def plot_rectangle_points(simrec_list):
    """
    Plots the corner points of rectangles.

    Args:
        simrec_list (list): List of minimum rotated rectangles (shapely.geometry.Polygon) 
                            or list of lists of tuples representing the corner points.
    """
    plt.figure()
    for i, rect_points in enumerate(simrec_list):  # Iterate over the list
        if isinstance(rect_points, Polygon):
            x, y = rect_points.exterior.xy  # Extract coordinates from Polygon
        else:
            x, y = zip(*rect_points)  # Unpack the list of tuples into x, y coordinates

        plt.plot(x, y, color='red')

        for j, (px, py) in enumerate(zip(x, y)):  # Plot the points correctly
            plt.plot(px, py, 'bo')  # Plot the points in blue
            plt.text(px, py, f'({px:.2f}, {py:.2f})', fontsize=7, ha='center')  # Label the points

    plt.title("Corner Points of Rectangles")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()

# lalalal


# Function to extract corner points of rectangles as a list of tuples
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

def calculate_combined_boundary(rectangle_points_list, expansion_factor=0.05):
    """
    Calculates the combined boundary of all rectangles and expands it by a given factor.

    Args:
        rectangle_points_list (list of lists): List where each inner list contains tuples 
                                               representing the corner points of a rectangle.
        expansion_factor (float): Factor by which to expand the boundary. Default is 0.05 (5%).

    Returns:
        boundary (tuple): Expanded boundary coordinates as (min_x, min_y, max_x, max_y).
    """
    all_x = []
    all_y = []

    # Collect all x and y coordinates from all rectangles
    for rect_points in rectangle_points_list:
        x_coords, y_coords = zip(*rect_points)
        all_x.extend(x_coords)
        all_y.extend(y_coords)

    # Calculate the minimum and maximum x and y coordinates
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)

    # Calculate the expansion amounts
    x_expansion = (max_x - min_x) * expansion_factor
    y_expansion = (max_y - min_y) * expansion_factor

    # Apply the expansion to the boundary
    expanded_min_x = min_x - x_expansion
    expanded_max_x = max_x + x_expansion
    expanded_min_y = min_y - y_expansion
    expanded_max_y = max_y + y_expansion

    return expanded_min_x, expanded_min_y, expanded_max_x, expanded_max_y

def calculate_combined_boundary(rectangle_points_list):
    # Convert each rectangle to a Shapely Polygon
    polygons = [ShapelyPolygon(rect_points) for rect_points in rectangle_points_list]
    
    # Combine all polygons into a single polygon (union)
    combined_polygon = polygons[0]
    for poly in polygons[1:]:
        combined_polygon = combined_polygon.union(poly)
    
    # Get the bounding box of the combined polygon
    minx, miny, maxx, maxy = combined_polygon.bounds
    
    # Scale the bounding box by a factor (e.g., 1.1 to increase size by 10%)
    bounding_box = box(minx, miny, maxx, maxy)
    scaled_bounding_box = scale(bounding_box, xfact=1.1, yfact=1.1, origin='center')
    
    # Get the new channel length and width
    channel_length = (scaled_bounding_box.bounds[0], scaled_bounding_box.bounds[2])
    channel_width = (scaled_bounding_box.bounds[1], scaled_bounding_box.bounds[3])
    
    return channel_length, channel_width

def calculate_length_and_width(rect_points):
    """
    Calculate the length and width of a rectangle based on its corner points.

    Args:
        rect_points (list): A list of tuples representing the corner points of the rectangle.

    Returns:
        length (float): The length of the rectangle (along the x-axis).
        width (float): The width of the rectangle (along the y-axis).
    """
    x_coords = [point[0] for point in rect_points]
    y_coords = [point[1] for point in rect_points]
    
    length = max(x_coords) - min(x_coords)
    width = max(y_coords) - min(y_coords)
    
    return length, width

def update_channel_dimensions(rectangle_points_list):
    """
    Update the channel length and width based on the largest rectangle in the list.

    Args:
        rectangle_points_list (list): A list of lists containing corner points for each rectangle.
    
    Returns:
        channel_length (tuple): Tuple representing the updated length of the channel.
        channel_width (tuple): Tuple representing the updated width of the channel.
    """
    max_length = 0
    max_width = 0

    for rect_points in rectangle_points_list:
        rect_points.pop()  # Remove last point if it's the closing point
        length, width = calculate_length_and_width(rect_points)
        max_length = max(max_length, length)
        max_width = max(max_width, width)
    
    # Assuming channel_length and channel_width should start from 0
    channel_length = (0, max_length)
    channel_width = (0, max_width)
    
    return channel_length, channel_width

# Define the necessary functions first
def calculate_min_max_coordinates(rectangle_points_list):
    all_x_coords = []
    all_y_coords = []

    for rect_points in rectangle_points_list:
        x_coords = [point[0] for point in rect_points]
        y_coords = [point[1] for point in rect_points]
        all_x_coords.extend(x_coords)
        all_y_coords.extend(y_coords)
    
    min_x = min(all_x_coords)
    max_x = max(all_x_coords)
    min_y = min(all_y_coords)
    max_y = max(all_y_coords)

    return min_x, max_x, min_y, max_y


