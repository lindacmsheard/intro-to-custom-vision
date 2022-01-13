#!/bin/bash

## Data citation: 2018 – Özgenel, Ç.F., Gönenç Sorguç, A. “Performance Comparison of Pretrained Convolutional Neural Networks on Crack Detection in Buildings”, ISARC 2018, Berlin.


# TODO: implement with ADF to avoid fetching to local machine - can adf deal with rar files?


# get Concrete Crack Images for Classification
mkdir -p Ozgenel2019                           # this will be gitignored
cd Ozgenel2019
wget https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/5y9wdsg2zt-2.zip


unzip *.zip

sudo apt update && sudo apt install --assume-yes unrar #Ubuntu and Debian

unrar x *.rar temp


