import pandas as pd
import pyvista as pv
import numpy as np

# === 1. Load the CSV data ===
df = pd.read_csv("data/example.csv")  # Columns expected: X, Y, Z, R

# === 2. Convert to PyVista point cloud ===
points = df[['X', 'Y', 'Z']].values.astype(np.float32)
cloud = pv.PolyData(points)

# Add scalar field for radioactivity
cloud["radioactivity"] = df['R']

# === 3. Display in 3D viewer ===
plotter = pv.Plotter()
plotter.add_mesh(
    cloud,
    scalars="radioactivity",
    point_size=10.0,
    render_points_as_spheres=True,
)
plotter.show_axes()
plotter.show()
