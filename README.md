# GQRX2SDR#

This tool has been written to support my undergraduate final year project with Imperial College. I had a need to go between the GQRX *.RAW and the SDR# *.WAV formats so put this together. I hope it is of use to someone!

Useful links:
* [gqrx] - Linux and GNURadio based SDR software
* [sdrsharp] - Windows based SDR software  
* [gqrxd] - Description of conversion
* [soxcmd] - Raw command in use

# Usage
Copy the *sox_convert.py* into the folder containing the *.RAW files to be converted. The script will create an output folder *soxoutput/* that will contain the *.WAV files.
### To process ALL the files in the current directory:
```bash
./sox_convert.py -a
``` 

### To process a single file:
```bash
./sox_convert.py -i /my/file/here
``` 

### To open a file selection dialog (no args):
```bash
./sox_convert.py
``` 

![Beep beep](/D8YZ5G.png?raw=True)
Beep beep!

License
----
MIT
*Jonathan Rawlinson 2018*

[//]: # 
   [gqrx]: <http://gqrx.dk/>
   [sdrsharp]: <https://airspy.com/download/>
   [gqrxd]: <https://www.bastibl.net/gqrx-for-digital-signals/>
   [soxcmd]: <https://gist.github.com/sam210723/4a194903e66f5d0147782bfbcea79f80>
   
