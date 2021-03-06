#!/usr/bin/env python
'''
This script copies the index.rst page from the Sphinx documentation, modifies
it slightly so refs point to the correct place.
'''
import os
import sys
import shutil


class GithubReadmeMaker(object):

    def __init__(self):
        self.root = os.path.abspath(os.path.dirname(__file__))
        os.chdir(self.root)

    def run(self):
        self.copy()
        rst = open('../README.rst').read()
        rst = self.fix_links(rst)
        rst = self.fix_index(rst)
        open('../README.rst', 'w').write(rst)

    def copy(self):
        shutil.copy('index.rst', '../README.rst')

    def fix_links(self, rst):
        prefix = 'https://pycallgraph.readthedocs.org/en/latest'
        rst = rst.replace(
            ':ref:`command-line interface <command_line_usage>`',
            '`command-line interface <{}/guide/command_line_usage.html>`_'
            .format(prefix)
        )
        rst = rst.replace(
            ':ref:`pycallgraph module <pycallgraph>`',
            '`pycallgraph module <{}/api/pycallgraph.html>`_'.format(prefix)
        )
        return rst

    def fix_index(self, rst):
        docidx_offset = rst.find('Documentation Index')
        rst = rst[:docidx_offset]

        rst += open('readme_extras.rst').read()

        return rst


if __name__ == '__main__':
    GithubReadmeMaker().run()
