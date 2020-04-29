from graphviz import Source
path = 'rulegrph_scaled.dot'
s = Source.from_file(path)
s.view()