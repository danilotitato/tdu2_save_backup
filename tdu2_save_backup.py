from datetime import datetime
import ctypes.wintypes
import os
import shutil

CSIDL_PERSONAL = 5 # Documents Path CSIDL
TDU2_SAVEGAME_PATH = os.path.join('Eden Games', 'Test Drive Unlimited 2', 'savegame')
DATE_FORMAT_STRING = '%Y-%m-%d_%H-%M-%S_'

# get save path
documents_path = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, 0, documents_path)

savegame_full_path = os.path.join(documents_path.value, TDU2_SAVEGAME_PATH)

if not os.path.isdir(savegame_full_path):
    exit("ERROR: No savegame path found")

# compress each savegame
os.chdir(savegame_full_path)

savegame_list = [x for x in os.listdir() if os.path.isdir(x)]

if not savegame_list:
    exit("ERROR: No savegame found")

current_date = datetime.now().strftime(DATE_FORMAT_STRING)

for savegame in savegame_list:
    shutil.make_archive(current_date + savegame, 'zip', savegame)
