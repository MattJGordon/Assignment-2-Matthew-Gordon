import unittest
from PieChart import PieChart
from BarGraph import BarGraph
from ScatterGraph import ScatterGraph
from BoxPlot import BoxPlot
"from FileHandler import FileHandler"


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_pie_title(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertEqual(pie_chart.test_title(), 'pie title')

    def test_pie_labels(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertEqual(pie_chart.test_labels(), ['one', 'two'])

    def test_pie_values(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertEqual(pie_chart.test_values(), [1, 2])

    def test_bar_title(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_title(), 'bar title')

    def test_bar_labels(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_labels(), ['one', 'two'])

    def test_bar_values(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_values(), [1, 2])

    def test_bar_names(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertEqual(bar_graph.test_names(), ['chart name 1', 'chart name 2'])

    def test_scatter_title(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_title(), 'scatter title')

    def test_scatter_labels(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_labels(), ['Oxygen', 'Hydrogen'])

    def test_scatter_values(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_values(), [4500, 2500, 1053, 500])

    def test_scatter_values_two(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertEqual(scatter_graph.test_values_two(), [500, 2400, 1453, 5700])

    def test_pie_build(self):
        pie_chart = PieChart('pie title', ['one', 'two'], [1, 2])
        self.assertTrue(pie_chart.give_graph())

    def test_bar_build(self):
        bar_graph = BarGraph('bar title', ['one', 'two'], [1, 2], ['chart name 1', 'chart name 2'])
        self.assertTrue(bar_graph.give_graph())

    def test_box_build(self):
        box_plot = BoxPlot('box title', [4500, 2500, 1200], [500, 6000, 2400], ['chart one', 'chart 2'])
        box_plot.trace_one()
        box_plot.trace_zero()
        self.assertTrue(box_plot.give_graph())

    def test_scatter_build(self):
        scatter_graph = ScatterGraph('scatter title', ['Oxygen', 'Hydrogen'], [4500, 2500, 1053, 500],
                                     [500, 2400, 1453, 5700])
        self.assertTrue(scatter_graph.give_graph())

if __name__ == '__main__':
    unittest.main()
