# -*- mode: python -*-

block_cipher = None


a = Analysis(['Promfi2.py'],
             pathex=['F:\\00085-PROGRAMMING & CODING PROJECTS\\Python Programming\\190422_python tutorial - programming with Mosh\\PROMFI 2 - Copy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Promfi2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
