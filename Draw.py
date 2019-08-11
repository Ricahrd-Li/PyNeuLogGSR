import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import GetSensorValue as gsv
import keyboard as kb

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
    
# This function is called periodically from FuncAnimation
# i is frame
# Note: data should not be list but a value!
def animate(i, xs, ys,f):
    # Add x and y to lists
    t = dt.datetime.now().strftime('%H:%M:%S.%f')
    xs.append(t)
    f.write('('+ t + ',')
    v = gsv.getSensorValue()
    ys.append(v)
    f.write("%f )\n" % v)

    # write data into txt file and close the diagram
    # bug? 
    if kb.is_pressed('q'):
        f.close()

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    ax.set_ylim([0,7])

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('GSR diagram')
    plt.ylabel('GSR Value (μS)')

def draw():
    # write GSR data into a txt file
    f = open("exp.txt","w+")
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys,f), interval=100)
    plt.show()

if __name__ == '__main__':
    # Set up plot to call animate() function periodically
    draw()
