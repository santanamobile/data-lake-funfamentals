import os
import shutil
import pandas as pd

def ingest_data(src_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)  # Remove the existing directory

    print(f"Ingesting data from {src_path} to {dest_path}")
    shutil.copytree(src_path, dest_path)

def read_data(file_path):
    print(f"Reading data from {file_path}")
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format")

def perform_data_operations(data, layer):
    print(f"Performing data operations for {layer} layer...")
    # Placeholder logic: Modify this based on the layer
    if layer == "refined":
        # Example: Adding a 'Processed' column to the data
        data['Processed'] = True
    elif layer == "curated":
        # Check if 'FirstName' column exists before applying the operation
        if 'FirstName' in data.columns:
            data['FirstName'] = data['FirstName'].apply(lambda x: x[::-1])

    return data

def main():
    # Set up project structure
    project_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(project_path, "data")
    data_lake_path = os.path.join(project_path, "data-lake")

    # Define layer paths
    raw_path = os.path.join(data_lake_path, "raw")
    refined_path = os.path.join(data_lake_path, "refined")
    curated_path = os.path.join(data_lake_path, "curated")

    # Create layer directories if they don't exist
    for layer_path in [raw_path, refined_path, curated_path]:
        os.makedirs(layer_path, exist_ok=True)

    # Ingest sample datasets to the raw layer
    source_data_path = data_path  # Path to sample datasets
    ingest_data(source_data_path, raw_path)

    # Data operations
    # Iterate through files in the raw layer
    for root, dirs, files in os.walk(raw_path):
        for file in files:
            file_path = os.path.join(root, file)
            data = read_data(file_path)

            # Perform data operations for the refined layer
            refined_data = perform_data_operations(data, layer="refined")

            # Save refined data to the refined layer
            refined_output_path = os.path.join(refined_path, file)
            os.makedirs(os.path.dirname(refined_output_path), exist_ok=True)
            refined_data.to_csv(refined_output_path, index=False)

            # Perform data operations for the curated layer
            curated_data = perform_data_operations(refined_data, layer="curated")

            # Save curated data to the curated layer
            curated_output_path = os.path.join(curated_path, file)
            os.makedirs(os.path.dirname(curated_output_path), exist_ok=True)
            curated_data.to_csv(curated_output_path, index=False)

if __name__ == "__main__":
    main()
