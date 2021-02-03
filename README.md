# interactiveGraph
Interactive bar chart with bar colors dependent of distribution compared to reference value.

This project is part of an assignment during the online course "Applied Plotting, Charting & Data Representation in Python" from the University of Michigan, through the Coursera platform. 

A bar chart with 95% confidence intervals represents some data for four years (1992 to 1995). A horizontal line represents a value of reference y. The probability that the distribution for each year is larger than this constant value y is mapped as a color to the corresponding bar (e.g. a gradient ranging from dark blue for the distribution being certainly below this y-axis, to white if the value is certainly contained, to dark red if the value is certainly not contained as the distribution is above the axis).

A screenshot of the chart is visible in figure example.png.

The chart is interactive because the user can move the horizontal line and see the changes of color in the bars resulting from the new position of the line.
