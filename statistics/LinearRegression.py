from sklearn import linear_model
import  numpy as np
import matplotlib.pyplot as plt

__author__ = 'francesco'

class LinearRegression:
    def print_diag(self, y_type, x_type, y_dataframe, x_dataframe):
        if y_type == "sar":
            y = y_dataframe.User.values + y_dataframe.Nice.values + y_dataframe.System.values # Total CPU Utilization
            y_label = "Total CPU Utilization"
        elif y_type == "rubbos":
            y = y_dataframe.UavgTot.values # Total RUBBoS average Utilization
            y = y[~np.isnan(y)]
            y_label = "Total CPU Utilization"

        if x_type == "rubbos":
            x = x_dataframe.XavgTot.values # Total RUBBoS average Throughput
            x = x[~np.isnan(x)]
            x_label = "Total average Throughput"

        x = x.reshape(len(x), 1)
        y = y.reshape(len(y), 1)

        regr = linear_model.LinearRegression()
        regr.fit(x, y)

        plt.scatter(x, y)
        plt.plot(x, regr.predict(x), 'r-', linewidth=2, label="Linear Regression")
        plt.legend(loc='lower right')
        #plt.xlim(xmin=0)
        #plt.ylim(ymin=0)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        #plt.xticks(())
        #plt.yticks(())
        plt.show()