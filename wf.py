"""
A sample workflow
"""


import structure_home


biogps_dir = "/home/user/packages/BioGPS-25.02.12-rhel8"
flap_dir = "/home/user/packages/FLAP3-25.01.32-rhel8"

work_dir = "/tmp/structure_home_test"

pdb_path = "/home/user/STRUCTURE_HOME/5VEW.pdb"
pdb_name = "5vew"

metadata = 'metadata.db'

sh = structure_home.StructureHome()

sh.set_flap_path(flap_dir)
sh.set_biogps_path(biogps_dir)
sh.set_work_dir(work_dir)
sh.set_metadata(metadata)

sh.load_pdb(pdb_path, pdb_name)
# sh.load_cif(pdb_path, pdb_name)

pockets = sh.compute_pockets(pdb_name)

# for pocket in pockets:
    # sh.compute_pocket_mifs(pdb_name, pocket)

sh.compute_hoh(pdb_name, pockets[0])
# for pocket in pockets:
    # sh.compute_hoh(pdb_name, pocket, save_vida=True)


