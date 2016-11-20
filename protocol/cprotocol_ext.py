from distutils.core import Extension
import os.path


def get_extension():
    cparser = system.get_extension_by_path('parser/cparser_ext.py')

    define_macros = []
    if system.args.enable_reaper:
        define_macros.append(('REAPER_ENABLED', 1))

    return Extension(
        'protocol.cprotocol',
        sources=['cprotocol.c', '../capsule.c', *cparser.sources],
        include_dirs=['.', '..', '../parser', '../router', '../request',
                      '../response', *cparser.include_dirs],
        libraries=cparser.libraries, library_dirs=cparser.library_dirs,
        extra_link_args=cparser.extra_link_args,
        define_macros=define_macros)
