#CST-305
#11/13/2022
#Jacob Silviera 

#implementation using Lorenz equation
#program orginally written in Visual Studio 2019

# needed imports  
import numpy as np #import lib numpy as np needed for math
import matplotlib.pyplot as plt #for graphs 

while True == True:
    rValue = int(input("Enter value for r: ")) #r input to show to show fragmentation process 

    #set values for s, r and b as seen in the documentation for Lorenz system values
    def lorenz(x, y, z, s=10, r=rValue, b=8/3):
        '''
        Given:
        x, y, z: a point of interest in three dimensional space
        s, r, b: parameters defining the lorenz attractor
        Returns:
        x_dot, y_dot, z_dot: values of the lorenz attractor's partial
            derivatives at the point x, y, z
        '''
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot

    dt = 0.01 #the step size
    num_steps = 10000 #the number of steps

    # Need one more for the initial values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Set initial values
    xs[0], ys[0], zs[0] = (11.8, 4.4, 2.4) 

    # Step through "time", calculating the partial derivatives at the current point and using them to estimate the next point 
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt) #filling xs
        ys[i + 1] = ys[i] + (y_dot * dt) #filling ys
        zs[i + 1] = zs[i] + (z_dot * dt) #filling zs

    #Plots
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz r value: " + str(rValue)) #displays whatever the user input was for the r vlaue 
    plt.show()

    t = np.linspace(0, 100, num_steps+1) #set t for time points 

    plt.plot(t, xs, 'b-', label='x(t)')
    #new plot for x/t
    plt.title('x(t) JPG  r= ' + str(rValue))    #title
    plt.xlabel('t')                             #label the horizontal t
    plt.ylabel('X  JPG')                        #label the vertical x
    plt.legend()                                #the legend
    plt.show()                                  #plot and display
    
    plt.plot(t, ys, 'b-', label='y(t)')
    #new plot for y/t
    plt.title('y(t) PNG  r= ' + str(rValue))    #title
    plt.xlabel('t')                             #label the horizontal t
    plt.ylabel('Y  PNG')                        #label the vertical y
    plt.legend()                                #the legend
    plt.show()                                  #plot and display
    
    plt.plot(t, zs, 'b-', label='z(t)')         
    #new plot for z/t                           
    plt.title('z(t) GIF  r= ' + str(rValue))    #title
    plt.xlabel('t')                             #label the horizontal t
    plt.ylabel('Z  GIF')                        #label the vertical y
    plt.legend()                                #the legend
    plt.show()                                  #plot and display
    
    exitProg = input("press e to exit: ") #to end the loop asking the user for r value
    if exitProg == "e": #exits program 
        break
    else:
        continue
