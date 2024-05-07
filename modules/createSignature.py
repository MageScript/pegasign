from PIL import Image, ImageDraw
import tkinter as tk
from modules.printAndLog import printAndLog
from modules.appData import getAppDataLocalPath


def createSignature(signFilename, window):

    try:
            
        signature_coordinates = []

        def captureCoordinates(event):
            x, y = event.x, event.y
            signature_coordinates.append((x, y))
            canevas.create_oval(x - 1, y - 1, x + 1, y + 1, fill="black", width=2)

        signWindow = tk.Toplevel(window)
        signWindow.title("draw signature")

        iconPath = "media/pegasign.ico"
        signWindow.iconbitmap(iconPath)

        canevas = tk.Canvas(signWindow, bg="white", width=170, height=170)
        canevas.pack()

        canevas.bind("<B1-Motion>", captureCoordinates)

        def finishCapture():
            signWindow.quit()
            signWindow.destroy()

        finishButton = tk.Button(signWindow, text="finish the capture", command=finishCapture)
        finishButton.pack()

        signWindow.mainloop()
        

        dir = getAppDataLocalPath() / "signatures" / "points"
        f = open(str(dir)+ '\\' + signFilename+".sign", 'w')
        for sign in signature_coordinates:   
            f.write(f"{sign[0]} {sign[1]}\n")
        f.close()

        width, height = 170, 170  
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)


        for i in range(1, len(signature_coordinates)):
            x1, y1 = signature_coordinates[i - 1]
            x2, y2 = signature_coordinates[i]
            draw.line([(x1, y1), (x2, y2)], fill="black", width=2)

        dir = getAppDataLocalPath() / "signatures" / "pics"
        image.save(str(dir) + '\\' + signFilename + ".png")

    except Exception as e:
        printAndLog(str(e))    
    