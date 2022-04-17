# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['BJ_pg.py'],
             pathex=['C:\\Users\\iberb\\PycharmProjects\\BlackJack\\BlackJack'],
             binaries=[],
             datas=[('back.png', '.'),('Hearts.png', '.'),('Diamonds.png', '.'),('Spades.png', '.'),('Clubs.png', '.')],
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
          name='BJ_pg',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
