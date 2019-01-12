@echo off

SET /P syncop=Please specify sync operation:

SET oparg=--%syncop%

call python sync_operation.py %oparg%

pause