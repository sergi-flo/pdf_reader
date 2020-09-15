# App to read pdfs and export information

## Requeriments

- Before installing the requeriments.txt file, you should have installed poppler and pkg-config in your computer. To do so in a MACOSX computer just verify if you have brew with the command:
```
which brew
```
If brew is not installed nothing should appear, otherwise a path to the bre intallation folder should appear. If it is not installed, please isnstall it following the official [Brew](https://brew.sh) web. Once you have brew installed you should run the 2 following commands to install poppler and pkg-conifg:
```
brew install poppler
brew install pkg-config
```

- Install the requeriments.txt using the following command:

```
pip install -r requirements.txt
```

## How to run the app

Paste the pdf file you want to visualize in folder pdfs and change the file_path variable in the open_pdf.py file. After that just execute the following command in terminal or run it with the pyhton interpreter:

```
python3 open_pdf.py
```

## Explanation

App that allows you to read pdfs with python and extract all the information from ECI tickets.