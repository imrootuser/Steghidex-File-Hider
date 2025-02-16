# StegHideX - File Hider

## Overview
StegHideX is a Python-based steganography tool that allows users to **hide files inside images** securely. This tool is useful for cybersecurity professionals, ethical hackers, and privacy enthusiasts who need to conceal sensitive data within images.

## Features
- Hide any file inside an image using steganography
- Extract hidden files from images
- Password protection for added security
- Supports multiple image formats (JPG, PNG, BMP)
- CLI-based for easy integration into scripts

## Installation
### Prerequisites
Ensure you have Python installed (version 3.x recommended). You can download it from [Python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
git clone https://github.com/imrootuser/steghidex.git
cd steghidex
```

### Install Required Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Hide a File Inside an Image
```bash
python steghidex.py hide -i cover.jpg -f secret.txt -o output.png -p yourpassword
```
Example:
```bash
python steghidex.py hide -i image.png -f confidential.pdf -o hidden.png -p mysecurepassword
```

### Extract a Hidden File
```bash
python steghidex.py extract -i hidden.png -p yourpassword
```

## Example Output
```
[+] Hiding secret.txt inside cover.jpg...
[+] Successfully saved as output.png
```

```
[+] Extracting hidden file from hidden.png...
[+] Successfully extracted as secret.txt
```

## Contribution
Feel free to contribute by opening an issue or creating a pull request!

## Disclaimer
This tool is for **educational and authorized security testing purposes only**. Unauthorized use for data concealment may be illegal in some jurisdictions. Use responsibly.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
**Author:** Root User 
**GitHub:** [Root User](https://github.com/imrootuser)
