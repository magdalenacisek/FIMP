import pandas as pd
import plotly.plotly as ply
# import cufflinks as cf
import matplotlib.pyplot as plt
from plotly.plotly import *
from statsmodels.tsa.seasonal import seasonal_decompose
plotly.tools.set_credentials_file(username='magdaP', api_key='BCkmP5irLLcyYL3sjHTu')

file = r'Electric_Production.csv'
data = pd.read_csv(file, index_col=0)
data.index = pd.to_datetime(data.index)
data.columns = ['Energy Production']
# data.plot()
# plt.show()

result = seasonal_decompose(data, model='multiplicative')
fig = result.plot()
plot_mpl(fig)

print "test Magda"
