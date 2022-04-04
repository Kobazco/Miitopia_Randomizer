if exist dist/ rmdir /S /Q dist
if exist Release/ rmdir /S /Q Release

python -m pip install sarc pyqt6 pyinstaller
pyinstaller -F cli.spec
pyinstaller -F gui.spec

mkdir Release
xcopy /E /I /Y Input Release\Input
xcopy /Y dist\*.exe Release
