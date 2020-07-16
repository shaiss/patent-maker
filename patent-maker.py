import inkex       # Required
import simplestyle # will be needed here for styles support
import os          # here for alternative debug method only - so not usually required
# many other useful ones in extensions folder. E.g. simplepath, cubicsuperpath, ...

from math import cos, sin, radians

class Myextension(inkex.Effect): # choose a better name
    
    def __init__(self):
        " define how the options are mapped from the inx file "
        inkex.Effect.__init__(self) # initialize the super class

    def add_text(self, node, text, position, text_height=12):
    #Create and insert a single line of text into the svg under node.
        line_style = {'font-size': '%dpx' % text_height, 'font-style':'normal', 'font-weight': 'normal',
            'fill': '#F6921E', 'font-family': 'Bitstream Vera Sans,sans-serif',
            'text-anchor': 'middle', 'text-align': 'center'}
        line_attribs = {inkex.addNS('label','inkscape'): 'Annotation',
            'style': simplestyle.formatStyle(line_style),
            'x': str(position[0]),
            'y': str((position[1] + text_height) * 1.2)
        }
        line = inkex.etree.SubElement(node, inkex.addNS('text','svg'), line_attribs)
        line.text = text

    def effect(self):
        topgroup = inkex.etree.SubElement(self.current_layer, 'g', g_attribs )
    

        note = "poop"
        text_height = 12
        # position above
        y = - 22
        self.add_text(topgroup, note, [0,y], text_height)

if __name__ == '__main__':
    Myextension().run()