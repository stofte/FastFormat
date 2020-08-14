Fast Format for Sublime Text
============================

A project for playing around with Python to Rust interop in the context of
Sublime Text while still doing something useful. In this case formatting JSON files.

Usage:

 - `test.bat` builds and runs the rust library using a python wrapper with some basic tests.
 - `pack.bat` builds the rust library and creates a `FastFormat` directory which can be copied into the ST packages directory (usually `%APPDATA%\Sublime Text 3\Packages`.)

The package adds the `Fast Format` command to the command palette (Ctrl+Shift+P).

Performance
-----------

Tested on a single-line JSON file, formatting was averaged over 5 runs after an initial warm-up. Platforms were Windows 10 and ST 3. 

|                     | 5MB       | 15MB      
|---------------------|-----------|-----------
| [JSON Reindent*](https://github.com/ThomasKliszowski/json_reindent) | 24.2 sec | 72.4 sec
| [JSTool (Notepad++)**](https://github.com/sunjw/jstoolnpp) | 0.87 sec | 2,69 sec
| Fast Format         | 0.95 sec  | 2.88 sec

<sup>*Added timers to the packaged code and numbers obtained this way<br>
**AutoIt script is used to get as accurate numbers as possible.</sup>

TODO
----

 - Support XML?
 - Allow looser JSON parsing (bare keys, etc)?
