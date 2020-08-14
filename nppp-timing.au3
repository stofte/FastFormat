#include <MsgBoxConstants.au3>

WinActivate ("[CLASS:Notepad++]")
Local $hTimer = TimerInit()
Send("^!m")
While 1
   Local $txt = StatusbarGetText("[CLASS:Notepad++]","", 2)
   Local $done = StringInStr($txt, "564.618")
   If $done > 0 Then
	  Local $fDiff = TimerDiff($hTimer)
	  MsgBox($MB_SYSTEMMODAL, "", "Elapsed: " & $fDiff)
	  ExitLoop
   EndIf
   Sleep(100)
WEnd
