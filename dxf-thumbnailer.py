#!usr/local/share/.dxf_thumbnailer_python_venv/bin/python
# -*- coding: utf-8 -*-

# from ezdxf example

import argparse
import sys
import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext, layout, config, pymupdf


# set parser parameters
parser = argparse.ArgumentParser(description='Extract the thubnail from LightBurn files')
parser.add_argument('-i', '--input', type=str, metavar='PATH TO FILE',
                    help='input file to extract thumbnail')
parser.add_argument('-o', '--output', type=str, metavar='PATH TO FILE',
                    help='ouput file to save a jpeg')


# get arguments parameters
args = parser.parse_args()

with open('/tmp/pepito', "a") as f:
    #f.write(args.input)
    f.write(args.output)

def check_args():
    # if not any parameters, exit
    if args.input is None:
        print("No se proporciono el archido de entrada")
        sys.exit(1)
    if args.output is None:
        print("No se proporciono el archido de salida")
        sys.exit(1)
        

def create_thumbnail():
    try:
        doc = ezdxf.readfile(args.input)
    except IOError:
        print(f"Not a DXF file or a generic I/O error.")
        sys.exit(1)
    except ezdxf.DXFStructureError:
        print(f"Invalid or corrupted DXF file.")
        sys.exit(2)

    msp = doc.modelspace()
    backend = pymupdf.PyMuPdfBackend()
    cfg = config.Configuration(
        background_policy=config.BackgroundPolicy.WHITE,
        #color_policy=config.ColorPolicy.BLACK,
    )
    frontend = Frontend(RenderContext(doc), backend, config=cfg)
    frontend.draw_layout(msp)
    page = layout.Page(128, 128, layout.Units.px, margins=layout.Margins.all(2))
    
    png_bytes = backend.get_pixmap_bytes(page, fmt="png", dpi=96)
    with open(args.output, "wb") as fp:
        fp.write(png_bytes)
    
    
check_args()
create_thumbnail()

sys.exit(0)
