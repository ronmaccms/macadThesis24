import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, box
from shapely import ops

# Function to fetch and process building footprints and simplify to rectangles
def fetch_and_simplify_building_footprints(location_point, radius=100, res=200):
    """
    Fetches and processes building footprints within a specified radius from a location point.
    Simplifies the footprints to rectangles.
    """
    # Fetch building footprints within the specified radius
    buildings = ox.features_from_point(location_point, tags={'building': True}, dist=radius)
    
    # Convert the footprints into rectangular bounding boxes
    simplified_buildings = []
    for geom in buildings['geometry']:
        # Get the bounding box (minimum rotated rectangle) for each footprint
        min_rect = geom.minimum_rotated_rectangle
        simplified_buildings.append(min_rect)

    # Plot the original footprints
    fig, ax = plt.subplots()
    for footprint in buildings['geometry']:
        x, y = footprint.exterior.xy
        ax.plot(x, y)

    plt.title("Original Footprints")
    plt.show()

    # Plot the simplified rectangular footprints
    fig, ax = plt.subplots()
    for footprint in simplified_buildings:
        x, y = footprint.exterior.xy
        ax.plot(x, y)

    plt.title("Simplified Rectangular Footprints")
    plt.show()

    return simplified_buildings

