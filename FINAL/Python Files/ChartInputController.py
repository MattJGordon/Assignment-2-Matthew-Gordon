from PieChart import PieChart
from BarGraph import BarGraph
from ScatterGraph import ScatterGraph
from BoxPlot import BoxPlot


def make_bar_graph(title, labels, values, chart_names):
    try:
        bar_graph = BarGraph(title, labels, values, chart_names)
        bar_graph.give_graph()
    except (ValueError, IndexError):
        print("Incorrect arguments in bar graph")
    else:
        print("Bar Graph Made!")


def make_pie_chart(title, labels, values):
    try:
        pie_chart = PieChart(title, labels, values)
        pie_chart.give_graph()
    except (ValueError, IndexError):
        print("Incorrect arguments in pie chart")
    else:
        print("Pie Chart Made!")


def make_scatter_graph(title, labels, values, values_two):
    try:
        scatter_graph = ScatterGraph(title, labels, values, values_two)
        scatter_graph.give_graph()
    except (ValueError, IndexError):
        print("Incorrect arguments in scatter graph")
    else:
        print("Scatter Graph Made!")


def make_box_plot(title, values, values_two, chart_names):
    try:
        box_plot = BoxPlot(title, values, values_two, chart_names)
        box_plot.give_graph()
    except (ValueError, IndexError):
        print("Incorrect arguments in scatter plot")
    else:
        print("Box Plot Made!")

make_bar_graph('This is a bar graph', ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500], ['words name', 'Numbers Names'])
make_pie_chart('This is a pie chart', ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen'], [4500, 2500, 1053, 500])
make_scatter_graph('This is a scatter graph', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500], [500, 2400, 1453, 5700])
make_box_plot('This is a box plot', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
