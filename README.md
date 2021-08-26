
# Why are Customers Leaving?
### Telco Customer Churn Classification Project

<hr style="border-top: 10px groove green; margin-top: 1px; margin-bottom: 20px"></hr>

### Project Summary
<hr style="border-top: 2px groove green; margin-top: 1px; margin-bottom: 1px"></hr>

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



#### Data Dictionary

|Target|Datatype|Definition|
|:-------|:--------|:----------|
| churn                  | 7049 non-null: object  |              |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| customer_id            | 7049 non-null: object  |              |
| gender                 | 7049 non-null: object  |              |
| is_senior_citizen      | 7049 non-null: int64   |              |
| partner                | 7049 non-null: object  |              |
| dependents             | 7049 non-null: object  |              |
| phone_service          | 7049 non-null: int64   |              |
| internet_service       | 7049 non-null: int64   |              |
| contract_type          | 7049 non-null: int64   |              |
| payment_type           | 7049 non-null: object  |              |
| monthly_charges        | 7049 non-null: float64 |              |
| total_charges          | 7038 non-null: float64 |              |
| churn                  | 7049 non-null: object  |              |
| tenure                 | 7049 non-null: int64   |              |
| is_female              | 7049 non-null: bool    |              |
| has_churned            | 7049 non-null: bool    |              |
| has_phone              | 7049 non-null: bool    |              |
| has_internet           | 7049 non-null: bool    |              |
| has_phone_and_internet | 7049 non-null: bool    |              |
| partner_depenents      | 7049 non-null: int64   |              |
| start_date             | 7049 non-null: object  |              |
| avg_monthly_charges    | 7049 non-null: object  |              |
| matches_orig           | 7049 non-null: object  |              |
| phone description      | 7049 non-null: object  |              |
| internet_desciption    | 7049 non-null: object  |              |
| contract_description   | 7049 non-null: object  |              |

