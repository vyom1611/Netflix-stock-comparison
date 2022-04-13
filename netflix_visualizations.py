


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

netflix_stocks = pd.read_csv('NFLX.csv')

dowjones_stocks = pd.read_csv('DJI.csv')

netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
#The data is representated by days for netflix_stock_quarterly but by months for netflix_stocks


#Replacing the column names 'Adj Close' to Price for better understanding of the closing value of the stocks.
netflix_stocks_quarterly.rename(columns={'Adj Close': 'Price'}, inplace=True)
dowjones_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
netflix_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)

# We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!


ax = sns.violinplot( data=netflix_stocks_quarterly,x='Quarter', y='Price')
ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')
ax.set_ylabel("Closing Stock Price")
ax.set_xlabel("Business Quarters in 2017")


# ## Graph Literacy
# - What are your first impressions looking at the visualized data?
#   The price of the stock was increased.
# - What were the highest and lowest prices?
#   Lowest ~ 125 and Highest ~ 210

# Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart.

x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions, earnings_actual, color='Red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='Blue',alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")

#The regions with purple dots have the estimate and actual earnings the most similar.


# Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side.

# The metrics below are in billions of dollars ._.
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1
t = 2
d = 4
w = 0.8
bars1_x = [t*element + w*n for element
             in range(d)]

plt.bar(bars1_x,revenue_by_quarter)



# Earnings
n = 2
t = 2
d = 4
w = 0.8
bars2_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars2_x, earnings_by_quarter)



middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.legend(labels)
plt.title('Netflix Earnings')
plt.xticks(middle_x, quarter_labels)

#Both the revenue and earnings have been on an upwards trend as visible from the graph in 2017.
#Roughly 1.75% of the Total revenue constitutes the earnings


# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure.


# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')





# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Dow Jones')
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')
plt.subplots_adjust(wspace=.5)





# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?

# - Which was more volatile?
# - How do the prices of the stocks compare?
