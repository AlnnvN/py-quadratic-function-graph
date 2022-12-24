graph = []
GRAPH_SIZE = 100

def create_x_y_lines():
    for i in range(GRAPH_SIZE):
        graph[GRAPH_SIZE//2][i] = '_'
        graph[i][GRAPH_SIZE//2] = "|"

def create_graph():
    for row in range(GRAPH_SIZE):
        graph.append([])
        for col in range(GRAPH_SIZE):
            graph[row].append(' ')
    create_x_y_lines()

def place_canvas(x,y):
    if x+GRAPH_SIZE//2>0 and -y+GRAPH_SIZE//2>0:
        if x+GRAPH_SIZE//2<GRAPH_SIZE-1 and -y+GRAPH_SIZE//2<GRAPH_SIZE-1:
            graph[-y+GRAPH_SIZE//2][x+GRAPH_SIZE//2] = '#'

def place_function(a,b,c):
    for x in range(-GRAPH_SIZE//2,GRAPH_SIZE//2):
        y = a*x**2 + b*x + c
        place_canvas(int(x),int(y))
        print(f'placing at ({int(x)},{int(y)})')

def print_graph():
    for row in graph:
        for col in row:
            print(col,end=' ')
        print("\n",end='')


#main
create_graph()
a = float(input('a(x²): '))
b = float(input('b(x): '))
c = float(input('c: '))
place_function(a,b,c)
print_graph()


