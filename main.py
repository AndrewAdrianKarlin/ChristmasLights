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
positions = []
colors = ["#ff0000", "#cc0000", "#b30000", "#800000", "#660000", "#4d0000", "#000000"]

while i<7:
    j = i*62+12
    positions.append(j)
    circles["circ{0}".format(i)] = graph.draw_circle([j, 200], 12, fill_color=colors[i], line_color="black", line_width=1)
    i=i+1

def updatePlot(key, circles, positions):
    graph = window.Element("graph")
    i = 0
    j = 0
    while i<7:
        k = i + 1
        if k == 7:
            k = 0
        while j<7:
            graph.RelocateFigure(j+1, positions[k], 200)
            window.read(timeout=0)
            k = k+1
            if k == 7:
                k = 0
            j = j + 1
        j = 0
        i = i + 1
    return

while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    else:
        updatePlot(graph, circles, positions)

