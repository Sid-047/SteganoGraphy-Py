# SteganoGraphy-Py
> Here's Steganography Implementation via Python

![CoreStuff](https://github.com/Sid-047/SteganoGraphy-Py/blob/main/ConceptualStuff/CoreStuff.jpg)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Sid-047/SteganoGraphy-Py.svg)](https://github.com/Sid-047/SteganoGraphy-Py/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/Sid-047/SteganoGraphy-Py.svg)](https://github.com/Sid-047/SteganoGraphy-Py/issues)
[![GitHub Forks](https://img.shields.io/github/forks/Sid-047/SteganoGraphy-Py.svg)](https://github.com/Sid-047/SteganoGraphy-Py/network/members)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

1. Clone the Repository:
   ```sh
   git clone https://github.com/Sid-047/SteganoGraphy-Py.git
   ```

## Usage

1. Navigate to the Project Directory:
    ```sh
    cd SteganoGraphy-Py
    ```

2. Install Dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Let's Embed Data into an Image
    ```sh
    python imgGeneration.py <img byteDepth> <inputImg Path> <inFile Path> <outImg Final Path>
    ```
    So, this is how it Looks like
   ```sh
    python imgGeneration.py 2 "Workin'Objects\workin'Img.png" "Workin'Objects\embedStuff\inAud.mp3" outImg.tiff
    ```
    Here it Comes!

4. Let's Extract the Embedded Data OUT
    ```sh
    python imgExtraction.py <embedImg File>
    ```
    Once again, Here's an Example
   ```sh
    python imgExtraction.py outImg.tiff
    ```
    Alter the line of Code or Paste the queryList from the Previous Stage
   
5. Yep! That is it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.