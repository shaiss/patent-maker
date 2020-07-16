#!/usr/bin/env python
#-*- coding: utf-8 -*-

import inkex

class MyExtensionName(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument('--patenturl', action='store', type=str, dest='patent_text',
                                     default=None, help='Helper text for this option')

    def effect(self):
        text_type = self.options.patent_text
        text = self._modifyTextNode(text_type)
        # text = text_type

    def _main_function(self, option):
           return text_type
    
    def _modifyTextNode(self, text_type):
        svg = self.document.getroot()
        current_selected = self.svg.selected
        if current_selected:
            for id_, node in current_selected.items():
                if node.tag == inkex.addNS('text', 'svg'):
                    tspan = node.getchildren()[0]
                    text = self._getSampleText(text_type)
                    tspan.text = text

if __name__ == '__main__':
    MyExtension = MyExtensionName()
    MyExtension.run()