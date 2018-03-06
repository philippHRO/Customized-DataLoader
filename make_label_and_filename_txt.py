import os
import math
import numpy as np
from sklearn import preprocessing

def write_label_and_filename_txt(filename_txt, label_txt, data_folder, class_1, class_2):
        """Write a text file for filenames and another for one-hot encoded labels
        found in the filenames.
        Currently only works for two classes only! 

        Arguments: 
        filename_txt: path + filename for the filename .txt file.
        label_txt: path + filename for the labels .txt file.
        data_folder: path to the data folder, that contains images to be analyzed.
        class_1 & class_2: strings in filenames to look for, that represent classes that will be encoded.
        """

        # Schreibe one-hot Label Werte in eine txt Datei
        with open(filename_txt, "w") as filelist_file: 
            with open(label_txt, "w") as label_file: 

                for i in os.listdir(data_folder):
                    # Write the file list
                    print(i, end='\n', sep=' ', file=filelist_file) 

                    cl1 = 1 if class_1 in i else 0
                    cl2 = 1 if class_2 in i else 0
                    one_hot = [cl1, cl2]
                    #one_hot_list.append(one_hot)
                    # Write the label list
                    print(one_hot[0], one_hot[1], end='\n', sep=' ', file=label_file)    

if __name__ == "__main__":

    TRAIN_FOLDER = "data/train_img"
    TRAIN_FILENAME_TXT = "data/train_img.txt"
    TRAIN_LABEL_TXT = "data/train_label.txt"

    TEST_FOLDER = "data/test_img/"
    TEST_FILENAME_TXT = "data/test_img.txt"
    TEST_LABEL_TXT = "data/test_label.txt"

    # Classes to look for
    CLASS_1 = "cat"
    CLASS_2 = "dog"

    write_label_and_filename_txt(TRAIN_FILENAME_TXT, TRAIN_LABEL_TXT, TRAIN_FOLDER, CLASS_1, CLASS_2)
    write_label_and_filename_txt(TEST_FILENAME_TXT, TEST_LABEL_TXT, TEST_FOLDER, CLASS_1, CLASS_2)

