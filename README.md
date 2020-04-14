example log:
	
["codex.txt R", "data.lib R W X", "exterminatus.exe X"]
["eretic R", "inquisition X R W", "guard R W"]
guard       read     codex.txt
inquisition read     data.lib
inquisition write    data.lib
guard       read     codex.txt
eretic      read     codex.txt
inquisition execute  exterminatus.exe
eretic      write    data.lib
inquisition read     codex.txt
eretic      execute  exterminatus.exe
inquisition write    codex.txt
