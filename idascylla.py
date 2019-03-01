from __future__ import absolute_import, division, print_function

def PLUGIN_ENTRY(*args, **kwargs):
    from idascylla.plugin import IdaScyllaPlugin
    return IdaScyllaPlugin(*args, **kwargs)