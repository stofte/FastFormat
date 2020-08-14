Fast Format for Sublime Text
============================

A project for playing around with Python to Rust interop in the context of
Sublime Text. `Fast Format` a simple package for formatting JSON which uses
a rust to do the heavy lifting.

Tested on Windows 10 using Sublime Text 3.

Usage:

 - `test.bat` builds and runs the rust library using a python wrapper with some basic tests.
 - `pack.bat` builds the rust library and creates a `FastFormat` directory which can be copied into the ST packages directory (usually `%APPDATA%\Sublime Text 3\Packages`.)

The package adds the `Fast Format` command to the command palette (Ctrl+Shift+P).

TODOs
-----

 - Create ome measurements to compare
 - Support XML?
 - Allow looser JSON parsing (bare keys, etc)?
