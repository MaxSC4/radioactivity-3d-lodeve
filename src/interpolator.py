import numpy as np
import pandas as pd
import pyvista as pv
from scipy.interpolate import RBFInterpolator

def interpolate_volume(df: pd.DataFrame, grid_spacing=25.0, depth=500.0) -> pv.ImageData:
    """
    Interpolate radioactivity from surface points into a 3D volume.

    Parameters:
    - df: DataFrame with columns X, Y, Z, R
    - grid_spacing: resolution of the interpolation grid (in meters)
    - depth: how deep the volume goes (from min(Z) downward)

    Returns:
    - pv.ImageData (uniform grid) with interpolated radioactivity
    """
    # Extract surface coordinates and values
    coords = df[["X", "Y", "Z"]].values.astype(np.float32)
    values = df["R"].values.astype(np.float32)

    # Define volume extent
    x_min, x_max = df["X"].min(), df["X"].max()
    y_min, y_max = df["Y"].min(), df["Y"].max()
    z_surface = df["Z"].min()
    z_bottom = z_surface - depth

    # Build regular 3D grid
    x = np.arange(x_min, x_max, grid_spacing)
    y = np.arange(y_min, y_max, grid_spacing)
    z = np.arange(z_bottom, z_surface, grid_spacing)  # from bottom to top
    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
    grid_points = np.column_stack((X.ravel(), Y.ravel(), Z.ravel()))

    # RBF interpolation
    rbf = RBFInterpolator(coords, values, neighbors=20, smoothing=5.0)
    interpolated_values = rbf(grid_points)
    volume = interpolated_values.reshape(X.shape)

    # Create uniform grid using ImageData
    grid = pv.ImageData()
    grid.dimensions = np.array(volume.shape) + 1  # because cell-centered
    grid.origin = (x[0], y[0], z[0])
    grid.spacing = (grid_spacing, grid_spacing, grid_spacing)
    grid.cell_data["radioactivity"] = volume.flatten(order="F")

    return grid
