"""
A sample workflow: alignment of two A2A GPCRs
"""

import shutil
import re
import os
import itertools

import structure_home


biogps_dir = "/home/gabo/md/packages/BioGPS-25.01.24-rhel8"
flap_dir = "/home/gabo/md/packages/FLAP3-25.01.32-rhel8"

work_dir = "/tmp/structure_home/test_align_optsel"

# a directory containing the alignment targets
targets_dir = "/tmp/bench_sh/repo"

generic_re = re.compile('(.{4})\\.pdb')
classc_re = re.compile('.+_(.{4})[A-Z]?\\.pdb')
target_re = generic_re

sh = structure_home.StructureHome()

sh.set_flap_path(flap_dir)
sh.set_biogps_path(biogps_dir)
sh.set_work_dir(work_dir)

targets = os.listdir(targets_dir)

t_paths = [
    os.path.join(targets_dir, f)
    for f in targets]
t_codes = [
    target_re.match(f).group(1)
    for f in targets]

for target, code in zip(t_paths, t_codes):
    sh.load_pdb(target, code)

# compute some data on the structure that will be aligned

opt, rmsd = sh.optimal_alignment_template(t_codes)

print("Optimal template = ", opt)
print("Optimal alignment RMSD = ", rmsd)





