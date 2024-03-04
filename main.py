# Import necessary libraries
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
    if layer == "refined":
        data['Processed'] = True
    elif layer == "curated":
        if 'FirstName' in data.columns:
            data['FirstName'] = data['FirstName'].apply(lambda x: x[::-1])
    elif layer == "enriched":
        # Placeholder logic: Add new data operations for the enriched layer
        pass

    return data

def main():
    project_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(project_path, "data")
    data_lake_path = os.path.join(project_path, "data-lake")

    raw_path = os.path.join(data_lake_path, "raw")
    refined_path = os.path.join(data_lake_path, "refined")
    curated_path = os.path.join(data_lake_path, "curated")
    enriched_path = os.path.join(data_lake_path, "enriched")

    for layer_path in [raw_path, refined_path, curated_path, enriched_path]:
        os.makedirs(layer_path, exist_ok=True)

    source_data_path = data_path
    ingest_data(source_data_path, raw_path)

    for root, dirs, files in os.walk(raw_path):
        for file in files:
            file_path = os.path.join(root, file)
            data = read_data(file_path)

            refined_data = perform_data_operations(data, layer="refined")
            refined_output_path = os.path.join(refined_path, file)
            os.makedirs(os.path.dirname(refined_output_path), exist_ok=True)
            refined_data.to_csv(refined_output_path, index=False)

            curated_data = perform_data_operations(refined_data, layer="curated")
            curated_output_path = os.path.join(curated_path, file)
            os.makedirs(os.path.dirname(curated_output_path), exist_ok=True)
            curated_data.to_csv(curated_output_path, index=False)

            enriched_data = perform_data_operations(curated_data, layer="enriched")
            enriched_output_path = os.path.join(enriched_path, file)
            os.makedirs(os.path.dirname(enriched_output_path), exist_ok=True)
            enriched_data.to_csv(enriched_output_path, index=False)

if __name__ == "__main__":
    main()
