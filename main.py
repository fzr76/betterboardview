import eaglepy

# Open the boardview file
board = eaglepy.Board(r'path/to/file.brd')

# Access board information
print("Board name: ", board.name)
print("Board size: ", board.size)

# Access the layers
print("Layers: ", board.layers)

# Access the elements on the board
print("Elements: ", board.elements)

# Access specific element
element = board.get_element_by_name("U1")
print("Element Name: ", element.name)
print("Element Attributes: ", element.attributes)

# Access the signals
print("Signals: ", board.signals)

# Access specific signal
signal = board.get_signal_by_name("VCC")
print("Signal Name: ", signal.name)
print("Signal Pads: ", signal.pads)
