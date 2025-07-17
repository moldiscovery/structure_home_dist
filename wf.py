"""
A sample workflow
"""


import structure_home


biogps_dir = "/home/gabo/md/packages/BioGPS-25.01.14-rhel8"
flap_dir = "/home/gabo/md/packages/FLAP3-25.01.32-rhel8"

work_dir = "/tmp/structure_home"

pdb_path = "/home/gabo/md/STRUCTURE_HOME/scripttest6zdv/A2A6zdv_input.pdb"
pdb_name = "6zdv"

sh = structure_home.StructureHome()

sh.set_flap_path(flap_dir)
sh.set_biogps_path(biogps_dir)
sh.set_work_dir(work_dir)

sh.load_pdb(pdb_path, pdb_name)

pockets = sh.compute_pockets(pdb_name)

# for pocket in pockets:
#     sh.compute_pocket_mifs(pdb_name, pocket)

for pocket in pockets:
    sh.compute_hoh(pdb_name, pocket)


