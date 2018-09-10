# CGAifier

This is a simple Python script based on PILlow. It takes any RGB image and converts it into a CGA palette. This means, at most, the resulting image will have 7 colors in it.

## Install

You'll need to `pip install -r requirements.txt` (or just `pip install Pillow`).

## Running

`python -m CGA [image file] [--scale factor] [--save]`

Supply the path to an image file. Optionally, supply a scaling factor. This scaling factor will be used as a divisor- it will *shrink* the image by that number of times. Bigger numbers mean smaller images. By default, this will open windows containing the resulting images. If you pass the `--save` flag, it will output the resulting images to disk. The image files are named based on the original image name *and* the CGA palette used.

E.g., `python -m CGA foo.jpg --save` will create `foo.0.gif` (CGA mode 0), `foo.1.gif` (CGA mode 1), and `foo.5.gif` (CGA mode 5).

## Examples
### Original
![Original](cocktails.jpg)

### CGA Mode 0
![CGA Palette 0](cocktails.0.gif)

### CGA Mode 1
![CGA Palette 1](cocktails.1.gif)

### CGA Mode 5
![CGA Palette 5](cocktails.5.gif)