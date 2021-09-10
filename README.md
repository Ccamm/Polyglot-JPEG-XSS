# XSS JPEG Tool (xjt)

Generates a polyglot JPEG with a javascript payload to bypass CSP. How it works is treating the header bytes of an image (`0xFF 0xD8 0xFF 0xE0`) as a variable name and using the comment within the JPEG to store the value for the variable. For more information about how it works please read https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs.

Simply put, if you see a similar CSP as shown below and you can upload JPEG images to the webserver you can bypass the CSP to exploit XSS vulnerabilities.

```
Content-Security-Policy: default-src 'self';
```

## Installation

**`xjt` requires to have ExifTool installed!**

```
python3 setup.py install
```

## Usage

```
usage: xjt [-h] [--width WIDTH] [--height HEIGHT] [-o OUTPUT_FILE] [-p PAYLOAD]

Generates a polyglot XSS jpeg that can be used to bypass CSP on websites if image uploads are allowed

optional arguments:
  -h, --help            show this help message and exit
  --width WIDTH         Change the width of the output image to bypass dimension restrictions
  --height HEIGHT       Change the height of the output image to bypass dimension restrictions
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Where to save the payload JPEG. Save to xjt.jpg by default.
  -p PAYLOAD, --payload PAYLOAD
                        The javascript code you want to execute. DO NOT USE ' IN YOUR PAYLOAD! By default it runs
                        alert("XSS EXPLOITED!");.
```
