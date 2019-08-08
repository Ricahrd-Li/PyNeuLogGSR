import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import GetSensorValue as gsv

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FuncAnimation
# i is frame
# Note: data should not be list but a value1!
def animate(i, xs, ys):
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(gsv.getSensorValue())

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('GSR diagram')
    plt.ylabel('GSR Value (μS)')

def draw():
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ), interval=100)
    plt.show()

if __name__ == '__main__':
    # Set up plot to call animate() function periodically
    draw()
