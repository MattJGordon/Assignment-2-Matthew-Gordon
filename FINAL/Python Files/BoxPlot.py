import plotly.graph_objs as go
import plotly
import os.path

class BoxPlot(object):

    def __init__(self, title, values, values_two, chart_names):
        self.values_two = values_two
        self.title = title
        self.values = values
        self.chart_names = chart_names

    def trace_zero(self):
        trace0 = go.Box(
            y=self.values,
            name=self.chart_names[0]
        )
        return trace0

    def trace_one(self):
        trace1 = go.Box(
            y=self.values_two,
            name=self.chart_names[1]
        )
        return trace1

    def give_graph(self):
        data = [BoxPlot.trace_zero(self), BoxPlot.trace_one(self)]
        layout = go.Layout(
            title=self.title,
        )
        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename=self.title + '.html')
        if (os.path.exists(self.title + '.html')):
            return True