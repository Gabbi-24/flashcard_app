from tkinter import *
import random

ANSWER_TIME = 3000
FONT_LANG = ("Arial", 40, "italic")
FONT_VOCAB = ("Arial", 60, "bold")
FONT_BUTTON = ("Arial", 20)

photo_list=[]

# -------------------------------------- FLASHCARD WINDOW -------------------------------------------------------------#
class FlashcardWindow:

    def __init__(self, colour_light, auto_func):
        self.auto_func = auto_func

        self.window = Toplevel()
        self.window.config(bg=colour_light, padx=50, pady=50)
        self.window.title("Flashcards")

    def timer(self):
        self.window.after(ANSWER_TIME, self.auto_func)



# -------------------------------------- FLASHCARD CANVAS -------------------------------------------------------------#
class CanvasSetup:
    non_eng_word = ""
    eng_word = ""
    counter = 1
    pic_list = []

    def __init__(self, window_ref, data, lang, colour_light, colour_dark, colour_neutral):
        ##### Define inputs #####
        self.window_ref = window_ref
        self.data = data
        self.my_lang = lang
        self.colour_light = colour_light
        self.colour_dark = colour_dark
        self.colour_neutral = colour_neutral

        ##### Get image for canvases #####
        self.eng_pic = PhotoImage(file=f"{self.my_lang}\\card_back.png")
        self.non_eng_pic = PhotoImage(file=f"{self.my_lang}\\card_front.png")

        ##### Get number list for length of data inputted #####
        self.number_list = list(self.data["eng"].keys())  # Updated to use lowercase "eng"

        ##### Create canvas #####
        self.canvas = Canvas(self.window_ref, width=800, height=500, highlightthickness=0, bg=self.colour_light)
        self.canvas.grid(column=0, row=0, columnspan=3)
        self.canvas_img = self.canvas.create_image(415, 265, image=self.non_eng_pic)

        ##### Initialise the random_word() method #####
        self.random_word(self.data)  # Randomly select the initial word to start with

        ##### Create labels #####
        self.label_lang = Label(self.window_ref, text=self.my_lang, font=FONT_LANG, bg=self.colour_neutral)
        self.label_vocab = Label(self.window_ref, text=CanvasSetup.non_eng_word, font=FONT_VOCAB, bg=self.colour_neutral, fg="black")
        self.label_lang.grid(column=1, row=0)
        self.label_vocab.grid(column=1, row=1, sticky="N")
        self.canvas.grid(column=0, row=0, columnspan=3, rowspan=2)

    def non_eng_canvas(self):
        self.random_word(self.data)  # Select a new random word
        self.canvas.itemconfig(self.canvas_img, image=self.non_eng_pic)
        self.label_lang.config(text=self.my_lang, bg=self.colour_neutral, fg="black")
        self.label_vocab.config(text=CanvasSetup.non_eng_word, bg=self.colour_neutral, fg="black")
        CanvasSetup.counter += 1

    def eng_canvas(self):
        self.canvas.itemconfig(self.canvas_img, image=self.eng_pic)
        self.label_lang.config(text="English", bg=self.colour_dark, fg=self.colour_neutral)
        self.label_vocab.config(text=CanvasSetup.eng_word, bg=self.colour_dark, fg=self.colour_neutral)
        CanvasSetup.counter += 1

    def random_word(self, data):
        ### Select a random word and update class variables ###
        self.random_number = random.choice(self.number_list)  # Pick a random key
        CanvasSetup.eng_word = data["eng"].get(str(self.random_number), "N/A")  # Use lowercase "eng"
        CanvasSetup.non_eng_word = data["non_eng"].get(str(self.random_number), "N/A")  # Use lowercase "non_eng"



# -------------------------------------- FLASHCARD BUTTONS ------------------------------------------------------------#
class ButtonSetup:

    def __init__(self, window_ref, function, colour_light, colour_dark, colour_neutral):
        self.window_ref = window_ref
        self.function = function
        self.colour_light = colour_light
        self.colour_dark = colour_dark
        self.colour_neutral = colour_neutral

        self.right_pic = PhotoImage(file="images\\right.png")
        self.wrong_pic = PhotoImage(file="images\\wrong.png")
        self.button = Button(self.window_ref, bg=self.colour_light, highlightthickness=0)


    def flip_card(self):
        self.button.config(text="Flip Card", bg=self.colour_dark, fg=self.colour_neutral, font=FONT_BUTTON,
                           highlightthickness=0, command=self.function)
        self.button.grid(column=1, row=2)


    def right_answer(self):
        self.button.config(image=self.right_pic, bg=self.colour_light,
                           highlightthickness=0, command=self.function)
        self.button.grid(column=2, row=2)

    def wrong_answer(self):
        self.button.config(image=self.wrong_pic, bg=self.colour_light,
                           highlightthickness=0, command=self.function)
        self.button.grid(column=0, row=2)