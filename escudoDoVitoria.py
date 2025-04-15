import glfw
from OpenGL.GL import *

vertices = [
    [0.0,0.5],
    [-0.9, 0.5],
    [-0.9, 0.2],
    [0.0, 0.5],
    [0.9, 0.5],
    [0.9, 0.2],
    [0.0,0.2],
    [0.9, 0.2],
    [0.0,0.5],
    [0.0,0.2],
    [-0.9, 0.2],
    [0.0,0.5],

    [0.0,-0.4],
    [-0.9,-0.4],
    [-0.9,-0.1],
    [0.0, -0.4],
    [0.9, -0.4],
    [0.9, -0.1],
    [0.0,-0.1],
    [0.9, -0.1],
    [0.0,-0.4],
    [0.0,-0.1],
    [-0.9, -0.1],
    [0.0,-0.4],
]

verticesLinhas =[
    [0.9, 0.8],
    [0.9, -0.7],
    [-0.9, -0.7],
    [-0.9, 0.8]
]
#Função para configurações iniciais da miha aplicação
def init():
    glClearColor(0,0,0,1) #os 3 primeiros são referentes a cores e o ultimo valor referente a opacidade
    glPointSize(5)
    glLineWidth(3)

#atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)

    #pontos
    glColor3f(1,0,0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_POINTS)
    for v in vertices:
        glVertex2fv(v)
    glEnd()

    glColor3f(1,0,0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLES)
    for v in (vertices):
        glVertex2fv(v)
    glEnd()

    #preto
    #triangulos linhas
    glColor3f(1,1,1)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_LINE_LOOP)
    for v in verticesLinhas:
        glVertex2fv(v)
    glEnd()

def main():
    glfw.init()                                                 #iniciando API GLFW
    window = glfw.create_window(600,500,'primeiro', None, None) #Criando Janela
    glfw.make_context_current(window)                           #Criando conexão OpenGl na janela
    init()

    while not glfw.window_should_close(window):                 #enquanto a janela não é fechada
        glfw.poll_events()                                      #tratamento de eventos
        render()
        glfw.swap_buffers(window)                               #troca de frame buffers
    glfw.terminate()                                            #finalizando API 




if __name__=='__main__':
    main()