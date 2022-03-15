```python
ex = "accgtacgtcgatagggcagggggctag"
```


```python
def suffixtable (t:str):
   """
   <<IN>> 
   >>> t = text
   <<OUT>>
   >>> List of Tuples (suffix, offset)
   """
   
   suffixtable = []
   for i in range(len(t)):
      suffix = t[i:]
      offset = i
      suffixtable.append((suffix,offset))
   return suffixtable

st = suffixtable (ex)
st.sort()
```


```python
li =[]
for x in st:
    string = x[0]
    li.append(string)
```


```python
ind = []
for x in st:
    ind.append(x[1])
```


```python
import pandas as pd
```


```python
df = pd.DataFrame(li,index=ind)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>accgtacgtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>5</th>
      <td>acgtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>26</th>
      <td>ag</td>
    </tr>
    <tr>
      <th>13</th>
      <td>agggcagggggctag</td>
    </tr>
    <tr>
      <th>18</th>
      <td>agggggctag</td>
    </tr>
    <tr>
      <th>11</th>
      <td>atagggcagggggctag</td>
    </tr>
    <tr>
      <th>17</th>
      <td>cagggggctag</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ccgtacgtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>9</th>
      <td>cgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>2</th>
      <td>cgtacgtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>6</th>
      <td>cgtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>24</th>
      <td>ctag</td>
    </tr>
    <tr>
      <th>27</th>
      <td>g</td>
    </tr>
    <tr>
      <th>10</th>
      <td>gatagggcagggggctag</td>
    </tr>
    <tr>
      <th>16</th>
      <td>gcagggggctag</td>
    </tr>
    <tr>
      <th>23</th>
      <td>gctag</td>
    </tr>
    <tr>
      <th>15</th>
      <td>ggcagggggctag</td>
    </tr>
    <tr>
      <th>22</th>
      <td>ggctag</td>
    </tr>
    <tr>
      <th>14</th>
      <td>gggcagggggctag</td>
    </tr>
    <tr>
      <th>21</th>
      <td>gggctag</td>
    </tr>
    <tr>
      <th>20</th>
      <td>ggggctag</td>
    </tr>
    <tr>
      <th>19</th>
      <td>gggggctag</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gtacgtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>7</th>
      <td>gtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tacgtcgatagggcagggggctag</td>
    </tr>
    <tr>
      <th>25</th>
      <td>tag</td>
    </tr>
    <tr>
      <th>12</th>
      <td>tagggcagggggctag</td>
    </tr>
    <tr>
      <th>8</th>
      <td>tcgatagggcagggggctag</td>
    </tr>
  </tbody>
</table>
</div>


