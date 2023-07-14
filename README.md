# mtg-scryfall-grabber
[![Pylint](https://github.com/Contrastellar/mtg_scryfall_grabber/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/Contrastellar/mtg_scryfall_grabber/actions/workflows/pylint.yml)

MTG-Scryfall-Grabber (MSG) is a Python library and module for scraping and organizing data from the Scryfall Rest-API.

`conda` is not _needed_ but a sample `environment.yaml` is provided for the bare minimums you need to run in your own conda enviornment.

## Installation

Please go to [Releases](https://github.com/Contrastellar/mtg-scryfall-grabber/releases) for the latest directories.

Additionally, this can be installed from pip using

```bash
python3 -m pip install mtg-scryfall-grabber
```


## Usage

After installing via pip using 
```bash
python3 -m pip install --upgrade mtg-scryfall-grabber
```

The functions from `mtg_scryfall_grabber.py` can be invoked using
```python
import mtg_scryfall_grabber
```


## Quickstart (/w conda)


### conda install

`conda` can be installed from [here](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)

### Once conda is installed

1. Clone the following repo
```
https://github.com/Contrastellar/mtg_scryfall_grabber
```

2. Navigate to the repo
```sh
cd ./mtg_scryfall_grabber/
```

3. Install the environment, where `$NAME_OF_ENVIRONMENT` is any name, or is omitted altogether, as one is given in the file.
```sh
conda env create --file ./environment.yaml --name $NAME_OF_ENVIRONMENT
```

4. Activate the environment
```sh
conda activate $NAME_OF_ENVIRONMENT
```

5. Navigate to the `./example/` directory
```sh
cd ./example/
```

6. Run the following OS dependant command to download the information for the set "Phyrexia, All Will Be One"
### PowerShell
```bash
py msfg.py ONE -c -p
```

### Unix 
```bash
python3 msfg.py ONE -c -p
```


## Quickstart w/o conda
To get started quickly, one must install Python 3 (version 3.8 or greater).

Once having completed Python 3 installation for your Operating System, running the following command

### PowerShell ---
```bash
py -m pip install --upgrade mtg-scryfall-grabber
```

### MacOS/UNIX Terminal/bash ---
```bash
python3 -m pip install --upgrade mtg-scryfall-grabber
```

This will install mtg-scryfall-grabber's `mtg_scryfall_grabber` library, to be imported and used in your own Python Module if so desired.
From here, downloading (either from releases, or from [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository) the `example/msfg.py` file. Once this is done, the following steps can be taken to 'quickstart' downloading information from the Scryfall API.

1. In your commandline (henceforth the CLI), navigate to the directory.
```bash
cd $MTG_SCRYFALL_GRABBER_DOWNLOAD_LOCATION/example/
```

2. Run the following command to download the information for the set "Phyrexia, All Will Be One"
### PowerShell
```bash
py msfg.py ONE -c -p
```

### MacOS/UNIX Terminal/Bash
```bash
python3 msfg.py ONE -c -p
```

In `./example/`, this will create a directory named "output", which will contain a `.json` file named like `ONE_name_price_$(TIME).json` -- where it is compiled by set code + unix time.


## TODO

Nothing else major needs to be done at this point, however polishing and code testing will be implemented to this library before this is considered a full, ready-to-be-used in production v.1 release.

Additional functions need to be implimented, however -- an example implementation of this library is given in `./example/` under `msfg.py`. This implementation can also be treated as the "primary" method of using this library, in order to generate JSON to be used inside Excel spreadsheets or another spreadsheet program.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
The license is covered under the file [license.md](https://github.com/Contrastellar/mtg-scryfall-grabber/blob/main/license.md).

In essence, please do not use this software for commercial (for profit) means. This library is provided as is, modifications to the source code are allowed. This is to follow the Wizards of the Coast's (WotC) Fan Content Policy. All modifications should be done in accordance with the WotC Fan Content Policy.
