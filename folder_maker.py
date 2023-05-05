import os
import yaml
import gooey

# Define the folder hierarchy YAML file
hierarchy_file = './folder_references.yaml'

# Load the folder hierarchy from the YAML file
with open(hierarchy_file) as f:
    folder_hierarchy = yaml.safe_load(f)

@gooey.Gooey
def create_folders():
    '''Set up the GUI and parse the command line arguments.
    Read folder hierarchy options from the YAML'''
    # Define the program description and the available options
    parser = gooey.GooeyParser(description='Create folder hierarchy')
    parser.add_argument('location', help='Location to create folder hierarchy')
    parser.add_argument('option', choices=['Riegl', 'QC', 'Bridge Resources'], help='Select an option')

    # Parse the command line arguments
    args = parser.parse_args()

    # Get the folder hierarchy for the selected option
    selected_hierarchy = folder_hierarchy[args.option]

    # Create the folder hierarchy based on the selected option
    create_folder_hierarchy(args.location, selected_hierarchy)

def create_folder_hierarchy(root_folder, folder_structure):
    """
    Recursively create folder hierarchy based on folder_structure dictionary.
    :param root_folder: The root folder of the folder hierarchy.
    :param folder_structure: A dictionary representing the folder hierarchy structure.
    """
    for folder_name, subfolders in folder_structure.items():
        folder_path = os.path.join(root_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        if subfolders:
            create_folder_hierarchy(folder_path, subfolders)


if __name__ == '__main__':
    create_folders()
