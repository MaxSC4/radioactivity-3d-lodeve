import pyvista as pv
import numpy as np
import pandas as pd

def create_point_cloud(df: pd.DataFrame) -> pv.PolyData:
    """Create a PyVista point cloud with radioactivity scalar field."""
    points = df[["X", "Y", "Z"]].values.astype(np.float32)
    cloud = pv.PolyData(points)
    cloud["radioactivity"] = df["R"].astype(np.float32)
    return cloud

def show_point_cloud(cloud: pv.PolyData):
    """Display the point cloud in a PyVista window."""
    plotter = pv.Plotter()
    plotter.add_mesh(
        cloud,
        scalars="radioactivity",
        point_size=10.0,
        render_points_as_spheres=True,
        scalar_bar_args={"title": "Radioactivity (cpm)"},
    )
    plotter.show_axes()
    plotter.show()
