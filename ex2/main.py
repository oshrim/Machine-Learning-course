import numpy as np
import matplotlib.pyplot as plt

global x0,x1,x2,desResult
global w0,w1,w2
global c0,c1,c2
global sum
global network
global t,r
global error,correction
global count

def init_all():
    '''
    Initialize all global vars
    :return: void
    '''
    global w0,w1,w2
    global c0,c1,c2
    global sum,network,t,r
    global error,correction,count
    w0 =0
    w1 =-0.5
    w2 =-0.5
    c0 =0
    c1 =0
    c2 =0
    sum =0
    network =0
    t=0
    error = 0
    correction=0
    r=0.1
    count =0

def getXs(array):
    '''
    get the current x0 x1 and x2
    :param array: in the array there are the x's
    :return: void
    '''
    global x0,x1,x2,desResult
    x0 = array[0]
    x1 = array[1]
    x2 = array[2]
    desResult = array[3]

def setCs(array):
    '''
    put the needed c's at the global vars
    :param array: array contain the x's
    :return: set the global c's vars
    '''
    global c0,c1,c2
    global w0,w1,w2
    global sum
    c0 = array[0]*w0
    c1 = array[1]*w1
    c2 = array[2]*w2
    sum = c0+c1+c2
    #print c0,c1,c2

def set_network():
    '''
    set the network to be 0 or 1
    :return:
    '''
    global sum,network,t
    if(sum>t):
        network=1
    else:
        network=0
    #print network

def get_error(desResult):
    '''
    get the error by the desired result
    :param desResult: contain the result we expected
    :return:
    '''
    global error,network
    error = desResult-network
    #print error

def getCorrection():
    '''
    chech the correction needed and update the global var
    :return:
    '''
    global r,correction,error
    correction= r*error
 #   print correction

def final_wight(array):
    '''
    set the final w's for the iteration
    :param array: contain the x's
    :return:
    '''
    global w0,w1,w2,correction,count
    lastw0 = w0
    lastw1 = w1
    lastw2 = w2
    w0=array[0]*correction +w0
    w1=array[1]*correction +w1
    w2=array[2]*correction +w2
    if lastw0==w0 and lastw1 ==w1 and lastw2 ==w2:
        count = count +1
    else:
        count = 0
    print w0,w1,w2 , count

def printplot(nand):
    '''
    print the plot each iteration
    :param nand: np array to get the x's and the desired result.
    :return:
    '''
    global w0,w1,w2,t
    a = np.array([w0, w1, w2])
    plt.title('Perception')
    plt.plot([nand[0][1],nand[1][1],nand[2][1],nand[3][1]],[nand[0][2],nand[1][2],nand[2][2],nand[3][2]],'ro')
    plt.axis([-8,8,-8,8])
    plt.xlabel('x1')
    plt.ylabel('x2')
    x1 = np.arange(-8.,8.,0.2)
    if w2 == 0 :
        return

    x2 = -(w1*x1 +w0 +t)/w2
    plt.plot(x1,x2)
    plt.show()


def main():
    '''
    main function, do the iterations and use other functions of the program.
    :return:
    '''
    global x1,x2,desResult,count

    nand = np.array([[1,0,0,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]) #set nand as np array

    init_all()
    while True:
        for row in nand:
            getXs(row)
            setCs(row)
            set_network()
            get_error(row[3])
            getCorrection()
            final_wight(row)
            printplot(nand)
        if count>=3: #at least 2 iterations
            break

if __name__ == '__main__':
    main()