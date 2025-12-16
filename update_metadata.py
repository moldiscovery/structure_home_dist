import structure_home

metadata = "Updated_List_PDB_structures_20251121.csv"
db_path = "metadata.db"
custom_mapping = "custom_mapping.csv"
structure_home.update_metadata(
    db_path,
    metadata,
    custom_mapping,
    incremental=True)

# internal_data = ""
# structure_home.add_internal_codes(internal_data, db_path)
