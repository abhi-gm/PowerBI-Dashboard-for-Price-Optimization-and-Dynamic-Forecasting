# **PowerBI Dashboard for Price Optimization and Dynamic Forecasting**

**CLAAT LINK:**  - https://codelabs-preview.appspot.com/?file_id=1G-kaFuvlpAOPTi676TQcSdJN6E11AXYdgCR-dbLP6uo#0

**Web App Link** - http://team1admproject.sharmashubh.com:8080/ 

## **Aim of the project is to -**
1.  Segmenting customers into different categories
2.  Finding the customer lifetime value and their churn rate.
3.  Building a dynamic pricing model and demanding forecasting.
4.  Predicting the next purchase date.
5.  Building the dashboard for the Nike marketers.
6.  Building a web app to host these dashboards.
7.  Hosting web applications in the Amazon web services.

We developed dashboards to help the Nike Marketers to help them in marketing their product better and have better sales

## **Demand forecasting and Dynamic pricing**

Format: ![Alt Text](https://github.com/Abhishek-Gargha-Maheshwarappa/INFO7374DigitalMarketingAnalytics/blob/master/Project/asset/Price_optimization.png)

## **Website insights**
Format: ![Alt Text](https://github.com/Abhishek-Gargha-Maheshwarappa/INFO7374DigitalMarketingAnalytics/blob/master/Project/asset/Nike_website_insights.png)


## **Use cases**

Nike is dealing with a weak supply chain, they are facing an unbalanced supply and demand problem. Through predictive analytics we will be predicting sales and the next customer purchase date which will help the company to better manage inventory and strategically plan their next moves.

1.  If the forecast shows an increase in sales, companies will take necessary measures to keep the inventory up in the supply chain to satisfy demand.
2.  If the forecast shows a coming dip in sales, Our Model will help to retain the customers. We will do this by analysing why churn occurs and also by targeting customers with specific promotions.
3.  We will be targeting customers by doing customer segmentation, Calculating their lifetime value(LTV) and then creating special promotions for them.
4.  We will also take out the effectiveness of our promotion campaign.
5.  We implement a dynamic price optimization model which will help to give consumer seasonal and promotional offers based on current prices, demand and inventory while still remaining profitable which is something quite difficult to achieve with a flat pricing model.

## **Dynamic pricing**

Format: ![Alt Text](https://github.com/Abhishek-Gargha-Maheshwarappa/PowerBI-Dashboard-for-Price-Optimization-and-Dynamic-Forecasting/blob/master/asset/dynamic_pricing.png)


## **Demand Forecasting**

The following driving factors for demand are considered in our demand forecasting model:

### **Price-related features such as:**

1.  The actual sales price and cost
2.  The discount of the price compared to MSRP (manufacturer's suggested retail price) or original price in other industries, and the relative price, the ratio between a product's price and the average price of all products in the same competing group.
3.  Product attributes such as the brand desirability and department information.
4.  Store attributes such as average traffic in the store, etc.

A demand forecasting model is built on the features mentioned above. The model's performance is evaluated through mean absolute percentage error (MAPE). The model is retrained monthly, since continuously-acquired transaction data can be used to improve the demand forecasting accuracy and, consequently, the price optimization results.

### **Price Optimization**

During price optimization, each product's price is constrained to a feasible range bounded by the wholesale cost and manufacturer's suggested retail price (MSRP)/original price. Companies may elect to tailor these constraints to their own business rules to reflect the differentiated pricing strategies they prefer for specific brands, departments, or stores.

An experiment is employed to evaluate the effect of price optimization strategy on profit. Stores are paired based on similarity and then divided into "treatment" and "control" groups. Stores in the treatment group accept the prices recommended by the optimization algorithm, whereas stores in the control group use the company's previous pricing strategy (which, in this demo scenario, is a randomized pricing strategy). The profit gain of the optimization approach can be estimated from the difference in profit between the treatment and control groups.
