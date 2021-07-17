import ctypes.wintypes
import os

CSIDL_PERSONAL = 5 # Documents Path CSIDL
TDU2_SAVEGAME_PATH = os.path.join('Eden Games', 'Test Drive Unlimited 2', 'savegame')

# get save path
documents_path = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, 0, documents_path)

savegame_full_path = os.path.join(documents_path.value, TDU2_SAVEGAME_PATH)

if not os.path.isdir(savegame_full_path):
    exit("ERROR: No savegame path found")