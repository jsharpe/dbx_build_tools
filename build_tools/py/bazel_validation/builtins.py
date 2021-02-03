from typing import Set, Text

# NOTE(jhance) sourced from https://github.com/jackmaney/python-stdlib-list
# and added some additional modules to the list:
ADDITIONAL_MISSING_MODULES = [
    "concurrent",
    "encodings",
    "posixpath",
    "sre_compile",
    "sre_constants",
    "sre_parse",
]

BUILTIN_MODULES_36 = set(
    ADDITIONAL_MISSING_MODULES
    + [
        "__future__",
        "__main__",
        "_dummy_thread",
        "_thread",
        "abc",
        "aifc",
        "argparse",
        "array",
        "ast",
        "asynchat",
        "asyncio",
        "asyncore",
        "atexit",
        "audioop",
        "base64",
        "bdb",
        "binascii",
        "binhex",
        "bisect",
        "builtins",
        "bz2",
        "cProfile",
        "calendar",
        "cgi",
        "cgitb",
        "chunk",
        "cmath",
        "cmd",
        "code",
        "codecs",
        "codeop",
        "collections",
        "collections.abc",
        "colorsys",
        "compileall",
        "concurrent.futures",
        "configparser",
        "contextlib",
        "contextvars",
        "copy",
        "copyreg",
        "crypt",
        "csv",
        "ctypes",
        "curses",
        "curses.ascii",
        "curses.panel",
        "curses.textpad",
        "dataclasses",
        "datetime",
        "dbm",
        "dbm.dumb",
        "dbm.gnu",
        "dbm.ndbm",
        "decimal",
        "difflib",
        "dis",
        "distutils",
        "distutils.archive_util",
        "distutils.bcppcompiler",
        "distutils.ccompiler",
        "distutils.cmd",
        "distutils.command",
        "distutils.command.bdist",
        "distutils.command.bdist_dumb",
        "distutils.command.bdist_msi",
        "distutils.command.bdist_packager",
        "distutils.command.bdist_rpm",
        "distutils.command.bdist_wininst",
        "distutils.command.build",
        "distutils.command.build_clib",
        "distutils.command.build_ext",
        "distutils.command.build_py",
        "distutils.command.build_scripts",
        "distutils.command.check",
        "distutils.command.clean",
        "distutils.command.config",
        "distutils.command.install",
        "distutils.command.install_data",
        "distutils.command.install_headers",
        "distutils.command.install_lib",
        "distutils.command.install_scripts",
        "distutils.command.register",
        "distutils.command.sdist",
        "distutils.core",
        "distutils.cygwinccompiler",
        "distutils.debug",
        "distutils.dep_util",
        "distutils.dir_util",
        "distutils.dist",
        "distutils.errors",
        "distutils.extension",
        "distutils.fancy_getopt",
        "distutils.file_util",
        "distutils.filelist",
        "distutils.log",
        "distutils.msvccompiler",
        "distutils.spawn",
        "distutils.sysconfig",
        "distutils.text_file",
        "distutils.unixccompiler",
        "distutils.util",
        "distutils.version",
        "doctest",
        "dummy_threading",
        "email",
        "email.charset",
        "email.contentmanager",
        "email.encoders",
        "email.errors",
        "email.generator",
        "email.header",
        "email.headerregistry",
        "email.iterators",
        "email.message",
        "email.mime",
        "email.parser",
        "email.policy",
        "email.utils",
        "encodings.idna",
        "encodings.mbcs",
        "encodings.utf_8_sig",
        "ensurepip",
        "enum",
        "errno",
        "faulthandler",
        "fcntl",
        "filecmp",
        "fileinput",
        "fnmatch",
        "formatter",
        "fractions",
        "ftplib",
        "functools",
        "gc",
        "getopt",
        "getpass",
        "gettext",
        "glob",
        "grp",
        "gzip",
        "hashlib",
        "heapq",
        "hmac",
        "html",
        "html.entities",
        "html.parser",
        "http",
        "http.client",
        "http.cookiejar",
        "http.cookies",
        "http.server",
        "imaplib",
        "imghdr",
        "imp",
        "importlib",
        "importlib.abc",
        "importlib.machinery",
        "importlib.resources",
        "importlib.util",
        "inspect",
        "io",
        "ipaddress",
        "itertools",
        "json",
        "json.tool",
        "keyword",
        "lib2to3",
        "linecache",
        "locale",
        "logging",
        "logging.config",
        "logging.handlers",
        "lzma",
        "macpath",
        "mailbox",
        "mailcap",
        "marshal",
        "math",
        "mimetypes",
        "mmap",
        "modulefinder",
        "msilib",
        "msvcrt",
        "multiprocessing",
        "multiprocessing.connection",
        "multiprocessing.dummy",
        "multiprocessing.managers",
        "multiprocessing.pool",
        "multiprocessing.sharedctypes",
        "netrc",
        "nis",
        "nntplib",
        "ntpath",
        "numbers",
        "operator",
        "optparse",
        "os",
        "os.path",
        "ossaudiodev",
        "parser",
        "pathlib",
        "pdb",
        "pickle",
        "pickletools",
        "pipes",
        "pkgutil",
        "platform",
        "plistlib",
        "poplib",
        "posix",
        "pprint",
        "profile",
        "pstats",
        "pty",
        "pwd",
        "py_compile",
        "pyclbr",
        "pydoc",
        "queue",
        "quopri",
        "random",
        "re",
        "readline",
        "reprlib",
        "resource",
        "rlcompleter",
        "runpy",
        "sched",
        "secrets",
        "select",
        "selectors",
        "shelve",
        "shlex",
        "shutil",
        "signal",
        "site",
        "smtpd",
        "smtplib",
        "sndhdr",
        "socket",
        "socketserver",
        "spwd",
        "sqlite3",
        "ssl",
        "stat",
        "statistics",
        "string",
        "stringprep",
        "struct",
        "subprocess",
        "sunau",
        "symbol",
        "symtable",
        "sys",
        "sysconfig",
        "syslog",
        "tabnanny",
        "tarfile",
        "telnetlib",
        "tempfile",
        "termios",
        "test",
        "test.support",
        "test.support.script_helper",
        "textwrap",
        "threading",
        "time",
        "timeit",
        "tkinter",
        "tkinter.scrolledtext",
        "tkinter.tix",
        "tkinter.ttk",
        "token",
        "tokenize",
        "trace",
        "traceback",
        "tracemalloc",
        "tty",
        "turtle",
        "turtledemo",
        "types",
        "typing",
        "unicodedata",
        "unittest",
        "unittest.mock",
        "urllib",
        "urllib.error",
        "urllib.parse",
        "urllib.request",
        "urllib.response",
        "urllib.robotparser",
        "uu",
        "uuid",
        "venv",
        "warnings",
        "wave",
        "weakref",
        "webbrowser",
        "winreg",
        "winsound",
        "wsgiref",
        "wsgiref.handlers",
        "wsgiref.headers",
        "wsgiref.simple_server",
        "wsgiref.util",
        "wsgiref.validate",
        "xdrlib",
        "xml",
        "xml.dom",
        "xml.dom.minidom",
        "xml.dom.pulldom",
        "xml.etree.ElementTree",
        "xml.parsers.expat",
        "xml.parsers.expat.errors",
        "xml.parsers.expat.model",
        "xml.sax",
        "xml.sax.handler",
        "xml.sax.saxutils",
        "xml.sax.xmlreader",
        "xmlrpc.client",
        "xmlrpc.server",
        "zipapp",
        "zipfile",
        "zipimport",
        "zlib",
    ]
)

BUILTIN_MODULES_27 = set(
    ADDITIONAL_MISSING_MODULES
    + [
        "AL",
        "BaseHTTPServer",
        "Bastion",
        "CGIHTTPServer",
        "Carbon.AE",
        "Carbon.AH",
        "Carbon.App",
        "Carbon.Appearance",
        "Carbon.CF",
        "Carbon.CG",
        "Carbon.CarbonEvents",
        "Carbon.CarbonEvt",
        "Carbon.Cm",
        "Carbon.Components",
        "Carbon.ControlAccessor",
        "Carbon.Controls",
        "Carbon.CoreFounation",
        "Carbon.CoreGraphics",
        "Carbon.Ctl",
        "Carbon.Dialogs",
        "Carbon.Dlg",
        "Carbon.Drag",
        "Carbon.Dragconst",
        "Carbon.Events",
        "Carbon.Evt",
        "Carbon.File",
        "Carbon.Files",
        "Carbon.Fm",
        "Carbon.Folder",
        "Carbon.Folders",
        "Carbon.Fonts",
        "Carbon.Help",
        "Carbon.IBCarbon",
        "Carbon.IBCarbonRuntime",
        "Carbon.Icns",
        "Carbon.Icons",
        "Carbon.Launch",
        "Carbon.LaunchServices",
        "Carbon.List",
        "Carbon.Lists",
        "Carbon.MacHelp",
        "Carbon.MediaDescr",
        "Carbon.Menu",
        "Carbon.Menus",
        "Carbon.Mlte",
        "Carbon.OSA",
        "Carbon.OSAconst",
        "Carbon.QDOffscreen",
        "Carbon.Qd",
        "Carbon.Qdoffs",
        "Carbon.Qt",
        "Carbon.QuickDraw",
        "Carbon.QuickTime",
        "Carbon.Res",
        "Carbon.Resources",
        "Carbon.Scrap",
        "Carbon.Snd",
        "Carbon.Sound",
        "Carbon.TE",
        "Carbon.TextEdit",
        "Carbon.Win",
        "Carbon.Windows",
        "ColorPicker",
        "ConfigParser",
        "Cookie",
        "DEVICE",
        "DocXMLRPCServer",
        "EasyDialogs",
        "FL",
        "FrameWork",
        "GL",
        "HTMLParser",
        "MacOS",
        "MimeWriter",
        "MiniAEFrame",
        "Nav",
        "PixMapWrapper",
        "Queue",
        "SUNAUDIODEV",
        "ScrolledText",
        "SimpleHTTPServer",
        "SimpleXMLRPCServer",
        "SocketServer",
        "StringIO",
        "Tix",
        "Tkinter",
        "UserDict",
        "UserList",
        "UserString",
        "W",
        "__builtin__",
        "__future__",
        "__main__",
        "_winreg",
        "abc",
        "aepack",
        "aetools",
        "aetypes",
        "aifc",
        "al",
        "anydbm",
        "applesingle",
        "argparse",
        "array",
        "ast",
        "asynchat",
        "asyncore",
        "atexit",
        "audioop",
        "autoGIL",
        "base64",
        "bdb",
        "binascii",
        "binhex",
        "bisect",
        "bsddb",
        "buildtools",
        "bz2",
        "cPickle",
        "cProfile",
        "cStringIO",
        "calendar",
        "cd",
        "cfmfile",
        "cgi",
        "cgitb",
        "chunk",
        "cmath",
        "cmd",
        "code",
        "codecs",
        "codeop",
        "collections",
        "colorsys",
        "commands",
        "compileall",
        "compiler",
        "compiler.ast",
        "compiler.visitor",
        "contextlib",
        "cookielib",
        "copy",
        "copy_reg",
        "crypt",
        "csv",
        "ctypes",
        "curses",
        "curses.ascii",
        "curses.panel",
        "curses.textpad",
        "datetime",
        "dbhash",
        "dbm",
        "decimal",
        "difflib",
        "dircache",
        "dis",
        "distutils",
        "distutils.archive_util",
        "distutils.bcppcompiler",
        "distutils.ccompiler",
        "distutils.cmd",
        "distutils.command",
        "distutils.command.bdist",
        "distutils.command.bdist_dumb",
        "distutils.command.bdist_msi",
        "distutils.command.bdist_packager",
        "distutils.command.bdist_rpm",
        "distutils.command.bdist_wininst",
        "distutils.command.build",
        "distutils.command.build_clib",
        "distutils.command.build_ext",
        "distutils.command.build_py",
        "distutils.command.build_scripts",
        "distutils.command.check",
        "distutils.command.clean",
        "distutils.command.config",
        "distutils.command.install",
        "distutils.command.install_data",
        "distutils.command.install_headers",
        "distutils.command.install_lib",
        "distutils.command.install_scripts",
        "distutils.command.register",
        "distutils.command.sdist",
        "distutils.core",
        "distutils.cygwinccompiler",
        "distutils.debug",
        "distutils.dep_util",
        "distutils.dir_util",
        "distutils.dist",
        "distutils.emxccompiler",
        "distutils.errors",
        "distutils.extension",
        "distutils.fancy_getopt",
        "distutils.file_util",
        "distutils.filelist",
        "distutils.log",
        "distutils.msvccompiler",
        "distutils.spawn",
        "distutils.sysconfig",
        "distutils.text_file",
        "distutils.unixccompiler",
        "distutils.util",
        "distutils.version",
        "dl",
        "doctest",
        "dumbdbm",
        "dummy_thread",
        "dummy_threading",
        "email",
        "email.charset",
        "email.encoders",
        "email.errors",
        "email.generator",
        "email.header",
        "email.iterators",
        "email.message",
        "email.mime",
        "email.parser",
        "email.utils",
        "encodings.idna",
        "encodings.utf_8_sig",
        "ensurepip",
        "errno",
        "exceptions",
        "fcntl",
        "filecmp",
        "fileinput",
        "findertools",
        "fl",
        "flp",
        "fm",
        "fnmatch",
        "formatter",
        "fpectl",
        "fpformat",
        "fractions",
        "ftplib",
        "functools",
        "future_builtins",
        "gc",
        "gdbm",
        "gensuitemodule",
        "getopt",
        "getpass",
        "gettext",
        "gl",
        "glob",
        "grp",
        "gzip",
        "hashlib",
        "heapq",
        "hmac",
        "hotshot",
        "hotshot.stats",
        "htmlentitydefs",
        "htmllib",
        "httplib",
        "ic",
        "icopen",
        "imageop",
        "imaplib",
        "imgfile",
        "imghdr",
        "imp",
        "importlib",
        "imputil",
        "inspect",
        "io",
        "itertools",
        "jpeg",
        "json",
        "keyword",
        "lib2to3",
        "linecache",
        "locale",
        "logging",
        "logging.config",
        "logging.handlers",
        "macerrors",
        "macostools",
        "macpath",
        "macresource",
        "mailbox",
        "mailcap",
        "marshal",
        "math",
        "md5",
        "mhlib",
        "mimetools",
        "mimetypes",
        "mimify",
        "mmap",
        "modulefinder",
        "msilib",
        "msvcrt",
        "multifile",
        "multiprocessing",
        "multiprocessing.connection",
        "multiprocessing.dummy",
        "multiprocessing.managers",
        "multiprocessing.pool",
        "multiprocessing.sharedctypes",
        "mutex",
        "netrc",
        "new",
        "nis",
        "nntplib",
        "ntpath",
        "numbers",
        "operator",
        "optparse",
        "os",
        "os.path",
        "ossaudiodev",
        "parser",
        "pdb",
        "pickle",
        "pickletools",
        "pipes",
        "pkgutil",
        "platform",
        "plistlib",
        "popen2",
        "poplib",
        "posix",
        "posixfile",
        "pprint",
        "profile",
        "pstats",
        "pty",
        "pwd",
        "py_compile",
        "pyclbr",
        "pydoc",
        "quopri",
        "random",
        "re",
        "readline",
        "resource",
        "rexec",
        "rfc822",
        "rlcompleter",
        "robotparser",
        "runpy",
        "sched",
        "select",
        "sets",
        "sgmllib",
        "sha",
        "shelve",
        "shlex",
        "shutil",
        "signal",
        "site",
        "smtpd",
        "smtplib",
        "sndhdr",
        "socket",
        "spwd",
        "sqlite3",
        "ssl",
        "stat",
        "statvfs",
        "string",
        "stringprep",
        "struct",
        "subprocess",
        "sunau",
        "sunaudiodev",
        "symbol",
        "symtable",
        "sys",
        "sysconfig",
        "syslog",
        "tabnanny",
        "tarfile",
        "telnetlib",
        "tempfile",
        "termios",
        "test",
        "test.test_support",
        "textwrap",
        "thread",
        "threading",
        "time",
        "timeit",
        "token",
        "tokenize",
        "trace",
        "traceback",
        "ttk",
        "tty",
        "turtle",
        "types",
        "unicodedata",
        "unittest",
        "urllib",
        "urllib2",
        "urlparse",
        "user",
        "uu",
        "uuid",
        "videoreader",
        "warnings",
        "wave",
        "weakref",
        "webbrowser",
        "whichdb",
        "winsound",
        "wsgiref",
        "wsgiref.handlers",
        "wsgiref.headers",
        "wsgiref.simple_server",
        "wsgiref.util",
        "wsgiref.validate",
        "xdrlib",
        "xml",
        "xml.dom",
        "xml.dom.minidom",
        "xml.dom.pulldom",
        "xml.etree.ElementTree",
        "xml.parsers.expat",
        "xml.sax",
        "xml.sax.handler",
        "xml.sax.saxutils",
        "xml.sax.xmlreader",
        "xmlrpclib",
        "zipfile",
        "zipimport",
        "zlib",
    ]
)

BUILTIN_MODULES_ALL = set()
BUILTIN_MODULES_ALL.update(BUILTIN_MODULES_27)
BUILTIN_MODULES_ALL.update(BUILTIN_MODULES_36)


def get_builtins_with_compatibility(py2_compatible, py3_compatible):
    # type: (bool, bool) -> Set[Text]
    assert py2_compatible or py3_compatible
    if py2_compatible and py3_compatible:
        # Note we return all the builtins, not the intersection, on the assumption that code might be
        # doing something like:
        # if six.PY3:
        #    import py3
        # else:
        #    import py2
        return BUILTIN_MODULES_ALL
    elif py2_compatible:
        return BUILTIN_MODULES_27
    else:
        return BUILTIN_MODULES_36
