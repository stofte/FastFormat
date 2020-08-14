@echo off
set nv=FastFormat
set nvlc=fastformat
rmdir /q /s %nv%
mkdir %nv%
cargo build --release
copy target\release\%nvlc%.dll %nv%\%nvlc%.dll /y
copy %nv%.py %nv%\%nv%.py /y
copy %nv%.sublime-commands %nv%\%nv%.sublime-commands /y
