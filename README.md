# **Intro to Programming - Final Assignment**
#### **By Michael Lindemulder & Anna Draft**

### **Step 1 - The Data!**
We investigated the following two data sets on Chicago Public Schools for 2017-2018:

  1) SQRP Ratings and Accountability Status 2017-2018 ("acct.xls")
  2) Demographics School Year 2017-2018 ("demo.xls")

  https://cps.edu/SchoolData/Pages/SchoolData.aspx

Our objective in joining these two data sets is to look at correlations between School Quality Rating Policy (SQRP) Scores (found in "acct.xls") and school demographics (found in "demo.xls") within Chicago Public Elementary, High School and Option schools. Both the these files, as well as cleaned files can be found in our repository.

The steps for cleaning and joining the data are listed below in **Step 2**.

**Step 3** lists actions taken to compare and analyze the data (i.e., regressions, plots and graphs) from the newly joined data on Elementary Schools, High Schools and Option Schools.

A more detailed overview of our objective, as well as all findings and analysis can be found on our website: **"XXXXXX"**

For code used in steps 2 & 3, please refer to **"Final Code.py"**.


### **Step 2 - Clean, Join & Save New Files:**

#### **1) Clean Data**
* In "acct.xls", some Elementary Schools, High Schools and Option schools were missing SQRP data. For each of the Sheets listed below, we dropped schools missing SQRP data.

    * Elementary Schools ("Elem Schools (grds PreK-8 only)")

    * High Schools ("High Schools (grds 9-12 only)")

    * Option Schools ("Option Schools")

* In "demo.xls", Sheet Name "Schools", some Elementary Schools, High Schools & Option Schools were missing data under the column "Bilingual, Bilingual %". This is because these schools do not offer Bilingual programs. For each school without a bilingual program, we filled in missing data (NaN) with 0.

#### **2) Join and save cleaned data as new files:**
* Once data was cleaned, we joined and saved the data as the following three, new files:

    * "joinedelem.xls"

    * "joinedhigh.xls"

    * "joinedoption.xls"


### **Step 3 - The Fun Part!!**
*All results and analysis from Step 3 can be found on our website "XXXX"*
#### **1) Regression Analysis**

From our newly saved files for Elementary Schools, High Schools & Option Schools, we ran regressions to test how schools with the following programs - **"Bilingual", "Special Education (SpED)", "Free/Reduced Lunch"** - may or may not be correlated with our dependent variable **"SQRP Total Points Earned".**

#### **2)   **
