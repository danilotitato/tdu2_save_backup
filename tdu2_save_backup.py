from datetime import datetime
import ctypes.wintypes
import os
import shutil

CSIDL_PERSONAL = 5 # Documents Path CSIDL
TDU2_SAVEGAME_PATH = os.path.join('Eden Games', 'Test Drive Unlimited 2', 'savegame')
DATE_FORMAT_STRING = '%Y-%m-%d_%H-%M-%S_'
MAX_BACKUPS_PER_SAVE = 10


def get_save_path():
    documents_path = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, 0, documents_path)

    savegame_full_path = os.path.join(documents_path.value, TDU2_SAVEGAME_PATH)

    if not os.path.isdir(savegame_full_path):
        exit("ERROR: No savegame path found")

    return savegame_full_path


def backup_save(savegame_full_path):
    os.chdir(savegame_full_path)

    savegame_list = [x for x in os.listdir() if os.path.isdir(x)]

    if not savegame_list:
        exit("ERROR: No savegame found")

    current_date = datetime.now().strftime(DATE_FORMAT_STRING)

    for savegame in savegame_list:
        shutil.make_archive(current_date + savegame, 'zip', savegame)

    return len(savegame_list)


def clear_old_backups(savegame_count):
    backup_list = [x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1] == '.zip']

    max_allowed_backups = savegame_count * MAX_BACKUPS_PER_SAVE

    while len(backup_list) > max_allowed_backups:
        os.remove(backup_list.pop(0))


savegame_full_path = get_save_path()
savegame_count = backup_save(savegame_full_path)
clear_old_backups(savegame_count)