import pandas as ps
import matplotlib.pyplot as plt

data = ps.read_csv('USvideos.csv', sep=',')

data['publish_time'] = ps.to_datetime(data['publish_time'])
data.insert(4, 'publish_date', ps.to_datetime(data['publish_time'].dt.date))
data.insert(5, 'publish_time_specific', data['publish_time'].dt.time)

data.index = data['publish_date']
data = data.sort_values('publish_date')
print(data.info())
#print(data.nunique())
#16 cat_id, publish_time, views


selected_date = data['publish_date'][1]
#print(data.loc[selected_date])
c_data = data[['publish_date', 'publish_time_specific', 'views', 'category_id']]
c_data = c_data.sort_values('category_id')
c_data = c_data.head(n=1500)

print(c_data)

c_data.index = c_data['category_id']
c_data['views'].plot()
#plt.legend()
plt.show()
