import tkinter as tk

class Program :
    def on_ok( self ) :
        print('ok button pressed')
        
    def on_cancel( self ) :
        print('cancel button pressed')
        self.__button_ok.pack()
    
    def __init__( self ) :
        window = tk.Tk()
        button_ok = tk.Button(window, text='ok', command=self.on_ok )
        button_cancel = tk.Button(window, text='cancel', command=self.on_cancel )
        
        button_ok.pack()
        button_cancel.pack()
        
        self.__button_ok = button_ok
        self.__button_cancel = button_cancel
        self.__window = window
    
    def run( self ) :
        self.__window.mainloop()
        
program = Program()
program.run()