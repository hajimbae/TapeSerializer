# TapeSerializer

TapeSerializer is a tool for serializing Ubisoft's TAPE files for Just Dance 2016, Just Dance 2017, Just Dance 2018, Just Dance 2019 and Just Dance 2020 (New-gen) to make them play-able for Old-gen versions of the game.

Back in 2019, I made a serializer and deserializer for myself but after some issues I had with my laptop, I lost all of my scripts.
These scripts are from EkvirJD with my touch on them.

## Installation

You need to download the latest version of [Python](https://www.python.org/downloads/)
In the installation of Python, please select ADD TO %PATH% and finish the installation.

After it's completely done, open CMD with typing CMD in your search bar or just using 
CTRL + R combination to open **Run** and type CMD.

Now, we have to install these extensions to make the serializer work.
Copy paste the commands below on your CMD/Terminal.
```bash
pip install binascii
```
```bash
pip install unidecode
```
and for chinese lyrics:
```bash
pip install hanzidentifier
```

## Usage

Put your new-gen tapes in the same folder as the .py files and run the script that fits your files' 
serialization type. Enter the files name with .ckd at end, press Enter and 
your files are now serialized for Wii, PS3 and Wii U!

## Contributing
For major changes, please open an issue first to discuss what you would like to change.

If you have any other issues, you can join our [Discord server](https://discord.gg/sbRQdVK).

## License
[Polyform Strict](https://polyformproject.org/licenses/strict/1.0.0/)
