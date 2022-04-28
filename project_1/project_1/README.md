# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: SAT & ACT Analysis

In this project, my objective is to analyse and find trends in the SAT and ACT participation rates and subject scores in 2017 and 2018. I am to assume the role of a College Board employee, and will be part of a team that tracks statewide participation and provide recommendations on where money can be best spent to improve SAT participation rates.

The datasets chosen for this project are:
* act_2017.csv
* act_2018.csv
* sat_2017.csv
* sat_2018.csv
<hr>

## Executive Summary
Based on the information gathered from the above datasets, high participation rates for SAT always results in lower participation rates in the other, and vice-versa. This is most prominently observed in states where either of these tests are mandated. 

There appears to be a weak negative correlation between scores of similar subjects (e.g. ACT Math vs SAT Math), and the only strong positive correlation identified in the data visuals are the total scores between 2017 and 2018 respective to the tests (SAT total mean score 2017 vs SAT total mean score 2018).

For ACT-mandated states, it is unlikely that efforts spent there will yield any satisfactory results. Resources are recommended to be better focused on states such as California, Georgia or Oregon, where SAT and ACT participation rates remain low and show potential for substantial growth.

Another recommendation would be to offer SAT tests at no cost to students, a move administered by [Delaware to promote a school culture to encourage more students to pursue education after high school]("https://delawarepta.org/free-sat-registration-now-open-for-public-school-juniors/") - the results of this funding speaks for itself in the datasets above with 100% participate rate in 2017 and 2018 from said state, 7 years after it kickstarted.

<hr>

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**state_sat_2017**<br>**state_act_2017**|*object*|ACT/SAT|The state the data is based on for the ACT and SAT tests taken in 2017.|
|**state_sat_2018**<br>**state_act_2018**|*object*|ACT/SAT|The state the data is based on for the ACT and SAT tests taken in 2017.|
|**sat_participation_2017**<br>**act_participation_2017**|*float*|ACT/SAT|The participation rates for all ACT and SAT tests in 2017.
|**sat_ebrw_2017**<br>**sat_ebrw_2018**|*integer*|SAT|The average score of all the tests taken for Evidence-Based Reading and Writing in 2017/2018.| 
|**sat_math_2017**<br>**sat_math_2018**|*integer*|SAT|The average score of all the tests taken for Math in 2017/2018.
|**sat_total_2017**<br>**sat_total_2018**|*integer*|SAT|The total average score of the Evidence-Based Reading and Writing and Math sections in 2017/2018.| 
|**act_english_2017**|*float*|ACT|The average score of all the tests taken for English in 2017.|
|**act_math_2017**|*float*|ACT|The average score of all the tests taken for Math in 2017.| 
|**act_reading_2017**|*float*|ACT|The average score of all the tests taken for Reading in 2017.| 
|**act_science_2017**|*float*|ACT|The average score of all the tests taken for Science in 2017.| 
|**act_composite_2017**|*float*|ACT|The total average score of the English, Math, Reading and Science sections taken in 2017.| 
<hr>