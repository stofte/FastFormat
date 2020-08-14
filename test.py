import os
import ctypes

filepath = os.path.dirname(os.path.abspath(__file__)) + "/fastformat.dll"
formatter = ctypes.cdll.LoadLibrary(filepath);
formatter.free.argtypes = ctypes.c_void_p,
formatter.free.restype = None
formatter.parse_string.argtypes = ctypes.c_void_p,
formatter.parse_string.restype = ctypes.c_void_p

def teststr(contents):
    print("Parsing: {str}".format(str=contents))
    fooob = ctypes.c_wchar_p(contents);
    ptr = formatter.parse_string(fooob, len(contents))
    if not ptr is None:
        tmp = ctypes.cast(ptr, ctypes.c_char_p).value.decode("utf-8")
        print("Success: {str}".format(str=tmp));
        formatter.free(ptr);
    else:
        print("Failed to parse")

teststr("{illegal: 42}")
teststr("<xml/>")
teststr("\"string")
teststr("")
teststr("true")
teststr("null")
teststr("[]")
teststr("\"string\"")

teststr("{\"HÆJMØR\": 42,\"䠢紊\": {\"array\": [1,\"2\"]}}")
