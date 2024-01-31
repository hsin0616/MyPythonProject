"""
File: babygraphics.py
Date: Jan 3, 2024
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui


FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    interval_width = (width - 2 * GRAPH_MARGIN_SIZE) / (len(YEARS))
    x = GRAPH_MARGIN_SIZE + year_index * interval_width
    return int(x)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Bottom horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, 2*GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, 2*GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # Vertical lines and year labels
    for i, year in enumerate(YEARS):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, GRAPH_MARGIN_SIZE, x, CANVAS_HEIGHT, width=LINE_WIDTH, fill='gray')
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX, text=str(year), anchor='nw')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_index = 0
    for name in lookup_names:
        ranks = []
        coordinates = []  # store (x,y)
        for i in range(len(YEARS)):
            year = YEARS[i]  # int
            x = get_x_coordinate(CANVAS_WIDTH, i)
            if str(year) in name_data[name]:  # name_data is {str: {str: str}}
                rank = int(name_data[name][str(year)])
                y = GRAPH_MARGIN_SIZE + (rank / MAX_RANK) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                canvas.create_text(x + TEXT_DX, y, text=f"{name} {rank}", anchor='sw', fill=COLORS[color_index])
            else:
                rank = None  # if name is not in name_data for the current year
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(x + TEXT_DX, y, text=f"{name} *", anchor='sw', fill=COLORS[color_index])
            ranks.append(rank)
            # print(f"Name: {name}, Year: {year}, Rank: {rank}")
            coordinates.append((x, y))

        # Lines connecting data points
        for i in range(1, len(coordinates)):
            x0, y0 = coordinates[i - 1]
            x1, y1 = coordinates[i]
            canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH, fill=COLORS[color_index])
        color_index = (color_index + 1) % len(COLORS)
        # print(f"{name}'s ranks: {ranks}")


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
