import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd
import numpy as np

class InteractiveBarChart:
    
    def __init__(self, initial_y=42000):
        np.random.seed(12345)
        self.df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
        self.m_list = [] # means per year
        self.h_list = [] # confidence interval widths per year
        self.se_list = [] # standard error of the mean per year
        for i in self.df.index:
            d = self.df.loc[i]
            m = np.mean(d)
            se = st.sem(d)
            h = se * st.t.ppf(0.975,len(self.df.columns)-1) #95% CI
            self.m_list.append(m)
            self.h_list.append(h)
            self.se_list.append(se)
        self.fig = plt.figure()
        self.canvas = self.fig.canvas
        self.draw_bars(initial_y)
        
    def click_on_line(self, event):
        self.follower = self.canvas.mpl_connect("motion_notify_event", self.follow_mouse)
        self.releaser = self.canvas.mpl_connect("button_release_event", self.release_click)
    
    def follow_mouse(self, event):
        self.line.set_ydata([event.ydata, event.ydata])
        self.canvas.draw()

    def release_click(self, event):
        self.canvas.mpl_disconnect(self.follower)
        self.canvas.mpl_disconnect(self.releaser)
        self.line.set_ydata([event.ydata, event.ydata])
        self.draw_bars(event.ydata)

    def draw_bars(self, y):
        plt.cla()
        # update shown value of y
        for txt in self.fig.texts:
            txt.remove()
        self.fig.text(0.2, 0.8, "y={}".format(int(y)), color="orange", fontsize=15)
        # choose colors of bars
        colors = []
        cmap = matplotlib.cm.get_cmap("seismic")
        for i in range(len(self.df.index)):
            z = (y - self.m_list[i])/self.se_list[i]
            prob = 1 - st.t.cdf(z, len(self.df.columns)-1)
            colors.append(cmap(prob))
        # plot the bars
        plt.bar(self.df.index, self.m_list, yerr=self.h_list, tick_label=self.df.index, color=colors, edgecolor="black")
        plt.tick_params(axis="x", bottom=False)
        # plot the line
        self.line = matplotlib.lines.Line2D([1991.4, 1995.6],[y, y], picker=5, color="orange")
        plt.gca().add_line(self.line)
        self.canvas.mpl_connect("pick_event", self.click_on_line)

if __name__=="__main__":
    InteractiveBarChart()
