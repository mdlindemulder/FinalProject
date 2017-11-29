# **Intro to Programming - Final Assignment**
#### **By Michael Lindemulder & Anna Draft**

### **Step 1 - The Data!**
We investigated the following two data sets on Chicago Public Schools for 2017-2018:

  1) SQRP Ratings and Accountability Status 2017-2018 ("acct.xls")
  2) Demographics School Year 2017-2018 ("demo.xls")

  https://cps.edu/SchoolData/Pages/SchoolData.aspx

Our objective in joining these two data sets is to look at correlations between School Quality Rating Policy (SQRP) Scores (found in "acct.xls") and school demographics (found in "demo.xls") within Chicago Public Elementary, High School and Option schools.

The steps for cleaning and joining the data are listed below in **Step 2**.

**Steps 3 -- XXXX** list steps taken to run regressions, plot and graph the newly joined data on Elementary Schools, High Schools and Option Schools.

All findings and analysis of the joined data can be found on our website **"XXXXXX"**

For steps 2 --- XXXX, please refer to **"Final Code.py"** for code.


### **Step 2 - Clean, Join & Save New Files:**

#### **1) Clean Data**
* In "acct.xls", some Elementary, High School and Option schools were missing SQRP data. For each of the Sheets listed below, we dropped schools missing SQRP data.

      + Drop schools missing SQRP data:

          - i) Elementary Schools ("Elem Schools (grds PreK-8 only)")

          - ii) High Schools ("High Schools (grds 9-12 only)")

          - iii) Option Schools ("Option Schools")

* In "demo.xls", Sheet Name "Schools", some Elementary, High School & Option Schools were missing data under the column "Bilingual - Bilingual %". This is because these schools do not offer Bilingual programs. For each school without a bilingual program, fill missing data with 0.

#### **2) Join and save cleaned data as new files:**
Once data was cleaned, we joined and saved the data as the following three new files:

a) "joinedelem.xls"
b) "joinedhigh.xls"
c) "joinedoption.xls"


### **Step 3 - The Fun Part!!**

#### **1) Run Regressions...**

For Elementary Schools, High Schools & Option Schools from newly saved files. Test independent variables that may or may not be correlated with changes in our dependent variable "SQRP Total Points Earned".

#### **2)   **
