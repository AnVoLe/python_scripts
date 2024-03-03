#NoEnv
#SingleInstance force
SendMode Input

; Define a hotkey (Win + Shift + E) to trigger the action
#+e::
    ; Open the item in File Explorer
    Run, explorer "%Clipboard%"

return
