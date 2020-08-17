import PySimpleGUI as PSG

message = PSG.Text("Click on image to change text")


rows = [
            [message],
            [PSG.ReadFormButton("Atari",image_filename="atari.gif")]
       ]

form = PSG.FlexForm("This is a form.")
form.Layout(rows)
while True:
    button, value = form.Read()
    if button == "Atari":
        message.Update("Clicked on Atari")
    else:
        break
