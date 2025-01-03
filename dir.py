import os

# Define root directory
root_dir = "NorthwellPracticeDWH_SSIS"

# Define the directory structure
structure = {
    root_dir: [
        "NorthwellPracticeDWH.sln",  # Solution file
        "NorthwellPracticeDWH.dtproj",  # SSIS project file
        "NorthwellPracticeDWH.database",  # Database metadata file
        "README.md",  # High-level documentation
        ".gitignore"  # Git ignore file
    ],
    f"{root_dir}/Project1_ClaimsDataAnalysis": [
        "Documentation/README.md",
        "Documentation/WorkflowDiagram.png",
        "Packages/LoadClaims.dtsx",
        "Packages/TransformClaims.dtsx",
        "Packages/LoadToFactDim.dtsx",
        "Connections/ClaimsDatabase.dtsConfig",
        "Connections/ClaimsFlatFile.dtsConfig",
        "Logs/ClaimsETLLog.txt",
        "Samples/SampleClaims.csv",
        "Samples/SampleClaimStatus.csv"
    ],
    f"{root_dir}/Project2_SalesDataAnalysis": [
        "Documentation/README.md",
        "Documentation/WorkflowDiagram.png",
        "Packages/LoadSales.dtsx",
        "Packages/TransformSales.dtsx",
        "Packages/LoadToFactDim.dtsx",
        "Connections/SalesDatabase.dtsConfig",
        "Connections/SalesFlatFile.dtsConfig",
        "Logs/SalesETLLog.txt",
        "Samples/SampleSales.csv",
        "Samples/SampleRegions.csv"
    ],
    f"{root_dir}/Shared": [
        "CommonPackages/LoggingFramework.dtsx",
        "CommonPackages/EmailNotification.dtsx",
        "CommonConnections/SharedSQLConnection.dtsConfig",
        "Logs/SharedExecutionLog.txt"
    ]
}

# Function to create directories and files
def create_structure(base_dir, structure):
    for folder, files in structure.items():
        # Create the main folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)
        for item in files:
            item_path = os.path.join(folder, item)
            if "/" in item:  # Nested directory/file
                dir_path = os.path.dirname(item_path)
                os.makedirs(dir_path, exist_ok=True)  # Ensure the directory exists
            if "." in os.path.basename(item):  # It's a file
                with open(item_path, "w") as f:
                    f.write("")  # Create an empty file

# Run the script
create_structure(".", structure)

print(f"Directory structure created at: {os.path.abspath(root_dir)}")
