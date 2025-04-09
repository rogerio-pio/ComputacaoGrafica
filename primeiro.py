import glfw

def main():
    glfw.init()
    window = glfw.create_window(500,500,'primeiro', None, None)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()




if __name__=='__main__':
    main()