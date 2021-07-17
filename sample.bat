:: NOTE: change <SCRIPT PATH> and <TDU2 INSTALL PATH> before running this
@echo off
python "<SCRIPT PATH>\tdu2_save_backup.py"
cd "<TDU2 INSTALL PATH>"
start TDU2_Universal_Launcher.exe
exit