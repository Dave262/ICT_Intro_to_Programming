import customtkinter as ctk
from customtkinter import filedialog
from utils.enums import Colour
from controller.main_controller import TextConvert

class PigLatinGenerator(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        # self.vowels = "aeiouAEIOU"

        self.txt_file = ""

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.geometry("900x480")
        self.title("Pig Latin Generator - By David Ross")



        # Import of functions from controller
        self._controller = TextConvert


        self.grid_rowconfigure(index=(0, 3), weight=0)
        self.grid_rowconfigure(index=(1), weight=1)
        self.grid_columnconfigure(index=(0, 1), weight=1)

        self.header_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
        self.header_frame.grid(row=0, columnspan=2, padx=1, pady=1, sticky="nswe")

        self.left_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
        self.left_frame.grid(row=1, columnspan=1, padx=1, pady=1, sticky="nswe")

        self.right_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
        self.right_frame.grid(
            row=1, column=1, columnspan=1, padx=1, pady=1, sticky="nswe"
        )

        self.title_label = ctk.CTkLabel(master=self.header_frame)
        self.title_label.pack(side="left", padx=5, pady=5)
        self.title_label.configure(
            text="Pig Latin Generator", font=("Inclusive Sans", 40)
        )

        # Text box to enter your normal text
        self.entry_textbox = ctk.CTkTextbox(
            master=self.left_frame, height=300, font=("Inclusive Sans", 20)
        )
        self.entry_textbox.pack(fill="both", pady=10, padx=10)
        self.entry_textbox.insert(index="1.0", text="enter your text here00")

        # Text box for output
        self.output_textbox = ctk.CTkTextbox(
            master=self.right_frame, height=300, font=("Inclusive Sans", 20)
        )
        self.output_textbox.pack(fill="both", pady=10, padx=10)
        self.output_textbox.insert(index="1.0", text="output will be here")

        self.footer_frame = ctk.CTkFrame(self, fg_color=Colour.NORD.value)
        self.footer_frame.grid(row=2, columnspan=2, padx=1, pady=1, sticky="nswe")

        # Convert Button

        self.choose_file_button = ctk.CTkButton(
            master=self.footer_frame,
            text="Choose txt File",
            fg_color=Colour.NORD.value,
            command=lambda: self.process_input(),
        )  # this calls the main controller
        self.choose_file_button.pack(side="left", pady=10, padx=50)
        self.choose_file_button.configure(fg_color=Colour.PINK.value)

        self.convert_button = ctk.CTkButton(
            master=self.footer_frame,
            text="Convert text!",
            fg_color=Colour.NORD.value,
            command= self.populate_output,
        )  # this calls the main controller
        self.convert_button.pack(side="right", pady=10, padx=50)
        self.convert_button.configure(fg_color=Colour.PINK.value)


    def process_input(self):
        self.txt_file = filedialog.askopenfilename(
            initialdir="/Users/davidross/GitHub_Projects/ICT_IntroToProgramming_Exercises/pig_latin_generator/text_files")
        with open(self.txt_file, "r") as text:
            output = text.read()
            
        self.entry_textbox.insert(index="1.0", text=output)
        self.entry_textbox.configure(font=("Inclusive Sans", 12))

    def populate_output(self):
        print(self.txt_file)
        if self.txt_file:
            converter = self._controller(self.txt_file)
            converted_text = converter.pig_string
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", converted_text)
            self.output_textbox.configure(font=("Inclusive Sans", 12))


        

# initiate the GUI
app = PigLatinGenerator()
app.mainloop()
