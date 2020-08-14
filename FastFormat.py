import sublime
import sublime_plugin
import os
import ctypes
import time

def plugin_loaded():
    global jsondll
    dllfilepath = os.path.dirname(os.path.abspath(__file__)) + "/fastformat.dll"
    jsondll = ctypes.cdll.LoadLibrary(dllfilepath);
    jsondll.free.argtypes = ctypes.c_void_p,
    jsondll.free.restype = None
    jsondll.parse_string.argtypes = ctypes.c_void_p,
    jsondll.parse_string.restype = ctypes.c_void_p

class FastFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        start = time.perf_counter()
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        time1 = time.perf_counter()
        ptr = jsondll.parse_string(ctypes.c_wchar_p(contents), len(contents))
        if ptr is None:
            print("FastFormat: could not parse")
            return
        time2 = time.perf_counter()
        tmp = ctypes.cast(ptr, ctypes.c_char_p).value.decode("utf-8")
        time3 = time.perf_counter()
        self.view.erase(edit, sublime.Region(0, self.view.size()))
        self.view.insert(edit, 0, tmp)
        time4 = time.perf_counter()
        jsondll.free(ptr)
        end = time.perf_counter()
        print("FastFormat: elapsed {time:0.4f} secs; extract {extract:0.4f}; rust-parse {rustparse:0.4f}; decode {decode:0.4f}; insert {insert:0.4f}; free {free:0.4f}".format(time=end-start, extract=time1-start, rustparse=time2-time1, decode=time3-time2, insert=time4-time3, free=end-time4))
