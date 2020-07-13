#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Example of extensions template for inkscape
'''
# standard library
import locale, os, sys, tempfile, webbrowser, math
try:
    from subprocess import Popen, PIPE
    bsubprocess = True
except:
    bsubprocess = False
# local library
import inkex, simplestyle, simpletransform

 
patenturl ="poop4"

#self.options.patenturl

f = open("demofile4.txt", "w")
f.write(patenturl)
f.close()

#SVG element generation routine
def draw_SVG_square((w,h), (x,y), parent):

    style = {   'stroke'        : 'none',
                'stroke-width'  : '1',
                'fill'          : '#000000'
            }
                
    attribs = {
        'style'     : simplestyle.formatStyle(style),
        'height'    : str(h),
        'width'     : str(w),
        'x'         : str(x),
        'y'         : str(y)
            }
    circ = inkex.etree.SubElement(parent, inkex.addNS('rect','svg'), attribs )