#My own grapher
from settings import *



pg.display.set_caption(TITTLE)
screen.fill(white)


#graph paper function
def paper(k):
    screen.set_clip(0,0,width,height)
    screen.fill(white)

    #draw the graph paper
    for i in range(width//k):
        gridx = k*i
        gridy = k*i
        pg.draw.line(screen, gridcolor, (gridx,0),(gridx,height), 1 )
        pg.draw.line(screen, gridcolor, (0,gridy),(width,gridy), 1 )

    # extra thick line
    pg.draw.line(screen,gridcolor, (width,0 ), (width, height), 5)

    #graph x and y axis
    midx, midy = width/(2*k), height/(2*k)
    pg.draw.line(screen,black,(midx*k,0), (midx*k,height),3)
    pg.draw.line(screen,black,(0,midy*k), (width,midy*k),3)

    #clip reset to all window
    screen.set_clip(None)

# the main function that runs the program
def main():
    #cleara screen
    screen.fill(white)

    #pixel per grid (always use a k that is a factor of width and height
    k = 25
    paper(k)

    #instructions and results

    instruct = font.render("Personal Grapher", 1, black)
    screen.blit(instruct, (width + 10, 20))

    instruct = font.render("Type in equation. Ex -3*x^2+1",1,black)
    screen.blit(instruct,(width+10, 70))

    instruct = font.render("select 'enter' when done or 'q' to start over. ",1,black)
    screen.blit(instruct,(width+10, 100))

    instruct = font.render("select 'backspace'  to delete last element ", 1, black)
    screen.blit(instruct, (width + 10, 130))
    instruct = font3.render("s=sin(), c=cos(), t=tan(), r=sqrt(), a=abs(),l=log10(), n=log(),e=e, p=pi", 1, black)
    screen.blit(instruct, (width + 10, 160))

    #start an array that will hold equation
    equation = []
    done = False


    active = True
    while active:
        #update the screen
        screen.set_clip(width+10, height-30, width + extraW, height)
        screen.fill(white)

        #join equation array without commas
        eq = ''.join(equation)
        eq = str.replace(eq,"","")

        #render and blit equation
        eqshow = font.render("Function:  y =" + eq,1,titlecolor)
        screen.blit(eqshow, (width+10 , height-30))


        pg.display.update()

        #keyboard and mouse action(event)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                active = False
                done = True

            elif event.type == pg.KEYDOWN:

                #math operation and symbols for the equation
                if event.unicode == u'*':
                    equation.append("*")
                elif event.unicode == u'+':
                    equation.append("+")
                elif event.unicode == u'-':
                    equation.append("-")
                elif event.unicode == u'/':
                    equation.append("/")
                elif event.unicode == u'.':
                    equation.append(".")
                elif event.unicode == u'(':
                    equation.append("(")
                elif event.unicode == u')':
                    equation.append(")")
                elif event.unicode == u'^':
                    equation.append("**")


                # numbers typed in for equation and the x variable
                elif event.key == K_1 or event.key == K_KP1:
                    equation.append("1")
                elif event.key == K_2 or event.key == K_KP2:
                    equation.append("2")
                elif event.key == K_3 or event.key == K_KP3:
                    equation.append("3")
                elif event.key == K_4 or event.key == K_KP4:
                    equation.append("4")
                elif event.key == K_5 or event.key == K_KP5:
                    equation.append("5")
                elif event.key == K_6 or event.key == K_KP6:
                    equation.append("6")
                elif event.key == K_7 or event.key == K_KP7:
                    equation.append("7")
                elif event.key == K_8 or event.key == K_KP8:
                    equation.append("8")
                elif event.key == K_9 or event.key == K_KP9:
                    equation.append("9")
                elif event.key == K_0 or event.key == K_KP0:
                    equation.append("0")

                #math function command
                elif event.key == K_s:
                    equation.append("sin(")
                elif event.key == K_c:
                    equation.append("cos(")
                elif event.key == K_t:
                    equation.append("tan(")
                elif event.key == K_r:
                    equation.append("sqrt(")
                elif event.key == K_a:
                    equation.append("abs(")
                elif event.key == K_n:
                    equation.append("log(")
                elif event.key == K_l:
                    equation.append("log10(")
                elif event.key == K_e:
                    equation.append("e")
                elif event.key == K_p:
                    equation.append("pi")


                elif event.key == K_x:
                    equation.append("x")

                elif event.key == K_RETURN:
                    active = False
                elif event.key == K_BACKSPACE:
                    equation.pop()
                elif event.key == K_q:
                    main()

    #an option to quit at entering equation or to graph
    if done:
        #quit
        pg.quit()
    else:
        #clip right side of the screen (except equation)
        screen.set_clip(width,0,width+extraW, height-30)
        screen.fill(white)
        screen.set_clip(None)
        #graph equation function called
        GraphEq(eq,k)
    sys.exit()
def GraphEq(eq,k):

    #graphing of the equation
    for i in range(width):
        try:
            x = (width/2-i)/float(k)
            y = eval(eq)
            pos1 = (width/2 + x*k, height/2-y*k)

            nx = x = (width/2 - (i+1))/float(k)
            ny = eval(eq)
            pos2 = (width/2+nx*k, height/2-ny*k)

            pg.draw.line(screen,graphcolor,pos1,pos2,3)
        except:
            pass
    #instruction and result
    title = font2.render("Personal Grapher", 1, titlecolor)
    screen.blit(title, (width + 10, 20))
    instruct = font.render("select q to start over", 1, black)
    screen.blit(instruct, (width + 10, 70))

    #compute and display y-intercept


    #RESIZE OF GRID INNSTRUCTION

    instruct = font.render("Select 's'  'm'  'l'  'o' for grid size ", 1, black)
    screen.blit(instruct, (width + 10, height - 70))

    #running loop to control the window
    active = True
    while active:
        #update the screen
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                active = False
            #commmand for starting over and other feature
            elif event.type == pg.KEYDOWN:
                if event.key == K_q:
                    main()
                elif event.key == K_y:
                    pg.draw.circle(screen, green, (int(width/2),int(height/2-yint*k)), 3)
                #resize command

                elif event.key == K_s:
                    k = 25
                    paper(k)
                    GraphEq(eq,k)
                elif event.key == K_m:
                    k = 20
                    paper(k)
                    GraphEq(eq,k)
                elif event.key == K_l:
                    k = 10
                    paper(k)
                    GraphEq(eq, k)
                elif event.key == K_o:
                    k = 5
                    paper(k)
                    GraphEq(eq, k)

    #quit
    pg.quit()



#Python' way of rnning a program

if __name__=='__main__':
    main()
