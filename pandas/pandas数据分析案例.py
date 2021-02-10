# Author: Frank
# CNDate: 2021/2/10
# Python: 3.8.5
import numpy as np
import pandas as pd

df = pd.read_csv('./2020.csv')

# 1.删除重复数据
df.drop_duplicates(inplace=True)

# 2.过滤非数据分析的岗位
cond = df['positionName'].str.contains("数据分析")
df = df[cond]

# 3.处理薪水过程25k-35k
df['salary'] = df.salary.str.lower()  # series
df['salary'] = df['salary'].str.extract(r'(\d+)[k]-(\d+)[k]').applymap(lambda x: int(x)).mean(axis=1)

# 4.查找重要技能
df['job_detail'] = df['job_detail'].str.lower()
df['sql'] = df['job_detail'].map(lambda x: 1 if 'sql' in x else 0)
df['python'] = df['job_detail'].map(lambda x: 1 if 'python' in x else 0)
df['tableau'] = df['job_detail'].map(lambda x: 1 if 'tableau' in x else 0)
df['excel'] = df['job_detail'].map(lambda x: 1 if 'excel' in x else 0)
df['SPSS/SAS'] = df['job_detail'].map(lambda x: 1 if 'spss/sas' in x else 0)

print(df.iloc[:5, -5:])


# 5.精细化招聘行业
def clean_industry(industry):
    industry = industry.split(',')
    if len(industry[-1]) >= 1:
        return industry[-1]
    else:
        return industry[0]


print(df.industryField)
df.industryField = df.industryField.map(clean_industry)
print(df.industryField)
