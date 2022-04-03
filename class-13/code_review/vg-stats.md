# Video game statistics

```python

na_median = df['NA_Sales'].median()
data_with_median = df[df['NA_Sales']==na_median]
mid = len(data_with_median) // 2
list(data_with_median[mid-5:mid+5])
```