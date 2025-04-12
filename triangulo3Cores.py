import glfw
from OpenGL.GL import *

vertices = [
    [-0.5, -0.5],
    [0.5, -0.5],
    [0.0, 0.5]
]

cores = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

#Função para configurações iniciais da miha aplicação
def init():
    glClearColor(1,1,1,1) #os 3 primeiros são referentes a cores e o ultimo valor referente a opacidade

#atualizar a renderização da cena
def render():
    global vertices, cores
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    
    for v,c in zip(vertices, cores):
        glColor3fv(c)
        glVertex2fv(v)

    glEnd()


def main():
    glfw.init()                                                 #iniciando API GLFW
    window = glfw.create_window(500,500,'primeiro', None, None) #Criando Janela
    glfw.make_context_current(window)                           #Criando conexão OpenGl na janela
    init()

    while not glfw.window_should_close(window):                 #enquanto a janela não é fechada
        glfw.poll_events()                                      #tratamento de eventos
        render()
        glfw.swap_buffers(window)                               #troca de frame buffers
    glfw.terminate()                                            #finalizando API 




if __name__=='__main__':
    main()