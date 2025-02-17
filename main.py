from db_data import GetData
from flashcards import *
from menu import MyMenu
from tkinter import messagebox

##### Global Variables #####
language = ""
learning_type = "Manual"
vocab = "All"


# --------------------------------- FUNCTIONS TO GET LANGUAGE SELECTED ----------------------------------------------- #
def dutch_language():
    global language
    language = "Dutch"
    return language

def french_language():
    global language
    language = "French"
    return language

def german_language():
    global language
    language = "German"
    return language

def portuguese_language():
    global language
    language = "Portuguese"
    return language

def spanish_language():
    global language
    language = "Spanish"
    return language


# -------------------------------- FUNCTIONS TO GET LEARNING TYPE SELECTED ------------------------------------------- #
def select_manual():
    global learning_type
    learning_type = "Manual"

def select_auto():
    global  learning_type
    learning_type = "Auto"


# -------------------------------- FUNCTIONS TO GET VOCAB SELECTED --------------------------------------------------- #
def select_all():
    global vocab
    vocab = "All"

def select_remaining():
    global vocab
    vocab = "Remaining"

def select_right():
    global vocab
    vocab = "Right"

def select_wrong():
    global vocab
    vocab = "Wrong"


# -------------------------------- FUNCTIONS TO HIGHLIGHT ANSWER ----------------------------------------------------- #
def highlight_right(window_object: FlashcardWindow, canvas_object: CanvasSetup):
    canvas_object.label_vocab.config(bg="green")  # Change background immediately
    if canvas_object.counter % 2 == 0:
        window_object.window.after(300, lambda: canvas_object.label_vocab.config(bg=canvas_object.colour_dark))  # Reset after 500ms
    else:
        window_object.window.after(300, lambda: canvas_object.label_vocab.config(bg=canvas_object.colour_neutral))  # Reset after 500ms

def highlight_wrong(window_object: FlashcardWindow, canvas_object: CanvasSetup):
    canvas_object.label_vocab.config(bg="red")  # Change background immediately
    if canvas_object.counter % 2 == 0:
        window_object.window.after(300, lambda: canvas_object.label_vocab.config(bg=canvas_object.colour_dark))  # Reset after 500ms
    else:
        window_object.window.after(300, lambda: canvas_object.label_vocab.config(bg=canvas_object.colour_neutral))  # Reset after 500ms



# --------------------------------- START FUNCTION ------------------------------------------------------------------- #
def start_flashcards(lang, learn_type, words):

    if lang == "Dutch":
        light_colour = "#FC8F54"
        dark_colour = "#EB5B00"
        neutral_colour = "#FFF0DC"
        data = GetData(lang)

    elif lang == "French":
        light_colour = "#578FCA"
        dark_colour = "#074799"
        neutral_colour = "#D9EAFD"
        data = GetData(lang)

    elif lang == "German":
        light_colour = "#FF4743"
        dark_colour = "#3A3A3A"
        neutral_colour = "#D1D1D1"
        data = GetData(lang)

    elif lang == "Portuguese":
        light_colour = "#EA4C4C"
        dark_colour = "#365E32"
        neutral_colour = "#CDE3CB"
        data = GetData(lang)

    elif lang == "Spanish":
        light_colour = "#FFC653"
        dark_colour = "#8E1616"
        neutral_colour = "#FFDDD9"
        data = GetData(lang)

    else:
        messagebox.showinfo(title="No language selected", message="Please select a language.")



    if words == "All":
        word_category = "complete"
        data_dict = data.fetch_data(word_category)

    elif words == "Remaining":
        word_category = "remaining"
        data_dict = data.fetch_data(word_category)

    elif words == "Right":
        word_category = "right"
        data_dict = data.fetch_data(word_category)

    else:
        word_category = "wrong"
        data_dict = data.fetch_data(word_category)

    ##### Auto flashcards #####
    def auto_flip_func():
        if flashcard_canvas.counter % 2 == 0:
            flashcard_canvas.non_eng_canvas()

        else:
            flashcard_canvas.eng_canvas()

        flash_window.window.after(ANSWER_TIME, auto_flip_func)

    ##### Manual flashcard function #####
    def flip_card_func():
        if flashcard_canvas.counter % 2 == 0:
            flashcard_canvas.non_eng_canvas()

        else:
            flashcard_canvas.eng_canvas()


    ##### Flashcard window Setup #####
    flash_window = FlashcardWindow(light_colour, auto_flip_func)

    if learn_type == "Manual":
        ##### Canvas setup #####
        flashcard_canvas = CanvasSetup(flash_window.window, data_dict, language,
                                       light_colour, dark_colour, neutral_colour)

        ##### Button setup #####
        flip_button = ButtonSetup(flash_window.window, flip_card_func, light_colour, dark_colour, neutral_colour)
        flip_button.flip_card()

        right_button = ButtonSetup(flash_window.window,
                                   lambda: (data.remove_word(word_category, flashcard_canvas.random_number),
                                            data.add_word("right",
                                                          flashcard_canvas.random_number,
                                                          flashcard_canvas.non_eng_word,
                                                          flashcard_canvas.eng_word),
                                            highlight_right(flash_window, flashcard_canvas)),
                                   light_colour, dark_colour,
                                   neutral_colour)  # Using lambda func to avoid executing immediately

        right_button.right_answer()

        wrong_button = ButtonSetup(flash_window.window,
                                   lambda: (data.remove_word(word_category, flashcard_canvas.random_number),
                                            data.add_word("wrong",
                                                          flashcard_canvas.random_number,
                                                          flashcard_canvas.non_eng_word,
                                                          flashcard_canvas.eng_word),
                                            highlight_wrong(flash_window, flashcard_canvas)),
                                   light_colour, dark_colour, neutral_colour)

        wrong_button.wrong_answer()

        ##### Keep window up #####
        flash_window.window.mainloop()


    else:  # If Automatic flip
        ##### Canvas setup #####
        flashcard_canvas = CanvasSetup(flash_window.window, data_dict, language,
                                       light_colour, dark_colour, neutral_colour)

        ##### Button setup #####
        right_button = ButtonSetup(flash_window.window,
                                   lambda: (data.remove_word(word_category, flashcard_canvas.random_number),
                                            data.add_word("right",
                                                          flashcard_canvas.random_number,
                                                          flashcard_canvas.non_eng_word,
                                                          flashcard_canvas.eng_word),
                                            highlight_right(flash_window, flashcard_canvas)),
                                   light_colour, dark_colour,
                                   neutral_colour)  # Using lambda func to avoid executing immediately

        right_button.right_answer()

        wrong_button = ButtonSetup(flash_window.window,
                                   lambda: (data.remove_word(word_category, flashcard_canvas.random_number),
                                            data.add_word("wrong",
                                                          flashcard_canvas.random_number,
                                                          flashcard_canvas.non_eng_word,
                                                          flashcard_canvas.eng_word),
                                            highlight_wrong(flash_window, flashcard_canvas)),
                                   light_colour, dark_colour, neutral_colour)

        wrong_button.wrong_answer()

        ##### Run timer for window update #####
        flash_window.window.after(ANSWER_TIME, auto_flip_func)
        ##### Keep window up #####
        flash_window.window.mainloop()




# --------------------------------- MAIN WINDOW SETUP ---------------------------------------------------------------- #
starter_image = "images\\menu_heading.png"
main_window = MyMenu(starter_image, lambda: start_flashcards(language, learning_type, vocab))

main_window.create_canvas()
main_window.create_labels()
main_window.create_dropdown(select_dutch=dutch_language,
                            select_french=french_language,
                            select_germ=german_language,
                            select_port=portuguese_language,
                            select_span=spanish_language)
main_window.radio_buttons_learning_type(select_manual, select_auto)
main_window.radio_buttons_vocab_select(select_all, select_remaining, select_wrong, select_right)


main_window.menu_window.mainloop()