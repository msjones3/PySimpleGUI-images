import PySimpleGUI as PSG

myImage = PSG.Image("heads.png")

rows = [
            [myImage],
            [PSG.ReadFormButton("Swap image")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)

while True:
    button, value = form.Read()
    if button == "Swap image":
        myImage.Update("atari.gif")
    else:
        break

