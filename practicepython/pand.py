import pandas as pd
employee_df=pd.read_csv(r'C:\Users\Shashi Kumar\PycharmProjects\pythonProject\practicepython\employee.csv')
#print(employee_df)
#print(employee_df.head(8))
#print(employee_df.columns)
res=employee_df[employee_df['First Name']=='Cynthia']
print(res[['First Name','Last Name']])
for i,v in res.iterrows():
    print(v['Last Name'])
Sub=employee_df[employee_df['First Name'].str[:1]=='J']
print(Sub)
empsrt=employee_df.sort_values(['Emp ID'], ascending=True)
print(empsrt)
Email=employee_df['Middle Initial'].notnull()
print(Email)
Email=employee_df['Middle Initial'].isnull()
print(employee_df.isnull())
print(employee_df.isna().sum())
print('Substring', employee_df[employee_df['First Name'].str[2]=='e'])
print(employee_df.agg({'Salary':['max','min','sum','mean']}))