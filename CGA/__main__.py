import sys
from argparse import ArgumentParser
import os.path
from PIL import Image

parser = ArgumentParser(prog="CGA Converter",
  description="""
  Convert a full color image into one of the commonly used CGA palettes
  """)
parser.add_argument('source', help='The source image', type=str)
parser.add_argument('--crop', type=str, help='Crop the image before scaling, as a tuple, x,y,w,h', default="")
parser.add_argument('--scale', type=float, help='Shrink the image by this factor', default=1)
parser.add_argument('--save', action="store_true", default=False, help="Save the image to a file")
args = parser.parse_args()

palette0 = Image.open('CGA/cga0.gif')
palette1 = Image.open('CGA/cga1.gif')
palette5 = Image.open('CGA/cga5.gif')

fp = os.path.abspath(args.source)
name_part,_ = os.path.splitext(os.path.basename(fp))

img = Image.open(fp)
w = int(img.width / args.scale)
h = int(img.height / args.scale)
img = img.resize((w,h))


p0 = img.quantize(7, method=3, palette=palette0, kmeans=7)
p1 = img.quantize(7, method=3, palette=palette1, kmeans=7)
p5 = img.quantize(7, method=3, palette=palette5, kmeans=7)

if args.save:
  p0.save('%s.0.gif' % name_part)
  p1.save('%s.1.gif' % name_part)
  p5.save('%s.5.gif' % name_part)
else:
  p0.show()
  p1.show()
  p5.show()