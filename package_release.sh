#! /usr/bin/env bash
rm -r dist
rm -r Release

pip install sarc pyqt6 pyinstaller
pyinstaller -F cli.spec
pyinstaller -F gui.spec

mkdir -p Release
cp -r Input Release
cp dist/* Release
