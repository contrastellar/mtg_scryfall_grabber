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

## TODO

Additional functions need to be implimented, however -- an example implementation of this library is given in `./example/` under `msfg.py`

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
The license is covered under the file [license.md](https://github.com/Contrastellar/mtg-scryfall-grabber/blob/main/license.md).

In essence, please do not use this software for commercial (for profit) means. This library is provided as is, modifications to the source code are allowed. This is to follow the Wizards of the Coast's Fan Content Policy.