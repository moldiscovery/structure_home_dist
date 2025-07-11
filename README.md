# Structure Home - sample scripts

Usage examples of the structure_home API

## Download FLAP3 and BioGPS

First of all, download the [FLAP3](https://download.moldiscovery.com/FLAP3-25.01.32-rhel8.tar.gz)
and [BioGPS](https://download.moldiscovery.com/BioGPS-25.01.14-rhel8.tar.gz) packages. Then:

- unpack them in a local directory
- provide them with a valid license
- update the Structure Home scripts, as described in section 'Usage'

## Environment setup

To setup the scripts execution environment, use the **pipenv** tool.

- create a working directory
- setup into it a python environment

```
  mkdir structure_work && cd structure_work
  pipenv shell
```

## Usage

Now, a python script can *import structure_home* and use its API.

A basic workflow implementation is available in structure_home/script/wf.py.

Modify the source code, set the following values:

- flap_dir: a directory containing a valid and licensed FLAP3 installation, providing flapwater and flapdock
- biogps_dir: the path to a valid and licensed BioGPS installation, providing fixpdb and flapsite
- work_dir: a writable directory, where output and temporary data will be written
- pdb_path: the path to a pdb containing the protein to be processed
- pdb_name: the PDB code, or a string ID, of the protein to be processed

Then, activate the virtual environment and run the script:

```
cd structure_work
pipenv shell
python structure_home_dist/wf.py
```
