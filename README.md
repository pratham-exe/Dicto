# Dicto

Offline Dictionary

No internet? Switch to this wonderful offline dictionary.

Basic offline dictionary, which gives you the meaning, synonym and antonym of the word with an additional feature of text to speech to verify the word entered with the user. Here .json file (data set) has been used, which contains the meaning of thousands of words.

Natural language toolkit (nltk) is used to find out the synonym and antonym of a particular word. To use the functionality of nltk we should first set up the path and install required dependencies using nltk downloader.

nltk:path specifies the file stored in the NLTK data package at "path". NLTK will search for these files in the directories specified by 'nltk.data.path'

## Prerequisites 

- tkinter (python gui) 
- pyttsx3 (text to speech converter)
- nltk (natural language toolkit)
- Setting up nltk_data, and it's path
- espeak (Linux OS)

## Installation

- First, install all the prerequisites as mentioned above.
    ```
    pip install tkinter
    pip install pyttsx3
    pip install nltk
    ```
- For linux os, install espeak for pyttsx3 functionality.
- Finally setting up the nltk_data, and it's path, follow the below steps for this process.
    1. Create the directory (preferably inside the project folder)
        ```
        mkdir nltk_data
        ```
    2. Download Corpus to the new directory
        ```
        python -m nltk.downloader
        ```
    This'll pop up the nltk downloader. Set your download directory to whatever_absolute_path_to_project/nltk_data/
    3. Let nltk know where to look
        nltk looks for data, resources etc. in the locations specified in the nltk.data.path variable. All you need to do is add
        ```
        nltk.data.path.append('./nltk_data/')
        ```
        to the python file actually using nltk, and it will look for the required dependencies.
