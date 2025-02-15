import os

# Define the directory structure
project_name = "my_data_viz_project"
dirs = [
    f"{project_name}/data",
    f"{project_name}/plots",
    f"{project_name}/src"
]

# Create directories
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Create placeholder files
with open(f"{project_name}/README.md", "w") as f:
    f.write("# My Data Visualization Project\nThis project contains various visualizations for qualitative and quantitative data.\n")

with open(f"{project_name}/requirements.txt", "w") as f:
    f.write("matplotlib\nseaborn\npandas\nstreamlit\n")

print("Project structure created successfully!")
