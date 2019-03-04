from __future__ import absolute_import, division, print_function
from idascylla import SCYLLA_DIR, PLUGIN_DIR

import idaapi

"""
Based on https://github.com/techbliss/SCyllaDumper but updated/reworked
Mostly read up on how https://github.com/zyantific/IDASkins was made and
wrote this accordingly.

Inlcudes Scylla v0.9.8 (https://github.com/NtQuery/Scylla/releases)
inside plugin/idascylla/Scylla

"""


class IdaScyllaPlugin(idaapi.plugin_t):
    """Entry point"""

    flags = idaapi.PLUGIN_FIX
    comment = "Plugin for using Scylla in IDA 7.0"

    help = "lolno"
    wanted_name = "IDA Scylla: Start"
    wanted_hotkey = "Alt-F7"

    def __init__(self, *args, **kwargs):
        print("[IDA Scylla] v0.0.1 (h@htp.re) loaded")
        idaapi.plugin_t.__init__(self)

    def run(self, arg):
        self.start_scylla()

    def start_scylla(self):
        if __import__('idc').__EA64__: # 64-bit
            path = '"{}"'.format(SCYLLA_DIR + '\\Scylla_x64.exe')
        else: # assumes 32-bit
            path = '"{}"'.format(SCYLLA_DIR + '\\Scylla_x64.exe')
        
        idaapi.IDAPython_ExecSystem(path)

    def init(self):
        return idaapi.PLUGIN_KEEP

    def term(self):
        print("term() called!")
