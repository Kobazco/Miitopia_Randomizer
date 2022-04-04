# -*- mode: python ; coding: utf-8 -*-
from site import getsitepackages, getusersitepackages
from os.path import join, exists


block_cipher = None


global_site_packages_path = getsitepackages()[-1]
user_site_packages_path = getusersitepackages()

sarc_path = join(global_site_packages_path, 'sarc', 'aglenv_file_info.json')
if not exists(sarc_path):
    sarc_path = join(user_site_packages_path, 'sarc', 'aglenv_file_info.json')
rstb_path = join(global_site_packages_path, 'rstb', 'resource_factory_info.tsv')
if not exists(rstb_path):
    rstb_path = join(user_site_packages_path, 'rstb', 'resource_factory_info.tsv')

a = Analysis(['cli.py'],
             pathex=[],
             binaries=[],
             datas=[
                 (sarc_path, 'sarc'),
                 (rstb_path, 'rstb')
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += Tree('./Data', prefix='Data')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='MiitopiaRandomizer_cli',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
