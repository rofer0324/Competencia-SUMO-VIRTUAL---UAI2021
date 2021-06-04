#RobotName: D4RK_SIDE

from RobotRL import RobotRL

robot = RobotRL()

def recto():
    robot.setVI(100)
    robot.setVD(100)

def retroceder():
    robot.setVI(-100)
    robot.setVD(-100)

def irIzquierda():
    robot.setVI(-40)
    robot.setVD(40)

def irDerecha():
    robot.setVI(40)
    robot.setVD(-40)

def parar():
    robot.setVI(0)
    robot.setVD(0)

def busqueda():
    di = robot.getDI()
    dd = robot.getDD()
    if((di < 20) and (dd < 20)):
        recto()
    elif ((di == 25) and (dd > 25)):
        robot.setVI(40)
        robot.esperar(0.5)
    elif ((di > 25) and (dd == 25)):
        robot.setVD(40)
        robot.esperar(0.5)
    else:
        irDerecha()
    
def impacto():
    bi = robot.getBI()
    bd = robot.getBD()
    if ((bi == True) or (bd == True)):
        retroceder()

def avispar():
    tp = robot.tiempoActual()
    print(tp)
    """Supuestamente, se obtiene la velocidad de los motores y si es menor que 20, o sea que esta atascado
        el robot verificara si el tiempo es mayor que 3 o menor que 10. si esto se cumple ejecutara las acciones.
        de lo contrario seguira con impacto(), busqueda(), noCaer()."""
    if((robot.getVi() < 20) and (robot.getVd() < 20)):
        if(tp >= 3.00) or (tp <= 10.00):
            retroceder()
            robot.esperar(1)
            irDerecha()
            robot.esperar(0.50)
    else:
        impacto()
        busqueda()
        noCaer()


def noCaer():
    if (robot.getColorPiso() > 35):
        retroceder()
        robot.esperar(0.75)
        irDerecha()
        robot.esperar(0.40)


while robot.step():
   avispar()
   
   """impacto()
    busqueda()
    noCaer()"""
