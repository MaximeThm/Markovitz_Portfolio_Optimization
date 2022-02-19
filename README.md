# Markovitz_Portfolio_Optimization

This python programm enables the optimal allocation of the selected assets to be obtained by following modern portfolio theory. 

Modern portfolio theory (MPT), or mean-variance analysis, is a mathematical framework for assembling a portfolio of assets such that the expected return is maximized for a given level of risk. It is a formalization and extension of diversification in investing, the idea that owning different kinds of financial assets is less risky than owning only one type. Its key insight is that an asset's risk and return should not be assessed by itself, but by how it contributes to a portfolio's overall risk and return. It uses the variance of asset prices as a proxy for risk.

Economist Harry Markowitz introduced MPT in a 1952 essay, for which he was later awarded a Nobel Prize in Economics.

# Inputs of the programm :

- list of tickers (from Yahoo Finance) : TSLA, AMZN, AAPL in this example. You can have as much as you want (but I tried with 120 different stocks and my computer doesn't like it...)
- start and end date of the period studied : 2520 days prior from today in the example (e.g. 10 years as a year has an average of 252 trading days)
- number of visual representation : 10,000 in this example (Below 100 you won't see much. Above 10,000 you better have a good computer)

# Outputs of the programm :

- the optimal weights of the assets or stocks you have choosen
- a nice visual representation of the efficient frontier (see https://en.wikipedia.org/wiki/Efficient_frontier for more information)


For the variables choosen here, the outputs are :

![Screenshot 2020-10-24 at 16 45 56](https://user-images.githubusercontent.com/35689674/97084683-19eeb580-1619-11eb-95ef-dc3f1033907b.png)

Which means the optimal weights are : 14.25% for Tesla, 41.96% for Apple and 43.79% for Amazon.

And then, the programm provides you with a nice visualization of the efficient frontier :

![Screenshot 2020-10-24 at 16 46 23](https://user-images.githubusercontent.com/35689674/97084800-b0bb7200-1619-11eb-8280-f1209b9f4822.png)

Have fun with this programm ! Tweak around the parameters and message me if you find a really nice combination of assets ;)
