#!/usr/bin/python

import pycallgraphNS

# which namespaces to consider libraries
#libraryNamespaces = []
libraryNamespaces = ['__builtin__','__future__','__main__','_winreg','abc','aepack','aetools','aetypes','aifc','al','AL','anydbm','applesingle','array','ast','asynchat','asyncore','atexit','audioop','autoGIL','base64','BaseHTTPServer','Bastion','bdb','binascii','binhex','bisect','bsddb','buildtools','bz2','calendar','Carbon.AE','Carbon.AH','Carbon.App','Carbon.Appearance','Carbon.CarbonEvents','Carbon.CarbonEvt','Carbon.CF','Carbon.CG','Carbon.Cm','Carbon.Components','Carbon.ControlAccessor','Carbon.Controls','Carbon.CoreFounation','Carbon.CoreGraphics','Carbon.Ctl','Carbon.Dialogs','Carbon.Dlg','Carbon.Drag','Carbon.Dragconst','Carbon.Events','Carbon.Evt','Carbon.File','Carbon.Files','Carbon.Fm','Carbon.Folder','Carbon.Folders','Carbon.Fonts','Carbon.Help','Carbon.IBCarbon','Carbon.IBCarbonRuntime','Carbon.Icns','Carbon.Icons','Carbon.Launch','Carbon.LaunchServices','Carbon.List','Carbon.Lists','Carbon.MacHelp','Carbon.MediaDescr','Carbon.Menu','Carbon.Menus','Carbon.Mlte','Carbon.OSA','Carbon.OSAconst','Carbon.Qd','Carbon.Qdoffs','Carbon.QDOffscreen','Carbon.Qt','Carbon.QuickDraw','Carbon.QuickTime','Carbon.Res','Carbon.Resources','Carbon.Scrap','Carbon.Snd','Carbon.Sound','Carbon.TE','Carbon.TextEdit','Carbon.Win','Carbon.Windows','cd','cfmfile','cgi','CGIHTTPServer','cgitb','chunk','cmath','cmd','code','codecs','codeop','collections','ColorPicker','colorsys','commands','compileall','compiler.ast','compiler.visitor','ConfigParser','contextlib','Cookie','cookielib','copy','copy_reg','cPickle','cProfile','crypt','cStringIO','csv','ctypes','curses.ascii','curses.panel','curses.textpad','curses.wrapper','datetime','dbhash','dbm','decimal','DEVICE','difflib','dircache','dis','distutils.archive_util','distutils.bcppcompiler','distutils.ccompiler','distutils.cmd','distutils.command','distutils.command.bdist','distutils.command.bdist_dumb','distutils.command.bdist_msi','distutils.command.bdist_packager','distutils.command.bdist_rpm','distutils.command.bdist_wininst','distutils.command.build','distutils.command.build_clib','distutils.command.build_ext','distutils.command.build_py','distutils.command.build_scripts','distutils.command.clean','distutils.command.config','distutils.command.install','distutils.command.install_data','distutils.command.install_headers','distutils.command.install_lib','distutils.command.install_scripts','distutils.command.register','distutils.command.sdist','distutils.core','distutils.cygwinccompiler','distutils.debug','distutils.dep_util','distutils.dir_util','distutils.dist','distutils.emxccompiler','distutils.errors','distutils.extension','distutils.fancy_getopt','distutils.file_util','distutils.filelist','distutils.log','distutils.msvccompiler','distutils.mwerkscompiler','distutils.spawn','distutils.sysconfig','distutils.text_file','distutils.unixccompiler','distutils.util','distutils.version','dl','doctest','DocXMLRPCServer','dumbdbm','dummy_thread','dummy_threading','EasyDialogs','email.charset','email.encoders','email.errors','email.generator','email.header','email.iterators','email.message','email.mime','email.parser','email.utils','encodings.idna','encodings.utf_8_sig','errno','exceptions','fcntl','filecmp','fileinput','findertools','FL','fl','flp','fm','fnmatch','formatter','fpectl','fpformat','fractions','FrameWork','ftplib','functools','future_builtins','gc','gdbm','gensuitemodule','getopt','getpass','gettext','gl','GL','glob','grp','gzip','hashlib','heapq','hmac','hotshot.stats','htmlentitydefs','htmllib','HTMLParser','httplib','ic','icopen','imageop','imaplib','imgfile','imghdr','imp','imputil','inspect','io','itertools','jpeg','json','keyword','lib2to3','linecache','locale','logging.handlers','macerrors','MacOS','macostools','macpath','macresource','mailbox','mailcap','marshal','math','md5','mhlib','mimetools','mimetypes','MimeWriter','mimify','MiniAEFrame','mmap','modulefinder','msilib','msvcrt','multifile','multiprocessing.connection','multiprocessing.dummy','multiprocessing.managers','multiprocessing.pool','multiprocessing.sharedctypes','mutex','Nav','netrc','new','nis','nntplib','numbers','operator','optparse','os.path','ossaudiodev','parser','pdb','pickle','pickletools','pipes','PixMapWrapper','pkgutil','platform','plistlib','popen2','poplib','posix','posixfile','pprint','pstats','pty','pwd','py_compile','pyclbr','pydoc','Queue','quopri','random','re','readline','repr','resource','rexec','rfc822','rlcompleter','robotparser','runpy','sched','ScrolledText','select','sets','sgmllib','sha','shelve','shlex','shutil','signal','SimpleHTTPServer','SimpleXMLRPCServer','site','smtpd','smtplib','sndhdr','socket','SocketServer','spwd','sqlite3','ssl','stat','statvfs','string','StringIO','stringprep','struct','subprocess','sunau','sunaudiodev','SUNAUDIODEV','symbol','symtable','sys','syslog','tabnanny','tarfile','telnetlib','tempfile','termios','test.test_support','textwrap','thread','threading','time','timeit','Tix','Tkinter','token','tokenize','trace','traceback','tty','turtle','types','unicodedata','unittest','urllib','urllib2','urlparse','user','UserDict','UserList','UserString','uu','uuid','videoreader','warnings','wave','weakref','webbrowser','whichdb','winsound','wsgiref.handlers','wsgiref.headers','wsgiref.simple_server','wsgiref.util','wsgiref.validate','xdrlib','xml.dom','xml.dom.minidom','xml.dom.pulldom','xml.etree.ElementTree','xml.parsers.expat','xml.sax','xml.sax.handler','xml.sax.saxutils','xml.sax.xmlreader','xmlrpclib','zipfile','zipimport','zlib','sre_compile','sre_parse','posixpath']


# minimum total time required for a function call to be exported
minimumTimeExportThreshold = 0

def start_trace():
    pycallgraphNS.start_trace()

def stop_trace():
    pycallgraphNS.stop_trace()
        
def make_TA_graph(filename, stop=True):
    """Creates a TA file compatible with lsedit. It
    will output into a file specified by filename.
    Setting stop to True will stop the current trace.
    """
    if stop:
        stop_trace()

    # create the TA file
    writeFile(filename, get_TA_file_contents(pycallgraphNS.func_count, pycallgraphNS.call_dict))

def get_TA_file_contents(funcCount, callDict):
    """Returns a string containing the contents of a TA file.
    """

    # pycallgraphNS always identifies the start of its trace as "__main__" regardless of the actual function's name.
    # we end up having to add this instance manually since it appears in the stored calls, but not in the stored
    # functions.
    originFunction = "__main__"
    
    # Add the schema and fixed header for the TA file.
    ret = ['// Generated by pycallgraphNS TA export', ]
    ret.append('SCHEME TUPLE :')
    ret.append('')
    ret.append('$INHERIT F   $ENTITY')
    ret.append('$INHERIT N   $ENTITY')
    ret.append('$INHERIT PN  N')
    ret.append('$INHERIT LN  N')
    ret.append('contain N N')
    ret.append('contain N F')

    ret.append('')
    ret.append('SCHEME ATTRIBUTE :')
    ret.append('')
    ret.append('F {')
    ret.append('   class_label = "Function"')
    ret.append('   color       = (255 255 204)')
    ret.append('   labelcolor = (0 0 0)')
    ret.append('   class_icon  = function.png')
    ret.append('   lineno')
    ret.append('}')
    ret.append('($RELATION) {')
    ret.append('   file')
    ret.append('   lineno')
    ret.append('   freq')
    ret.append('}')
    ret.append('(CF) {')
    ret.append('   class_label = "Calls Function"')
    ret.append('   color       = (153 0 0)')
    ret.append('   class_style = 0')
    ret.append('}')
    ret.append('N {')
    ret.append('   class_label = "Namespace"')
    ret.append('   color       = (255 255 153)')
    ret.append('   labelcolor  = (0 0 0)')
    ret.append('   class_icon  = directory.png')
    ret.append('   class_style = 4')
    ret.append('}')
    ret.append('PN {')
    ret.append('   class_label = "Program Namespace"')
    ret.append('   color       = (0 255 0)')
    ret.append('   labelcolor  = (0 0 0)')
    ret.append('   class_icon  = directory.png')
    ret.append('   class_style = 4')
    ret.append('}')
    ret.append('LN {')
    ret.append('   class_label = "Library Namespace"')
    ret.append('   color       = (0 0 255)')
    ret.append('   labelcolor  = (0 0 0)')
    ret.append('   class_icon  = directory.png')
    ret.append('   class_style = 4')
    ret.append('}')

    ret.append('')
    ret.append('FACT TUPLE :')
    ret.append('')
    
    # Add the instances.
    ret.append('$INSTANCE F%s F' % originFunction)
    ret.append('$INSTANCE N%s PN' % pycallgraphNS.originNamespace)
    # need to add this manually, since it is excluded in the Namespaces loop
    ret.append('contain N%s F%s' % (pycallgraphNS.originNamespace, originFunction))

    # Namespaces
    alreadyAddedNamespaces = []
    for func, hits in funcCount.items():
        if (shouldExportFunction(func)):
            namespace = getContainingNamespace(func)
            while (namespace <> "" and not (namespace in alreadyAddedNamespaces)):
                if (isLibraryNamespace(namespace)):
                    ret.append('$INSTANCE N%s LN' % namespace)
                else:
                    ret.append('$INSTANCE N%s PN' % namespace)

                alreadyAddedNamespaces.append(namespace)
                parentNamespace = getContainingNamespace(namespace)
                if (parentNamespace <> "" and parentNamespace != pycallgraphNS.originNamespace):
                    ret.append('contain N%s N%s' % (parentNamespace, namespace))
                namespace = parentNamespace

    # Functions
    for func, hits in funcCount.items():
        if (shouldExportFunction(func)):
            # Split function name to separate the namespace(s) from the function name
            ret.append('$INSTANCE F%s F' % func)
            containingNamespace = getContainingNamespace(func)
            if (containingNamespace <> ""):
                ret.append('contain N%s F%s' % (containingNamespace, func))

    # Add the function calls.
    for fr_key, fr_val in callDict.items():
        if (shouldExportFunction(fr_key)):
            for to_key, to_val in fr_val.items():
                if (shouldExportFunction(to_key)):
                    # export one edge per call
                    for i in range(0,getNumberOfCallsBetween(fr_key, to_key)):
                        ret.append('CF F%s F%s' % (fr_key, to_key))
            
    ret.append('')
    ret.append('FACT ATTRIBUTE :')
    ret.append('')

    # Functions
    ret.append('F%s {label="%s" file="."}' % (originFunction, originFunction))
    for func, hits in funcCount.items():
        if (shouldExportFunction(func)):
            total_time = getTotalTimeForFunction(func)

            ret.append('F%s {label="%s" file="."}' % (func, "%s (%s calls, %f s)" % (getLocalName(func), hits, round(total_time, 6))))
    
    # Namespaces
    for namespace in alreadyAddedNamespaces:
        ret.append('N%s {label="%s"}' % (namespace, "%s (%s s)" % (getLocalName(namespace), round(getTotalTimeForNamespace(namespace, funcCount), 6))))
        
    # Collapse the collection of lines into a single string.
    ret = '\n'.join(ret)

    # For Debugging.
#    print "TA Contents:"
#    print ret 
    
    return ret

def isLibraryNamespace(namespace):
    return (namespace in libraryNamespaces)

def getNumberOfCallsBetween(fromName, toName):
    return pycallgraphNS.func_count_between["%s->%s" % (fromName, toName)]

def getTotalTimeForNamespace(namespaceName, funcCount):
    try:
        return pycallgraphNS.namespace_time[namespaceName]
    except KeyError:
        return 0

def getTotalTimeForFunction(functionName):
    try:
        return pycallgraphNS.func_time[functionName]
    except KeyError:
        return 0
    
def shouldExportFunction(functionName):
    """Returns true if the function should export anything related to the function specified.
       This is used so that blanks and functions used inside pycallgraphNSTAexport don't show
       up in the trace output. It also allows us to optionally filter out functions which
       took up less than some minimum threshold amount of time.
    """
    excludedNamespaces = ['pycallgraphNS', 'pycallgraphTAexport']
    if (functionName == ''):
        return False
    if (getContainingNamespace(functionName) in excludedNamespaces):
        return False
    if (getTotalTimeForFunction(functionName) < minimumTimeExportThreshold):
        return False
    return True

def writeFile(path, contents):
    file = open(path, "w")
    file.write(contents)
    file.close()

def getContainingNamespace(fullyQualifiedName):
    lastPeriod = fullyQualifiedName.rfind('.')
    if (lastPeriod == -1):
        return pycallgraphNS.originNamespace
    return fullyQualifiedName[0:lastPeriod]

def getLocalName(fullyQualifiedName):
    lastPeriod = fullyQualifiedName.rfind('.')
    if (lastPeriod == -1):
        return fullyQualifiedName
    return fullyQualifiedName[(lastPeriod+1):len(fullyQualifiedName)]
    
