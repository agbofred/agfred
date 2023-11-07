import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-poster')

def rev_quest():
    f = plt.figure(figsize=(6,5))
    axa = f.add_subplot(122)
    axb = f.add_subplot(121)
    axa.plot([5,4,3,2,1], 'ro-')
    f.savefig('SolA.png')
    del f

    f = plt.figure(figsize=(6,5))
    axa = f.add_subplot(121)
    axb = f.add_subplot(122)
    axa.plot([5,4,3,2,1], 'ro-')
    f.savefig('SolB.png')
    del f

    f = plt.figure(figsize=(6,5))
    axa = f.add_subplot(122)
    axb = f.add_subplot(121)
    axa.plot([5,4,3,2,1], 'ro')
    f.savefig('SolC.png')
    del f

    f = plt.figure(figsize=(6,5))
    axa = f.add_subplot(121)
    axb = f.add_subplot(122)
    axa.plot([1,2,3,4,5], 'ro-')
    f.savefig('SolD.png')
    del f

def labels_example():
    # Labels
    # plt.style.use('ggplot')
    f = plt.figure()
    ax1 = f.add_subplot(211)
    ax2 = f.add_subplot(212)
    ax1.plot((1,2,3,4))
    ax2.plot([1,2,3],[3,2,3])

    ax1.set_xlabel('Axis 1 X')
    ax2.set_xlabel('Axis 2 X')

    ax1.set_ylabel('Axis 1 Y')
    ax2.set_ylabel('Axis 2 Y')

    ax1.set_title('Title of Plot 1')
    ax2.set_title('Title of Plot 2')

    f.suptitle('Two glorious plots!', fontsize=26)
    #f.subplots_adjust(top, bottom, right, left, hspace, wspace)

    # Ticks
    ax1.set_xlim(0,5)
    ax1.set_ylim(0,4)

    ax2.set_xticks([0,1,1.5,2,3])
    ax2.set_xticklabels(['A','B','C','D','E'])

    plt.show()

def shared_axes():
    # Shared Axes
    # Overlapping
    f = plt.figure(figsize=(8,6))
    ax1 = f.add_subplot(111)
    ax1.plot([1,2,3,4],[1,4,9,16])

    ax2 = ax1.twinx()
    ax2.plot([1,2,3,4],[10,100,1000,10000],'go--', markersize=20)
    ax2.set_yscale('log')
    plt.show()

    # Side by side
    f = plt.figure()
    ax1 = f.add_subplot(121)
    ax2 = f.add_subplot(122, sharey=ax1)
    f.subplots_adjust(wspace=0.05)
    plt.setp(ax2.get_yticklabels(), visible=False)

    ax1.plot(range(1,10), 'r^-')
    ax2.plot(range(10,1,-1), 'gs-.')

    ax1.set_ylim(0,10)
    plt.show()


def sample_plots():
    xs = np.arange(-5,5,0.1)
    ys = np.arange(-5,5,0.1)
    X,Y = np.meshgrid(xs,ys)

    Z = np.sin(X)*np.cos(Y)

    # imshow
    f = plt.figure(figsize=(5,5))
    ax = f.add_subplot(111)
    ax.imshow(Z, origin='lower', extent=[-5,5,-5,5])
    ax.set_title('Heatmaps')
    f.savefig('../Images/Heatmap.png')
    del f

    # Contours
    f = plt.figure(figsize=(5,5))
    ax = f.add_subplot(111)
    ax.contour(X,Y,Z,10)
    ax.set_title('Contours')
    f.savefig('../Images/Contour.png')
    del f

    # Histogram
    import random
    z = [random.randint(1,6)+random.randint(1,6) for i in range(1000)]
    f = plt.figure(figsize=(5,5))
    ax = f.add_subplot(111)
    ax.hist(z)
    ax.set_title('Histograms')
    f.subplots_adjust(left=.2)
    f.savefig('../Images/Histogram.png')
    del f

    # Bar Chart
    z = [1,2,4,9,16]
    f = plt.figure(figsize=(5,5))
    ax = f.add_subplot(111)
    ax.bar(['A','B','C','D','E'],z)
    ax.set_title('Bar Plots')
    f.subplots_adjust(left=.2)
    f.savefig('../Images/BarPlot.png')
    del f

    # Pie Chart
    z = [1,2,4,9,16]
    f = plt.figure(figsize=(5,5))
    ax = f.add_subplot(111)
    ax.pie(z,[0,0,.2,0,0],labels=['A','B','C','D','E'])
    ax.set_title('Pie Charts')
    f.savefig('../Images/PieChart.png')
    del f

def graphics_demo():
    import graphics as g

    w = g.GraphWin("Example",100,100)
    w.setBackground('white')
    c = g.Circle(g.Point(50,50), 20)
    c.draw(w)
    w.getMouse()
    c.setFill('red')
    w.getMouse()
    w.close()

