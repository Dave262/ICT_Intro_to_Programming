import customtkinter as ctk
from utils.enums import Colour
from controller.main_controller import TextConvert


class PigLatinGenerator(ctk.CTk):
  def __init__(self) -> None:
    super().__init__()
    self.vowels = "aeiouAEIOU"
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    self.geometry("900x480")
    self.title("Pig Latin Generator - By David Ross")
    
    
    
    
# Import of functions from controller
    self._controller = TextConvert()
    sentence: str = self._controller.get_text
        
    
    
    
    
    
    self.grid_rowconfigure(index=(0,3), weight=0) 
    self.grid_rowconfigure(index=(1), weight=1)  
    self.grid_columnconfigure(index=(0,1), weight=1)  


    self.header_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
    self.header_frame.grid(row=0, columnspan=2, padx=1, pady=1, sticky="nswe")
    
    self.left_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
    self.left_frame.grid(row=1, columnspan=1, padx=1, pady=1, sticky="nswe")
    
    self.right_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
    self.right_frame.grid(row=1, column=1, columnspan=1, padx=1, pady=1, sticky="nswe")


    self.title_label = ctk.CTkLabel(master=self.header_frame)
    self.title_label.pack(side='left', padx=5, pady=5)
    self.title_label.configure(text="Pig Latin Generator",font=("Inclusive Sans", 40))


# Text box to enter your normal text 
    self.entry_textbox = ctk.CTkTextbox(master= self.left_frame, height=300, font=("Inclusive Sans", 20))
    self.entry_textbox.pack(fill="both", pady=10, padx=10)
    self.entry_textbox.insert(index="1.0", text="enter your text here00")
    
# Text box for output  
    self.output_textbox = ctk.CTkTextbox(master= self.right_frame, height=300, font=("Inclusive Sans", 20))
    self.output_textbox.pack(fill="both", pady=10, padx=10)
    self.output_textbox.insert(index="1.0", text="output will be here")
    
    
    self.footer_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
    self.footer_frame.grid(row=2, columnspan=2, padx=1, pady=1, sticky="nswe")
    
# Convert Button    
    self.convert_button = ctk.CTkButton(master=self.footer_frame, text="Convert text!", fg_color=Colour.NORD.value, command=lambda: self._controller.convert_sentence(sentence)) # this calls the main controller
    self.convert_button.pack(pady=10)
    self.convert_button.configure(fg_color=Colour.PINK.value)
    
    
    self.show_text_button = ctk.CTkButton(master=self.footer_frame, text="Show text", fg_color=Colour.NORD.value, command=lambda: self._controller.get_text(self.entry_textbox)) # this calls the main controller IMPORTANT to use lambda so it doesn't call once on load and then not work again
    self.show_text_button.pack(pady=10)
    self.show_text_button.configure(fg_color=Colour.PINK.value)
    


  def populate_output(self):
    text = self._controller.convert_sentence()
    print(text)
    self.output_textbox.delete("1.0", "end")
    self.output_textbox.insert(index="1.0", text=f"{text}")
    
    
    
    
    


# initiate the GUI    
app = PigLatinGenerator()
app.mainloop()   
    
    