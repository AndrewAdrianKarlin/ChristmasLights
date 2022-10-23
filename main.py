import PySimpleGUI as sg
import time


layout = [
    [
        sg.Graph(
            canvas_size=(400, 400),
            graph_bottom_left=(0, 0),
            graph_top_right=(400, 400),
            key="graph"
        )
    ]
]

window = sg.Window("rect on image", layout, finalize=True)

graph = window.Element("graph")

i = 0
circles = {}

while i<7:
    j = i*62+12
    circles["circ{0}".format(i)] = graph.draw_circle([j, 200], 12, fill_color=None, line_color="black", line_width=1)
    i=i+1

def updatePlot(key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 12, fill_color=color, line_color="black")
    return

while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    #else:
    #    time.sleep(1)
    #    updatePlot("graph", "red")
    #    window.read(timeout=0)
    #    time.sleep(1)
    #    updatePlot("graph", "green")

