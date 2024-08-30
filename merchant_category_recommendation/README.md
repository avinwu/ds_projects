# Credit Card Merchant Category Recommendation - Loyalty Score Prediction
Imagine walking through an unfamiliar neighborhood, feeling hungry, and receiving a timely recommendation for a nearby restaurant that matches your personal tastes. Along with the recommendation, you get an exclusive discount from your credit card provider for a place just around the corner!

Currently, a major payment brand has established partnerships with local businesses to offer targeted promotions and discounts to cardholders. But the question remains: are these promotions effective? Do they enhance the customer experience? Do businesses see increased loyalty and repeat visits? Personalization is crucial.

To address this, machine learning models have been developed to understand the key aspects and preferences that drive customer behavior, from dining choices to shopping habits. However, these models have yet to be tailored to individual customer profiles. This is where your expertise is needed.

The challenge is to develop algorithms that can identify and deliver the most relevant opportunities to each customer by uncovering patterns in customer loyalty. This will enhance customer satisfaction, reduce ineffective marketing campaigns, and create a more personalized experience for every user.


**Data Dictionary**

| Sl. | Field Name | Field Description |
| :- | :- | :- |
|1| merchant_id | Unique merchant identifier |
|2| merchant_group_id | Merchant group (anonymized ) |
|3| merchant_category_id | Unique identifier for merchant category (anonymized ) |
|4| subsector_id | Merchant category group (anonymized ) |
|5| numerical_1 | anonymized measure |
|6| numerical_2 | anonymized measure |
|7| category_1 | anonymized category |
|8| most_recent_sales_range | Range of revenue (monetary units) in last active month --> A > B > C > D > E |
|9| most_recent_purchases_range | Range of quantity of transactions in last active month --> A > B > C > D > E |
|10| avg_sales_lag3 | Monthly average of revenue in last 3 months divided by revenue in last active month |
|11| avg_purchases_lag3 | Monthly average of transactions in last 3 months divided by transactions in last active month |
|12| active_months_lag3 | Quantity of active months within last 3 months |
|13| avg_sales_lag6 | Monthly average of revenue in last 6 months divided by revenue in last active month |
|14| avg_purchases_lag6 | Monthly average of transactions in last 6 months divided by transactions in last active month |
|15| active_months_lag6 | Quantity of active months within last 6 months |
|16| avg_sales_lag12 | Monthly average of revenue in last 12 months divided by revenue in last active month |
|17| avg_purchases_lag12 | Monthly average of transactions in last 12 months divided by transactions in last active month |
|18| active_months_lag12 | Quantity of active months within last 12 months |
|19| category_4 | anonymized category |
|20| city_id | City identifier (anonymized ) |
|21| state_id | State identifier (anonymized ) |
|22| category_2 | anonymized category |