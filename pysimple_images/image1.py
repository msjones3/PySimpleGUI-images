import PySimpleGUI as PSG

rows = [
            [PSG.Image("atari.gif")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

button, value = form.Read()
