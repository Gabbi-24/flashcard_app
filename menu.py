from tkinter import *

CREAM = "#FCF2FB"
PURPLE = "#A02B93"
LIGHT_PURPLE = "#ECBAE6"
FONT_LABEL = ("Arial", 20, "italic")
FONT_OPTIONS = ("Arial", 16)


class MyMenu:

    def __init__(self, heading_img, start_func):
        self.menu_window = Tk()
        self.heading_img = PhotoImage(file=heading_img)
        self.menu_window.config(bg=CREAM, pady=50, padx=50)
        self.menu_window.title("Language Learning")

        self.selected_learning = StringVar(value="Manually flip the flashcards")
        self.selected_vocab = StringVar(value="Cycle through all 1000 words")

        self.button_start = Button(text="Start Learning", font=FONT_LABEL, bg=PURPLE, fg=CREAM, highlightthickness=0,
                                   command=start_func)
        self.button_start.grid(column=0, row = 11, columnspan=2)

        self.create_canvas()
        self.create_labels()


    def create_canvas(self):
        canvas = Canvas(width=600, height=108, bg=CREAM, highlightthickness=0)
        canvas.create_image(300,54, image=self.heading_img)
        canvas.grid(column=0, row=0, columnspan=2)


    def create_labels(self):
        label_lang_select = Label(text="What language would you like to learn?", font=FONT_LABEL, bg=CREAM, fg="black",
                                  pady=10, padx=10)
        label_lang_select.grid(column=0, row=1, sticky="w")

        label_learn_type = Label(text="How would you like to learn?", font=FONT_LABEL, bg=CREAM, fg="black",
                                 pady=10, padx=10)
        label_learn_type.grid(column=0, row=3, columnspan=2, sticky="w")

        label_select_vocab = Label(text="What vocabulary would you like to learn?", font=FONT_LABEL, bg=CREAM, fg="black",
                                   pady=10, padx=10)
        label_select_vocab.grid(column=0, row=6, columnspan=2, sticky="w")


    def create_dropdown(self, select_dutch, select_french, select_germ, select_port, select_span):
        lang_var = StringVar()
        lang_var.set("Select an Option")

        def change_dropdown_label(lang):
            lang_var.set(lang)



        lang_dropdown = Menubutton(textvariable=lang_var, font=FONT_OPTIONS, bg=LIGHT_PURPLE, fg="black",
                                   relief=RAISED)
        lang_dropdown.grid(column=0, row=2, sticky="w", pady=(0,20))

        menu = Menu(lang_dropdown, tearoff=0)
        lang_dropdown["menu"] = menu    # Create and attach a menu to the dropdown then add to the menu
        menu.add_command(label="Dutch", command=lambda: (select_dutch(),
                                                         change_dropdown_label("Dutch")))
        menu.add_command(label="French", command=lambda: (select_french(),
                                                         change_dropdown_label("French")))
        menu.add_command(label="German", command=lambda: (select_germ(),
                                                          change_dropdown_label("German")))
        menu.add_command(label="Portuguese", command=lambda: (select_port(),
                                                         change_dropdown_label("Portuguese")))
        menu.add_command(label="Spanish", command=lambda: (select_span(),
                                                         change_dropdown_label("Spanish")))


    def radio_buttons_learning_type(self, selection_manual, selection_auto):
        # selected_button = StringVar(value="Manually flip the flashcards")

        radio_1 = Radiobutton(text="Manually flip the flashcards", variable=self.selected_learning,
                              value="Manually flip the flashcards", command=selection_manual,
                              bg=CREAM, fg="black", font=FONT_OPTIONS)
        radio_2 = Radiobutton(text="Automatically flip the flashcards after 3 seconds", variable=self.selected_learning,
                              value="Automatically flip the flashcards after 3 seconds", command=selection_auto,
                              bg=CREAM, fg="black", font=FONT_OPTIONS)

        radio_1.grid(column=0, row=4, columnspan=2, sticky="w")
        radio_2.grid(column=0, row=5, columnspan=2, sticky="w", pady=(0,20))


    def radio_buttons_vocab_select(self, select_all, select_remaining, select_wrong, select_right):
        # selected_button = StringVar(value="Cycle through all 1000 words")

        radio_1 = Radiobutton(text="Cycle through all 1000 words", variable=self.selected_vocab,
                              value="Cycle through all 1000 words", command=select_all,
                              bg=CREAM, fg="black", font=FONT_OPTIONS)

        radio_2 = Radiobutton(text="Cycle through the words you haven't seen yet", variable=self.selected_vocab,
                              value="Cycle through the words you haven't seen yet", command=select_remaining,
                              bg=CREAM, fg="black", font=FONT_OPTIONS)

        radio_3 = Radiobutton(text="Cycle through the words you got wrong", variable=self.selected_vocab,
                              value="Cycle through the words you got wrong", command=select_wrong,
                              bg=CREAM, fg="black", font=FONT_OPTIONS)

        radio_4 = Radiobutton(text="Cycle through the words you got correct", variable=self.selected_vocab,
                              value="Cycle through the words you got correct", command=select_right,
                              bg=CREAM, fg="black", font=FONT_OPTIONS)

        radio_1.grid(column=0, row=7, columnspan=2, sticky="w")
        radio_2.grid(column=0, row=8, columnspan=2, sticky="w")
        radio_3.grid(column=0, row=9, columnspan=2, sticky="w")
        radio_4.grid(column=0, row=10, columnspan=2, sticky="w", pady=(0,40))