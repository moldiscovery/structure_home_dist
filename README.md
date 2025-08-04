# Structure Home - sample scripts

This package provides some python scripts that use the **structure_home** API to perform various operations on a PDB protein:

- **wf.py** imports a protein into a workspace and computes pockets, HOHs and mifs on it
- **wf_align.py** allows to align a protein on a target

## Download FLAP3 and BioGPS

First of all, download the [FLAP3](https://download.moldiscovery.com/FLAP3-25.01.32-rhel8.tar.gz)
and [BioGPS](https://download.moldiscovery.com/BioGPS-25.01.14-rhel8.tar.gz) packages. Then:

- unpack them in a local directory;
- provide them with a valid license string.

## Requirements

Structure Home comes as a python package, set up using the python **setuptools** utilities.

To deploy it, a bunch of widespread usage tools should be available in the 
host machine:

- sqlite3, to access the metadata DB;
- pyenv, allowing to automate the installation of the right python interpreter version;
- pipenv, which automates the setup of a python execution environment.

### sqlite3

Install it using your standard distribution package manager. 

On Ubuntu, the *libsqlite3-dev* package is required.

### pyenv

Run the following command from the shell:

```
curl -fsSL https://pyenv.run | bash
```

Three more bash commands are required to set it up, listed [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#bash).

Full install instruction available in the [pyenv official documentation](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

### pipenv

Install it using the standard distribution package manager, or using *pip*:

```
pip install pipenv
```

## Environment setup

Use the pipenv tool to setup the scripts execution environment.
From the main structure_home_dist directory run:

```
  pipenv sync
```

## Usage

Before running the scripts, open them with a text editor and set the following values:

- flap_dir: the path to a valid and licensed FLAP3 installation
- biogps_dir: the path to a valid and licensed BioGPS installation
- work_dir: a writable directory, where output and temporary data will be written

Then, update the path and name of your input proteins.

Finally, activate the virtual environment and run the script:

```
pipenv shell
python structure_home_dist/wf.py
```
