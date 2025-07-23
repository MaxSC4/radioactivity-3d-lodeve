from src.loader import load_points_csv
from src.visualizer import create_point_cloud, show_point_cloud

# Load geospatial radioactivity data
df = load_points_csv("data/example.csv")

# Create and display point cloud
cloud = create_point_cloud(df)
show_point_cloud(cloud)
