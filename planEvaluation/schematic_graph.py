import numpy as np
import matplotlib.pyplot as plt


class PlotGraph:
   def __init__(self):
      # Mean of the distribution
      self.mean = 120
      self.mean2 = 100
      # satndard deviation of the distribution
      self.sd1 = 5
      self.sd2 = 1
      # size
      self.size = 100000
      
   def norm_dist(self):
      # creating first normal distribution data
      values = np.random.normal(self.mean, self.sd1, self.size)
      # creating second normal distribution data
      values2 = np.random.normal(self.mean2, self.sd2, self.size)

      return values, values2 
   
   def main(self):
      values, values2 = self.norm_dist()

      # plotting histograph
      plt.hist(values, 100, color='b')
      plt.hist(values2, 100, color='cyan')

      # plotting lines for first distribution
      plt.axvline(values.mean(), color='k', linestyle='dashed', linewidth=1)
      plt.text(values.mean() - 2, 1.5,'  $E_1$',rotation=90)
      plt.annotate(' ', xy=(75, 300), xytext=(100, 300),
            arrowprops=dict(arrowstyle='<->', linestyle='dashed', color='k', linewidth=1))
      plt.text(values.mean() - 3, 300 + 100, '  $\sigma_1$',rotation=0)


      # plotting lines for second distribution
      plt.axvline(values2.mean(), color='k', linestyle='dashed', linewidth=1)
      plt.text(values2.mean() - 2, 0.5, '  $E_2$',rotation=90)
      plt.annotate(' ', xy=(110, 300), xytext=(130, 300),
            arrowprops=dict(arrowstyle='<->', linestyle='dashed', color='k', linewidth=1))
      plt.text(values2.mean() - 3, 300 + 100, '  $\sigma_2$',rotation=0)

      plt.title('Comparison two reward distributions')
      plt.text(values.mean() - 10, -400, '  reward values',rotation=0)
      plt.show()

   

if __name__ == '__main__':
   plot_graph = PlotGraph()
   plot_graph.main()
   
