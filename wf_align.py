"""
A sample workflow: alignment of two A2A GPCRs
"""


import structure_home


flap_dir = "/home/gabo/md/packages/FLAP3-25.01.1-rhel8"
biogps_dir = "/home/gabo/md/build/qt6_biogps/install"

work_dir = "/tmp/structure_home"

target_path = "/home/gabo/md/STRUCTURE_HOME/align_test/5wf5.pdb"
target_name = "5wf5"

sh = structure_home.StructureHome()

sh.set_flap_path(flap_dir)
sh.set_biogps_path(biogps_dir)
sh.set_work_dir(work_dir)

sh.load_pdb(target_path, target_name)

pdb_path = "/home/gabo/md/STRUCTURE_HOME/align_test/7utz.pdb"
pdb_name = "7utz"

sh.load_align_pdb(pdb_path, pdb_name, target_name)

# pockets and HOH on aligned

pockets = sh.compute_pockets(pdb_name)

for pocket in pockets:
    sh.compute_pocket_mifs(pdb_name, pocket)

# for pocket in pockets:
#     sh.compute_hoh(pdb_name, pocket)


