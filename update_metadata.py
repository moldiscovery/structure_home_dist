import structure_home

# incremental metadata update. Add rows to the GPCR metadata CSV table and relaunch.
metadata = "Updated_List_PDB_structures_20251121.csv"
db_path = "metadata.db"
custom_mapping = "custom_mapping.csv"
structure_home.update_metadata(
    db_path,
    metadata,
    custom_mapping,
    incremental=True)

# incremental insertion of custom structures
internal_data = "Custom_GPCR_table.csv"
internal_custom_mapping = "internal_custom_mapping.csv"
structure_home.add_internal_codes(
    db_path,
    internal_data,
    internal_custom_mapping)
