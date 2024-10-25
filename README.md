# Student Performance Predictive Analysis

## Intro/Project Components
The purpose of this project is to provide users with an interactive app to determine which key factors influence a students academic performance (GPA). We wanted to do this in order to help parents/students see what is contributing positively or negatively to the student’s academic performance, as well as to see what could be changed in their academic and home life in order to improve academic performance. The components of our project included building the model using machine learning, outputting the model using flask, then analyzing the results through our process and with visualizations. 

## Data Processing/Cleaning
In order to optimize our original dataset, we had to do a few things with it. We began by deciding if there were any superfluous columns we did not need, like Student ID. Then, we transformed any numerical values that referenced an outside key into string values, so that any output would show our specific components like race, parental support, or absences as so, not as numbers.

## Model
random forest vs linear regression? explain model and key influence factors (absences, tutoring, and parental support)

## Visualizations
After the data cleansing process, our high school GPA dataset was visualized using Tableau in order to examine the data and any trends more closely. The most interesting relationship seemed to exist between the number of absences and GPA, meaning the higher the number of absences, the lower the average GPA. When looking through the remaining dataset analyses (amount of study time, participation in sports, volunteer activity, etc.) it indicated that Caucasians made up the bulk of each attribute tracked (i.e. grades), reflecting the fact that they made up bulk of ethnicities tracked in the study results but otherwise not clearly articulating any contributing factors to GPA beyond absence vs. GPA.

## Challenges
The main challenge with out project was the limitations of our dataset. For the purposes of our educational class project it sufficed, but in order for this app to be really helpful to all students, the dataset would need to be much more extensive. The current dataset only includes 2,392 high school students who are primarily white, black, and Asian, which limits the utility of our model if it were to be utilized outside the reaches of this class project. 

## Source
https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset

