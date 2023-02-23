
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.font import BOLD
import pytube
import util.generic as utl


class MasterPanel:
    def show_link(self):
        link=self.usuario.get()
        youtube = pytube.YouTube(link)
        indice = self.listbox.curselection()
        if indice:
            op=self.listbox.get(indice)
        if op == "AUDIO":
            audio = youtube.streams.get_by_itag("140").download('Audios')
            messagebox.showinfo(message="Audio Descargado",title="Mensaje")
            self.usuario.delete(0, tk.END)
        elif op == "VIDEO 360p":
            video = youtube.streams.get_by_itag("18").download('Videos')
            messagebox.showinfo(message="Video Descargado",title="Mensaje")
            self.usuario.delete(0, tk.END)
        elif op == "VIDEO 720p":
            video = youtube.streams.get_by_itag("22").download('Videos')
            messagebox.showinfo(message="Video Descargado",title="Mensaje")
            self.usuario.delete(0, tk.END)
        elif op == "VIDEO 1080p":
            video = youtube.streams.get_by_itag("137").download('Videos')
            messagebox.showinfo(message="Video Descargado",title="Mensaje")
            self.usuario.delete(0, tk.END)
            
        print(link)
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Convertidor')
        self.ventana.geometry('500x300')
        self.ventana.config(bg='#f2f2f2')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,700,500)
        
        logo =utl.leer_imagen("GUI Login/imagenes/white-youtube.png", (200, 200))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#808080')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='#808080')
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#f2f2f2')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 0, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="CONVERTIDOR",font=('Times', 30), fg="#666a88",bg='#f2f2f2',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 0,  bd=0, relief=tk.SOLID,bg='#f2f2f2')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Link", font=('Times', 14) ,fg="#666a88",bg='#f2f2f2', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)

        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=40,pady=10)

        self.listbox=tk.Listbox(frame_form_fill, font=('Times') ,fg="#666a88",bg='#f2f2f2')
        self.listbox.insert(tk.END,"AUDIO")
        self.listbox.insert(tk.END,"VIDEO 360p")
        self.listbox.insert(tk.END,"VIDEO 720p")
        self.listbox.insert(tk.END,"VIDEO 1080p")

        self.listbox.pack(fill=tk.X, padx=100,pady=0,expand=tk.YES)
        
        inicio = tk.Button(frame_form_fill,text="Convertir",font=('Times', 15,BOLD),bg='#808080', bd=0,fg="#fff", command=self.show_link)
        inicio.pack(fill=tk.X, padx=40,pady=20)   
        inicio.bind("<Return>",(lambda event: self.show_link()))
        self.ventana.bind("<Return>",(lambda event: self.show_link()))
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, tk.PhotoImage(file='GUI Login/imagenes/logoyutu.png'))

        self.ventana.mainloop()