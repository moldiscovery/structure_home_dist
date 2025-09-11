# Structure Home - sample scripts

This package provides some python scripts that use the **structure_home** API to perform various operations on a PDB protein:

- **wf.py** imports a protein into a workspace and computes pockets, HOHs and mifs on it
- **wf_align.py** allows to align a protein on a target
- **wf_align_optsel.py** allows to look for the optimal alignment target, out of a set of proteins

## Download FLAP3 and BioGPS

First of all, download the [FLAP3](https://download.moldiscovery.com/FLAP3-25.01.32-rhel8.tar.gz)
and [BioGPS](https://download.moldiscovery.com/BioGPS-25.01.15-rhel8.tar.gz) packages. Then:

- unpack them in a local directory;
- provide them with a valid license string.

## Requirements

Structure Home comes as a python package, set up using the **Astral UV** package manager.

To deploy it, a bunch of widespread usage tools should be available in the 
host machine:

- **sqlite3**, to access the metadata DB;
- **Astral UV**, to setup the execution environment

### sqlite3

Install it using your standard distribution package manager. 

On Ubuntu, the *libsqlite3-dev* package is required.

### Astral UV

To install it in your working environment, type:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Chech [here](https://docs.astral.sh/uv/getting-started/installation/) for more installation methods.

## Environment setup

Use the **uv** tool to setup the scripts execution environment.
From the main structure_home_dist directory run:

```
  uv sync
```

## Usage

Before running the scripts, open them with a text editor and set the following values:

- flap_dir: the path to a valid and licensed FLAP3 installation
- biogps_dir: the path to a valid and licensed BioGPS installation
- work_dir: a writable directory, where output and temporary data will be written

Then, update the path and name of your input proteins.

Finally, from the main structure_home_dist directory run:

```
uv run wf.py
```
