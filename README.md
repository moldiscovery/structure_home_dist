# Structure Home - sample scripts

Usage examples of the structure_home API

## Environment setup

To setup the scripts execution environment, use the **pipenv** tool.
- create a working directory
- setup into it a python environment

```
  mkdir structure_work && cd structure_work
  pipenv shell
```

## Install the library

From the directory created in the step above, 
install the structure_home library, provided as a .tar.gz file, so that it can 
be imported in the sample scripts:

```
pip install structure_home-0.2.0.tar.gz
```

## Usage

Now, a python script can *import structure_home* and use its API.

A basic workflow implementation is available in structure_home/script/wf.py.

Modify the source code, set the following values:
- flap_dir: a directory containing a valid and licensed FLAP3 installation, providing flapwater and flapdock
- biogps_dir: the path to a valid and licensed BioGPS installation, providing fixpdb and flapsite
- work_dir: a writable directory, where output and temporary data will be written
- pdb_path: the path to a pdb containing the protein to be processed

Then, activate the virtual environment and run the script:

```
cd structure_work
pipenv shell
python structure_home_dist/wf.py
```
