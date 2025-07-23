from src.loader import load_points_csv
from src.visualizer import create_point_cloud, show_point_cloud
from src.interpolator import interpolate_volume
import pyvista as pv

# === Load and visualize surface data ===
df = load_points_csv("data/example.csv")
cloud = create_point_cloud(df)
show_point_cloud(cloud)

# === Interpolate in 3D volume ===
volume_grid = interpolate_volume(df, grid_spacing=25.0, depth=500.0)

# === Display interpolated volume ===
plotter = pv.Plotter()
plotter.add_mesh(cloud, scalars="radioactivity", point_size=10.0, render_points_as_spheres=True)
plotter.add_volume(volume_grid, scalars="radioactivity", opacity="sigmoid", cmap="viridis")
plotter.show_axes()
plotter.show()
