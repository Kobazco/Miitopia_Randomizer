if exist dist/ rmdir /S /Q dist
if exist Release/ rmdir /S /Q Release

python -m pip install sarc pyqt6 pyinstaller
pyinstaller cli.spec
pyinstaller gui.spec

mkdir Release
xcopy /E /I /Y Input Release\Input
xcopy /Y dist\*.exe Release
