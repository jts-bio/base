# PANDAS


```python
import pandas as pd
import yaml
from yaml import loader, Loader
```


```python
empl_doc = open("employees.yaml","r")
data = yaml.load(empl_doc,Loader=Loader)
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-2-605d56de3c3a> in <module>
    ----> 1 empl_doc = open("employees.yaml","r")
          2 data = yaml.load(empl_doc,Loader=Loader)


    FileNotFoundError: [Errno 2] No such file or directory: 'employees.yaml'



```python
df = pd.DataFrame(data).T
df
```


```python
def getAllShifts ():
   out = []
   for tf in df.trained_for:
      for shift in tf:
         if shift not in out:
            out.append (shift)
   print ("ALL SHIFTS:")
   return out

shifts = getAllShifts()
print (len(shifts),":" ,shifts)
```


```python
mi = ["MI" in df['trained_for'][x] for x in range(len(df['trained_for']))]
df['mi'] = mi
print("TRAINED FOR MI")
df[df['mi']]
```

### Employee Training Report


```python
def empl_trained_for (empl:str,shift:str) -> bool:
   """ [function]
   CHECKS IF EMPLOYEE IS TRAINED FOR SHIFT

        Args:
            empl (str): employee id by name
            shift (str): shift id by name
        Returns:
            >>> bool: True if employee can work shift
                      False if employee cannot
   """
   a = shift in df.loc[empl]['trained_for']
   return a

```


```python
def empl_training_report (empl) :
   dic = {}
   for s in getAllShifts():
      result = empl_trained_for(empl, s)
      dic.update({s : result})
   ##--[ Calc % of Shifts Can Work ]--##
   count = 0
   for val in dic.values():
      if val == True:
         count += 1
   percent = round(count/len(dic)*100,0)
   ##--[ Display as DF ]--##   
   df = pd.DataFrame(dic.values(),columns =[empl],index=dic.keys())
   print (percent,"%")   
   return df
```


```python
empl_training_report ("Josh")
```

# DATETIME


```python
import datetime as dt
import timedelta
```


```python
d1 = dt.date(2022,3,8)
days = [d1 + dt.timedelta(days=x) for x in range(100)]
fmt = []
for x in days:
   i = x.ctime()
   fmt.append(str(i)[0:10])
print(fmt)
```


```python
empl_list = list(data.keys())
empl_list
```


```python
df_sched = pd.DataFrame(columns=days,index=empl_list)
df_sched
```


```python
weekdaydata = [x.weekday() for x in df_sched.columns]
weekdaydata = pd.Series(weekdaydata, index=list(df_sched))
weekdaydata
```


```python
def generate_weeknumber (list_of_dates):
   count = 0
   weekno = []
   for x in list_of_dates:
      if x == 0:
         count +=1
      weekno.append(count)
   weekno = pd.Series(weekno,index=list(df_sched))

   return weekno
```


```python
generate_weeknumber(weekdaydata)
```
