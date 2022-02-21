# Lab: Data Analysis with Pandas

## Overview

Today we're taking a tour into Data Science to learn a bit more about the field and tools used in this space!

The best way to hone your data analysis skills is consistent, deliberate practice.

One of the best places to acquire data for analysis is [Kaggle](https://www.kaggle.com/), so practice your abilities with some [Kaggle](https://www.kaggle.com/datasets) data sets.

Sign up for a Kaggle account (if you don't already have one).

## Feature Tasks and Requirements

- Find and download the following data set:
  - [Video Game Sales](https://www.kaggle.com/gregorut/videogamesales){:target="_blank"} - Sales data from more than 16,500 games

- Create new Notebook called `vg-stats`.
- Add a markdown cell at the top of notebook with the title of this assignment, an appropriate name for the data set, as well as your name and the date.

- In the `vg-stats` notebook answer the following questions/do the following tasks. Note that the numbers quoted for sales are in the millions, and apply only for those games with over 10,000 sales.:
    1. Which company is the most common video game publisher?
    1. What’s the most common platform?
    1. What about the most common genre?
    1. What are the top 20 highest grossing games?
    1. For North American video game sales, what’s the median?
       - Provide a secondary output showing ten games surrounding the median sales output.
       - Assume that games with same median value are sorted in descending order.
    1. For the top-selling game of all time, how many standard deviations above/below the mean are its sales for North America?
    1. The Nintendo Wii seems to have outdone itself with games. How does its average number of sales compare with all of the other platforms?
    1. Come up with 3 more questions that can be answered with this data set.

- When you're done answering all of the questions for each data set, clean up your notebooks leaving only cells that contain relevant data and calculations. Then restart and run your notebook so that the cell numbering is sequential from top to bottom.

- **Have fun with the data!! Play around a bit, and see if there's anything else you can/want to do with the info available!**

### Publish with Kaggle

- Create an account (if you haven't already) at [Kaggle](https://www.kaggle.com/){:target="_blank"}.
- Create a new Notebook.
  - Easiest way is by choosing `New Notebook` option from [Video Game Sales](https://www.kaggle.com/gregorut/videogamesales){:target="_blank"} page.
  - Alternately, create a new project by clicking `+ Create` button.
  - Use `File: Add or Updload Data` in menu to store data sets using the links above in `Feature Tasks and Requirements` section.
- Name project `Video Game Stats`.
- Click `Share` button and select `Public` access.
- Submit the Public URLs for Noteboks.

### User Acceptance Tests

Below are example tests. You'll need one test minimum for each requirement listed above.

```python
def test():

    def assert_equal(actual,expected):
        assert actual == expected, f"Expected {expected} but got {actual}"

    assert_equal(most_common_publisher, None)
    assert_equal(most_common_platform, None)
    assert_equal(most_common_genre, None)
    assert_equal(top_twenty_highest_grossing_games.iloc[0].Name, None)
    assert_equal(top_twenty_highest_grossing_games.iloc[19].Name, None)
    assert_equal(na_median_sales, None)
    assert_equal(ten_median_na_seller_names, None)

    print("Success!!!")

test()
```

## Stretch

- [Cycle Share Data set](https://www.kaggle.com/pronto/cycle-share-dataset){:target="_blank"} - Bicycle Trip Data from Seattle's Cycle Share System
- In the `bike-stats` notebook, answer the following questions/do the following tasks:
    1. What is the average trip duration for a borrowed bicycle?
    1. What's the most common age of a bicycle-sharer?
    1. Given all the weather data here, find the average precipitation per month, and the median precipitation.
    1. What’s the average number of bikes at a given bike station?
    1. When a bike station is modified, is it more likely that it’ll lose bikes or gain bikes? How do you know?
    1. Come up with 3 more questions that can be answered with this data set.
- _NOTE: There's an issue with one of the CSV files. You will need to find a way to handle that error... Google it, and work around it!_
