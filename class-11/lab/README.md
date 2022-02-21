# Lab: Numpy Arrays

## Overview

Today we'll be constructing chess boards like it's 1980.

No prebuilt images, just the power of arrays and pixel art.

## Feature Tasks and Requirements

Your job is to render out chess boards with red and blue queens on them.

We're keeping it really basic here so the only pieces are queens and each queen is represented by a blue or red square.

Chess board is an 8 by 8 grid of alternating black and white squares. The queens are red and blue squares.

Each board will have one red and one blue queen at different coordinates. In addition to displaying the board you'll need to identify if the queens are "under attack" based on their coordinates.

## Implementation Notes

- Define a `ChessBoard` class
- should contain an 8x8 grid
  - Each cell in grid should have a color represented in RGB format.
    - black = (0,0,0)
    - white = (1,1,1)
    - blue = (0,1,1)
    - red = (1,.2,0)
- should have `add_red` method that accepts a row and column as input which colors corresponding cell.
- should have `add_blue` method that accepts a row and column as input which colors corresponding cell.
- should have `render` method that displays the chess board on screen with red and blue shown in correct locations
- should have `is_under_attack` method that return boolean if red is under attack by a blue piece horizontally, vertically or diagonally
- Diagonal attacks can come from four directions. Make sure to handle all of them.
- Render your board for each `is_under_attack` scenario:
  - Horizontal (aka same row).
  - Vertical (aka same column).
  - Four Diagonals.
  - A "Not Under Attack" scenario.

### User Acceptance Tests

- There are no acceptance tests required.
- But Notebook should clearly show the various `is_under_attack` scenarios have been handled.


### Stretch Goal

- Enlarge the chessboard to allow for pixel art drawn pieces. 16x16 ought to be enough.
- Add more attacking queens.
- Add opacity to cell colors.

## Configuration & Submission

Kaggle is an excellent all around resource and has good, free notebook hosting.

- Create account at [Kaggle](https://www.kaggle.com/){:target="_blank"}.
- Create a new project by clicking `+ Create` button.
- Name project `Chess Board`.
- Click `Share` button and select `Public` access.
- Submit the Public URL for Notebok.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.





