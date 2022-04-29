#! /usr/bin/env bash
rm -r dist
rm -r Release

pip install sarc pyqt6 pyinstaller
pyinstaller cli.spec
pyinstaller gui.spec

mkdir -p Release
cp -r Input Release
cp dist/* Release
