# Convert in Terminal

I got tired of opening a browser everytime I had to convert something, usually for converting energy electronvolt, kcal/mol and hartree. So I create a small script.

## Installation

Copy-pastable install

    git clone https://github.com/charnley/convert-in-terminal.git
    cd convert-in-terminal
    pip install -r requirements.txt
    ln -rs ./convert.py ~/bin/c
    chmod +x ~/bin/c

My setup is a I have a symbolic link in my `~/bin/` folder for easy usage

    ln -rs <path to git folder>/convert.py ~/bin/c
    chmod +x ~/bin/c

## Usage

Then I call it like, currently supporting

currency

    $ c 15 usd in dkk
    15 USD = 105.1980 DKK

energy

    $ c 50 ev in kcal
    1153.04611723 kcal

more to come

