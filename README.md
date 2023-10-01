# Sentiment-Analysis
This is a django project, incorporating a machine learning models of sentiment analysis inside. The aim of the project is to be able to detect user's sentiment inside the review's text. Human's emotion can be complicated. Myself, for example, cannot put a very bad words in any review no matter how bad I feel, so I would use words such as 'it can be improved by ...' or 'the package can be protected more with bubble wrap', rather than 'the service was terrible'. This is where sentiment analysis can be beneficial, to detect the hidden emotion under the text. Some platforms may use ratings to get ultimate user's experience score, while for some people, rating does not always linear to their actual experience. As more customers express their thoughts about things they bought more openly than ever before, sentiment analysis can become a powerful tool to maintain and acknowledge online conversation. By doing this, we can tailor our products and services to meet the customer's need thus increasing the success rate.

# Technologies used
Python (Pandas, Numpy, Matplotlib, Seaborn, Pickle, sklearn), Google Colab, Django

## Table of Content:
### Data Collection:
  - Sources: https://data.world/datafiniti/consumer-reviews-of-amazon-products
  - Contains reviewText, reviewTime, and overall rating
### Data Cleaning:
  - Removing null value
  - Using vectorizer to transform text data into feature index in the matrix
### Data Modelling:
  - Classification model fitted: Decision Tree Classifier, Random Forest Classifier, Logistic Regressor
  - The best models will be tuned with the estimator hyperparameters
### Webpage by Django:
  - The salary prediction will be put in a webpage by django project
  - Data visualization by matplotlib is also shown

# Ilustration of Web App:
![alt text](https://github.com/cindysuyitno/Sentiment-Analysis/blob/main/sentiment_analysis2.png)
![alt text](https://github.com/cindysuyitno/Sentiment-Analysis/blob/main/sentiment_analysis1.png)
![alt text](https://github.com/cindysuyitno/Sentiment-Analysis/blob/main/sentiment_analysis3.png)

# Comments and Suggestion from Author
The final model use LogisticRegression (C=1, multi_class='multinomial') with the final accuracy of 69.2%. The result is great, now we can detect the final sentiment score of a review text, whether it is neutral, positive, or negative. We can also see the percentage of the score (if user is having both negative and positive experience, it should be seen on both graphs). However, since this model is trained on only one company dataset, it may not be suitable for other company that has different customer behaviour. The model should be incorporated into other company dataset to enrich the data collections. Other kind of classification models can also be used in order to find the most suitable and highest accuracy.
