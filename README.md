
# Why are Customers Leaving?
### Telco Customer Churn Classification Project

<hr style="border-top: 10px groove green; margin-top: 1px; margin-bottom: 20px"></hr>

### Project Summary
<hr style="border-top: 2px groove green; margin-top: 1px; margin-bottom: 1px"></hr>

- Customers at the telecommunications company, Telco, are churning. 
- The goal of this project is to determine why customers are churning by developing machine learning classification models to predict customer churn based on the customer data available.  In particular, we will be looking into customers with automatic payments to see if there really is independent from churn.   
- The models will be created using Python, Pandas, Matplot, Seaborn, and Scikit-Learn libraries. 


### Project Planning:

PLAN -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

Working through the data science pipeline, we will acquire data using an acquire.py file which pulls data from the Telco churn database using SQL and joins 3 tables.
We will prepare the data using a prepare.py file which will get rid of unneeded columns, encode string values to 0s and 1s and create dummies.
Then we will explore the data by looking for possible relationships between features and look at how they are distribute by creating plots and looking at the data.
Next we will create models using Decision Tree, Random Forest and K - Nearest Neighbors Classifiers.  We will then compare the models that were run on training data to validate data before running our model on the test data to get the final accuracy.  We will then present the Jupyter Notebook with the code of this entire process to the class.  

#### Project Objectives

> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.

> - Create modules (acquire.py, prepare.py) that make your process repeateable.

> - Construct a model to predict customer churn using classification techniques.

> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.

> - Answer panel questions about your code, process, findings and key takeaways, and model.

#### Business Goals

> - Find drivers for customer churn at Telco. Why are customers churning?

> - Construct a ML classification model that accurately predicts customer churn.

> - Document your process well enough to be presented or read like a report.

#### Audience
> - Codeup Data Science students

#### Project Deliverables
> - A final report notebook 
> - A final report notebook presentation
> - All necessary modules to make my project reproducible

#### Project Context
> - The Telco dataset from the Codeup database.
> - The target variable for this assessment is going to be the feature Churn.



#### Data Dictionary

|Target|Datatype|Definition|
|:-------|:--------|:----------|
| churn                  | 7043 non-null: object| indicates whether the customer churned - yes or no  |              |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| customer_id            | 7043 non-null: object| customer identification number  |              |
| gender                 | 7043 non-null: object| customer gender, male or female  |              |
| senior_citizen      | 7043 non-null: int64 | indicates if customer is senior citizen - yes or no   |              |
| partner                | 7043 non-null: object| indicates if customer has a partner - yes or no  |              |
| dependents             | 7043 non-null: object| number of dependents a customer has  |              ||              |
| tenure                   | 7043 non-null: int64|number of months a customer has been with the company    |              |
| phone_service            | 7043 non-null: object | Type of phone service plan a customer has|              |
| multiple_lines           | 7043 non-null: object |indicates whether customer has multiple lines - yes or no|              |
| internet_service_type_id | 7043 non-null: int64|type of internet service customer has -  1 for DSL, 2 for Fiber Optic, 3 for None   |              |
| online_security          | 7043 non-null: object|indicates whether customer has online security - yes, no or no internet service  |              |
| online_backup            | 7043 non-null: object |indicates whether customer has an online backup -  yes, no, or no internet service  |              |
| device_protection        | 7043 non-null: object|indicates whether customer has device protection - yes, no, or no internet service  |              |
| tech_support             | 7043 non-null: object|indicates whether customer has tech support - yes, no, or no internet service  |              |
| streaming_tv             | 7043 non-null: object| |indicates whether customer has streaming tv - yes, no, or no internet service  |              |
| streaming_movies         | 7043 non-null: object| |indicates whether customer has device protection - yes, no, or no internet service  |              |
| contract_type_id         | 7043 non-null: int64| contract term of the customer  - month-to-month, one year, wo year)   |              |
| paperless_billing        | 7043 non-null: object|indicates whether customer has paperless billing - yes or no  |              |
| payment_type_id          | 7043 non-null: int64| customer payment method - 1 for electronic check, 2 for mailed check, 3 for automatic bank transfer, 4 for automatic credit card payment   |              |
| monthly_charges          | 7043 non-null: float64| amount charged to customer monthly  |              |
| total_charges            | 7043 non-null: object| Total amount customer has paid  |              |
***



###  Null Hypothesis:  ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0)

 -  Customers who churn are independent of whether they are on automatic payments

### Althernative Hypothesis:  

- Customers who churn are not dependent of whether they are on automatic payments 

### Answers to Hypotheses

- We reject the hypothesis that customers who churn are independent of whether they are on automatic payments.

    - This means that whether customers use automatic payments is an indicator of churn.  If they are on automatic payments, they are less likely to churn.  

### Key Findings
- Continuing to dig deeper into the initial findings from the previous Telco churn project, we can now state that the payment method that a customer uses is not independent of churn
- A customer's contract type and specific payment method are good indicators of churn.
- Customers who were on month-to-month contracts were more likely to churn
- Customers who use electronic checks as their payment method were more likely to churn.
- Customers who use automatic payment methods are less likely to churn than those not on automatic payments
- The model was successful in predicting churn accuracy with an accuracy of 0.88!
- That is a higher than the baseline which was 0.74.


### Recommendations & Takeaways
Offer incentives to convert to automatic payment plans
Offer incentives to convert month-to-month customers to longer term customers
Find out more about electronic check customers to determine if there are issues causing their churn
Next Steps
Continue running more models changing the hyperparameters to get a better model of churn
Group features together, such as month-to-month e-check customers who do not have partners or service types to run models on
Send a survery to customers who churn to further understand their actual reason for leaving
Fine tune the model by optimizing for precision or recall

### How to Recreate This Project

To recreate this project you will need the following files from this repository:
- README.md
- env file for you data base credentials to connect to the SQL database containing Telco data
- acquire.py
- prepare.py
- explore.py
- Final Telco Churn Project Notebook.ipynb


Instructions:
- Read the README.md
- Download the aquire.py, prepare.py, explore.py and final_report.ipynb files into your working directory, or clone this repository
- Add your own env file to your directory (user, password, host)  
- Run the Final Telco Churn Project Notebook.ipynb notebook