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



## **Next Purchase date**

By predicting the next purchase date we can build out a strategy on top of this date to plan our next promotion move For a particular customer.

Like customers who will purchase within the next few days can be taken out of any promotional activities as they will be buying our product anyway, instead we can target the customers who will be buying our product in the next 30 days for way beyond that.

We have classified people in the class range of 0-20 days, customers who will buy our product in next 21-49 days and customers who will buy our product after 50 days.

We can target the group of customers who are in the 21-49 days category with a new promotional offer so that they can be converted way before their predicted buying date and target customers that are in category class after 50 days can be targeted in order to stop the customer churn.

## **Steps :**

1.  We segmented our customers in two groups: 6 months purchase behavior and a group with purchase behavior after 6 months. We are creating a cutoff date in our data.
2.  We create a data frame between the last purchase date in a 6 month group and the next purchase date after that.
3.  We take out RFM scores days between last their purchases and mean & standard deviation of the between the purchase in days.
4.  Using the shift function we will take out the last 3 dates of purchase and then the difference of days between these dates of purchase.
5.  We kept the customers that are having >3 purchases.
6.  We categorized out customers in three classes
> 1.  0–20: Customers that will purchase in 0–20 days — Class name: 2
> 2. 21–49: Customers that will purchase in 21–49 days — Class name: 1
>3. ≥ 50: Customers that will purchase in more than 50 days — Class name: 0
7.  Then used the xib classifier model we used it to predict the next purchase date class.



## **References :**

https://towardsdatascience.com/predicting-next-purchase-day-15fae5548027

https://flask-table.readthedocs.io/en/stable/

https://codepen.io/azouaoui-med/pen/wpBadb

https://docs.aws.amazon.com/

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/
