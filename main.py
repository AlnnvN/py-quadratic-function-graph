graph = []
graph_size = 75

def create_x_y_lines():
    for i in range(graph_size):
        graph[graph_size//2][i] = '_'
        graph[i][graph_size//2] = "|"

def create_graph():
    for row in range(graph_size):
        graph.append([])
        for col in range(graph_size):
            graph[row].append(' ')
    create_x_y_lines()

def place_canvas(x,y):
    if x < graph_size-1 and y < graph_size-1 and x+graph_size//2>0 and -y+graph_size//2>0:
        graph[-y+graph_size//2][x+graph_size//2] = '#'

def place_function(a,b,c):
    for x in range(-graph_size//2,graph_size//2):
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


