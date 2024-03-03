#NoEnv
#SingleInstance force
SendMode Input

; Define a hotkey (Win + Shift + E) to trigger the action
#+e::
    ; Save the current clipboard contents
    ClipboardOld := ClipboardAll

    ; Open clipboard history by simulating keystrokes
    Send ^+{v}

    ; Wait for the clipboard history to open
    Sleep 500

    ; Send keys to select and copy the last item
    Send ^{vk56}

    ; Wait for the selection to be copied
    Sleep 100

    ; Retrieve the clipboard contents
    Clipboard := Clipboard

    ; Close clipboard history
    Send {Esc}

    ; If clipboard is empty, show error message
    if (Clipboard = "")
    {
        MsgBox, No data found in the clipboard history.
        return
    }

    ; Open the item in File Explorer
    Run, explorer "%Clipboard%"

    ; Restore the original clipboard contents
    Clipboard := ClipboardOld
return
