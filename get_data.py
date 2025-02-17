import pandas as pd
import json

class GetData:

    def __init__(self, csv, data_complete_lang, data_remaining_lang, data_right_lang, data_wrong_lang):
        self.csv = csv
        self.complete_file = data_complete_lang
        self.remaining_file = data_remaining_lang
        self.right_file = data_right_lang
        self.wrong_file = data_wrong_lang

        # Get complete data #
        self.data_raw = pd.read_csv(self.csv)
        data_dict_temp = self.data_raw.to_dict()  # Don't use the .json because it gives you a json str

        with open(self.complete_file, "w") as data_file:  # Write dict into a json file
                json.dump(data_dict_temp, data_file, indent=4)

        with open(self.complete_file, "r") as data_file:
                self.data_complete = json.load(data_file)  # Read the file as data_dict


        # Get data that remain #
        try:
            with open(self.remaining_file, "r") as data_file:
                self.data_remaining = json.load(data_file)

        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.remaining_file, "w") as data_file:
                json.dump(self.data_complete, data_file, indent=4)

            with open(self.remaining_file, "r") as data_file:
                self.data_remaining = json.load(data_file)

            # self.data_remaining.shutil.copy(self.complete_file,
            #                                 self.remaining_file)  # Copy the complete data to get data remaining that we can edit


        # Get data that were correct #
        try:
            with open(self.right_file, "r") as data_file:
                self.data_right = json.load(data_file)

        except (FileNotFoundError, json.JSONDecodeError):
                self.data_right = {"NL": {}, "ENG": {}}

        # Get data that were incorrect #
        try:
            with open(self.wrong_file, "r") as data_file:
                self.data_wrong = json.load(data_file)

        except (FileNotFoundError, json.JSONDecodeError):
                self.data_wrong = {"NL": {}, "ENG": {}}


    def remove_word(self, word_number):
        word_number_str = str(word_number)

        if word_number_str in self.data_remaining["NL"] and word_number_str in self.data_remaining["ENG"]:
            del self.data_remaining["NL"][word_number_str]
            del self.data_remaining["ENG"][word_number_str]

            with open(self.remaining_file, "w") as data_file:
                json.dump(self.data_remaining, data_file, indent=4)

        elif word_number_str in self.data_right["NL"] and word_number_str in self.data_right["ENG"]:
            del self.data_right["NL"][word_number_str]
            del self.data_right["ENG"][word_number_str]

            with open(self.right_file, "w") as data_file:
                json.dump(self.data_right, data_file, indent=4)

        elif word_number_str in self.data_wrong["NL"] and word_number_str in self.data_wrong["ENG"]:
            del self.data_wrong["NL"][word_number_str]
            del self.data_wrong["ENG"][word_number_str]

            with open(self.wrong_file, "w") as data_file:
                json.dump(self.data_wrong, data_file, indent=4)

        else:
            print(f"Key {word_number_str} not found in data.")


    def add_word_right(self, word_number, dutch_word, eng_word):
        word_number_str = str(word_number)

        self.data_right["NL"][word_number_str] = dutch_word
        self.data_right["ENG"][word_number_str] = eng_word

        with open(self.right_file, "w") as data_file:
            json.dump(self.data_right, data_file, indent=4)




    def add_word_wrong(self, word_number, dutch_word, eng_word):
        word_number_str = str(word_number)

        self.data_wrong["NL"][word_number_str] = dutch_word
        self.data_wrong["ENG"][word_number_str] = eng_word

        with open(self.wrong_file, "w") as data_file:
            json.dump(self.data_wrong, data_file, indent=4)