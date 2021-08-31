
# Why are Customers Leaving?
### Telco Customer Churn Classification Project

<hr style="border-top: 10px groove green; margin-top: 1px; margin-bottom: 20px"></hr>

### Project Summary
<hr style="border-top: 2px groove green; margin-top: 1px; margin-bottom: 1px"></hr>

- Customers at the telecommunications company, Telco, are churning. 
- The goal of this project is to determine why customers are churning by developing machine learning classification models to predict customer churn based on the customer data available. 
- The models will be created using Python, Pandas, Matplot, Seaborn, and Scikit-Learn libraries. 


### Project Planning:

PLAN -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

Working through the data science pipeline, 

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

 - Customers not on automatic payment methods pay more than month-to-month customers on automatic payment methods. 


### Althernative Hypothesis:  

- Customers not on automatic payment methods pay less than or equal to customers on automatic payment methods.  


### Instructions for Recreating This Project

project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?),



### Answers to Hypotheses


### Key Findings


### Recommendations & Takeaways

*** 