# mtg-scryfall-grabber

MTG-Scryfall-Grabber (MSG) is a Python library and module for scraping and organizing data from the Scryfall Rest-API.

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

The functions from `grab_cards.py` can be invoked using
```python
import grab_cards
```

At the moment, two functions are currently working.
`grab_cards()` and `grab_prices()`, these two, respectively, grab card names sorted by collector ID, and card prices, sorted by Collector ID. This is intended to be imported into spreadsheet software such as Microsoft Excel, in order to be sorted by things like Collector Number, Name, or Price.

## Quickstart
To get started quickly, one must install Python 3 (version 3.8 or greater).

Once having completed Python 3 installation for your Operating System, running the following command

### WINDOWS PowerShell ---
```bash
py -m pip install --upgrade mtg-scryfall-grabber
```

### MacOS/UNIX Terminal/bash ---
```bash
python3 -m pip install --upgrade mtg-scryfall-grabber
```

This will install mtg-scryfall-grabber's `grab-card` library, to be imported and used in your own Python Module if so desired.

From here, downloading (either from releases, or from [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository) the `example/msfg.py` file. Once this is done, the following steps can be taken to 'quickstart' downloading information from the Scryfall API.

1. In your commandline (henceforth the CLI), navigate to the directory.
```bash
cd $MTG_SCRYFALL_GRABBER_DOWNLOAD_LOCATION/example/
```
2. Run the following command to download the information for "Phyrexia, All Will Be One"
### WINDOWS PowerShell
```bash
py msfg.py ONE
```

### MacOS/UNIX Terminal/Bash
```bash
python3 msfg.py ONE
```

In `./example/`, this will create a directory named "output", which will contain a `.json` file named `Phyrexia: All Will Be One_card_name_info.json`

## TODO

Additional functions need to be implimented, however -- an example implementation of this library is given in `./example/` under `msfg.py`. This implementation can also be treated as the "primary" method of using this library, in order to generate JSON to be used inside Excel spreadsheets.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
The license is covered under the file [license.md](https://github.com/Contrastellar/mtg-scryfall-grabber/blob/main/license.md).

In essence, please do not use this software for commercial (for profit) means. This library is provided as is, modifications to the source code are allowed. This is to follow the Wizards of the Coast's Fan Content Policy.