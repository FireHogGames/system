import tkinter as tk #for creating visuals

class WinAPI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.prompt = tk.Label(self, text="TestWindow", anchor="w")#prompt
        self.submit = tk.Button(self, text="OK", command="")

        self.prompt.pack(side="top", fill="x")
        self.submit.pack(side="right")


    def InitWindow():
        root = tk.Tk()
        WinAPI(root).pack(fill="both", expand=True)
        root.mainloop()

    def CloseWindow():
        this.close()
