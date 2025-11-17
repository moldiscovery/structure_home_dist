"""
A sample workflow
"""


import structure_home


biogps_dir = "/home/gabo/md/build/biogps/install"
flap_dir = "/home/gabo/md/packages/FLAP3-25.01.32-rhel8"

work_dir = "/tmp/structure_home"

pdb_path = "/home/gabo/md/STRUCTURE_HOME/6Z10.cif"
pdb_name = "6z10"

sh = structure_home.StructureHome()

sh.set_flap_path(flap_dir)
sh.set_biogps_path(biogps_dir)
sh.set_work_dir(work_dir)

# sh.load_pdb(pdb_path, pdb_name)
sh.load_cif(pdb_path, pdb_name)

pockets = sh.compute_pockets(pdb_name)

# for pocket in pockets:
    # sh.compute_pocket_mifs(pdb_name, pocket)

# for pocket in pockets:
    # sh.compute_hoh(pdb_name, pocket, save_vida=True)


