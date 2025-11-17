"""
A sample workflow: alignment of two A2A GPCRs
"""

import shutil

import structure_home


biogps_dir = "/home/gabo/md/build/biogps/install"
flap_dir = "/home/gabo/md/packages/FLAP3-25.01.32-rhel8"

work_dir = "/tmp/structure_home"

target_path = "/home/gabo/md/STRUCTURE_HOME/6X18.pdb"
target_name = "6x18"

sh = structure_home.StructureHome()

sh.set_flap_path(flap_dir)
sh.set_biogps_path(biogps_dir)
sh.set_work_dir(work_dir)

rt_path = "/home/gabo/md/STRUCTURE_HOME/5VEW.pdb"
rt_name = "5vew"

shutil.rmtree(work_dir, ignore_errors=True)

if not sh.protein_avail(target_name):
    sh.load_pdb(target_path, target_name)

if not sh.protein_avail(rt_name):
    sh.load_pdb(rt_path, rt_name)

# compute some data on the structure that will be aligned

pockets = sh.compute_pockets(rt_name)

# sh.compute_hoh(rt_name, pockets[0])

# for pocket in pockets:
#     sh.compute_hoh(rt_name, pocket)

# now, align the structure and its features

rmsd = sh.align(rt_name, target_name)

print("Alignment RMSD = ", rmsd)

# for p in sh.protein_pockets(rt_name):
    # sh.compute_rt_pocket_mifs(rt_name, target_name, p)
