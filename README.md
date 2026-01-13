# Structure Home - sample scripts

This package provides some python scripts that use the **structure_home** API to perform various operations on a PDB protein:

- **wf.py** imports a protein into a workspace and computes pockets, HOHs and mifs on it
- **wf_align.py** allows to align a protein and its pocket/water networks on a template structure
- **wf_align_optsel.py** allows to look for the optimal template structure for alignment, out of a set of proteins
- **update_metadata.py** allows to incrementally update the metadata.db file for new GPCR structures from RCSB

## Download FLAP3 and BioGPS

First of all, download the [FLAP3](https://download.moldiscovery.com/FLAP3-25.01.32-rhel8.tar.gz)
and [BioGPS](https://download.moldiscovery.com/BioGPS-25.02.12-rhel8.tar.gz) packages. 
Then:

- unpack them in a local directory;
- provide them with a valid license string.

## Requirements

Structure Home comes as a python package, set up using the **Astral UV** package manager.

To deploy it, a bunch of widespread usage tools should be available in the 
host machine:

- **sqlite3**, to access the metadata DB;
- **Astral UV**, to setup the execution environment

### sqlite3

Install sqlite3 using your standard distribution package manager. 

On Ubuntu, the *libsqlite3-dev* package is required.

### Astral UV

To install Astral UV in your working environment, type:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Check [here](https://docs.astral.sh/uv/getting-started/installation/) for more installation methods.

## Environment setup

Use the **uv** tool to setup the scripts execution environment.
From the main structure_home_dist directory run:

```bash
  uv sync
```

## Usage

Before running the scripts, open them with a text editor and set the following values:

- flap_dir: the path to a valid and licensed FLAP3 installation
- biogps_dir: the path to a valid and licensed BioGPS installation
- work_dir: a writable directory, where output and temporary data will be written

Then, update the path and name of your input proteins.

Finally, from the main structure_home_dist directory run:

```bash
uv run wf.py
```

## Runtime errors 

Here's a comprehensive list of errors that may raise during the scripts execution.

* MISSING_FLAP: the path provided to StructureHome.set_flap_path(), 
  which should point to a valid FLAP3 installation, doesn't exist; 
  verify that the directory is readable and accessible
* MISSING_BIOGPS: the path provided to StructureHome.set_biogps_path(), 
  which should point to a valid BioGPS installation, doesn't exist
  verify that the directory is readable and accessible
* MISSING_METADATA: the path provided to StructureHome.set_metadata(), 
  which should point to a StructureHome metadata.db metadata repository, doesn't exist;
  verify that the path to the metadata.db is valid
* DUPLICATE_PROTEIN: trying to import a protein using a name that already exists.
  The StructureHome repository requires protein to have a unique name. Try to use
  another name.
* MISSING_PROTEIN: trying to use a protein not available in the StructureHome workspace.
  Try to choose the name of a protein that has already been imported.
* MISSING_FLAP_EXE: a command line executable was not found in the provided FLAP3 directory.
  Check your FLAP3 installation.
* MISSING_BIOGPS_EXE: a command line executable was not found in the provided BioGPS directory.
  Check your BioGPS installation.
* GPCR_SUBSET_ERROR: the script couldn't compute the GPCR subset of a protein.
  None of the protein chains is classified according to the GPCR Uniprot Accession Code
  provided in the StructureHome metadata.
  This error may happen because the GPCR Uniprot AC of the protein had been marked as
  deprecated, when the StructureHome metadata was generated.
* NO_GENERIC_NUMBERING: raised when one of the proteins used in an alignment features no 
  generic GPCR residue numbering scheme in GPCRdb. In this case alignment becomes impossible, because
  we have no way to generate a common subset between the two structures.
* COMMON_GNS_ERROR: while aligning a pair of structures, the script was unable 
  to compute a common residues subset between the target and the mobile structures.
  
  The common GNS (which stands for Generic-Numbered Subset) is computed 
  selecting the residues available in both the structures, according to the generic GPCR residue numbering schemes in GPCRdb.
  
  To verify that the two structures are provided with Generic GPCR Residue Numbering: 
  open their _GNS.pdb files in PyMOL, verify that they're not empty.
  Display the Generic Numbers by typing the following command:
  
  ``` label <protein_code> and name CA, b if b != 0.00 else '' ```
  
  Verify that a consistent number of chains.residues are available on both the structures.
* ALIGN_ERROR: the alignment executable raised an error and couldn't output the aligned protein file.
  Run the logged align command line in a new shell, to get further details.
* FIXPDB_ERROR: the fixpdb tool, allowing to filter the protein PDB and to extract various features,
  encountered an error, likely because of a malformed PDB input. Run the logged fixpdb command line
  in a new shell, to get further details.
  
# Structure Home Metadata

This repository contains a file metadata.db, which aggregates GPCR and PDB data 
from various sources:

- a precomputed table of GPCR proteins, in csv format, providing for each structure 
the following properties:
    * 'Uniprot Entry name': the Uniprot class name (HCAR1_HUMAN, ACM2_HUMAN, ...)
    * 'Uniprot AC': the Uniprot accession code (Q9BXC0, P08172, ...)
    * 'PDB ID': the 4-digit protein PDB code
    * 'Class': the GPCR class the protein belongs to. (A, B1, B2, C...)
- various metadata from RCSB.org
- the generic GPCR residue numbering system, provided by GPCRdb
- residue index PDB to UNIPROT mapping, from EMBL
- additional custom residue mappings, from a user provided csv table

## Submission of new public structures

The metadata can be incrementally updated, running the attached script **update_metadata.py**

First of all, add some new GPCR structures to the **RCSB_GPCR_structure_table.csv**, providing for each of them 
an uniprot AC, the corresponding uniprot name, a unique ID and the GPCR class.

Then, open **update_metadata.py** and update the values of the following variables:

* metadata: path to the public GPCR proteins table **RCSB_GPCR_structure_table.csv**
* db_path: path to the destination metadata DB file **metadata.db** 
* custom_mapping: path to the CSV file providing custom PDB to UNIPROT residues mapping **RCSB_GPCR_custom_mapping.csv**

Finally, just run the script from the main project directory:

```
uv run update_metadata.py
```

To use the updated metadata DB file **metadata.db** file, assign its path to the variables **metadata**
 available in the various workflow scripts.
 
## Submission of proprietary and custom structures

The script also allows to store the information required to work on proprietary and custom structures, 
whose metadata is not available on public repositories.

Add the required information to the **internal_GPCR_structure_table.csv** file. 

For each structure, the following data is required:

* **PDB ID**: a unique protein identifier.
* **Chain**: the code of the protein GPCR chain
* **Uniprot AC**: the uniprot code of the GPCR chain. Required to infer the generic chain residues numbering.
* **Uniprot entry name**: the uniprot name of the GPCR chain
* **Class**: the class of the protein GPCR chain

Then, run again the **update_metadata.py** script:

```
uv run update_metadata.py
```

Once again, ensure that the resulting **metadata DB** file is in use, assigned to the 
variables **metadata** occuring in the various workflow scripts.
