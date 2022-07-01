# SoftUni Python Conference Web Scraping Demos

## About

The code in this repo is from the [SoftUni](https://softuni.bg) conference **Dive int(0) Python**.

You can find more about it [here](https://softuni.bg/trainings/3866/dive-into-python)

## Installation

    $ pip install -r requirements.txt
    
## Running Scrapy Spiders

There are 3 spiders in the **spiders** folder

    $ scrapy crawl names
    
    $ scrapy crawl trainers
    
    $ scrapy crawl courses
    
To save the data from any of the spiders add **-O file_name.json** after the command.
Other file types can be used as well.
Example:

    $ scrapy crawl courses -O courses.json
    
## Running Beautiful Soup Scraper

    $ python trainers_bs4.py
