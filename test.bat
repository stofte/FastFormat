@echo off
cargo build --release
copy target\release\fastformat.dll fastformat.dll /Y
python test.py
del /Q fastformat.dll
