"""
A sample workflow: alignment of two A2A GPCRs
"""


import structure_home


flap_dir = "/home/gabo/md/packages/FLAP3-25.01.29-rhel8/"
biogps_dir = "/home/gabo/md/build/qt6_biogps/install"

work_dir = "/tmp/structure_home"

target_path = "/home/gabo/md/STRUCTURE_HOME/align_test/5wf5.pdb"
target_name = "5wf5"

sh = structure_home.StructureHome()

sh.set_flap_path(flap_dir)
sh.set_biogps_path(biogps_dir)
sh.set_work_dir(work_dir)

rt_path = "/home/gabo/md/STRUCTURE_HOME/align_test/7utz.pdb"
rt_name = "7utz"

sh.load_pdb(target_path, target_name)
sh.load_pdb(rt_path, rt_name)

# compute some data on the structure that will be aligned

pockets = sh.compute_pockets(rt_name)

sh.compute_hoh(rt_name, '001_7utz') # pockets[0])

# for pocket in pockets:
#     sh.compute_hoh(rt_name, pocket)

# now, align the structure and its features

sh.align(rt_name, target_name)




