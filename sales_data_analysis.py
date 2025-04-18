import pymysql
import matplotlib.pyplot as plt

db=pymysql.connect(host='localhost',user='root',password='1234',database='ai_resume')
mycursor=db.cursor()
print('successfully')

query='''select customer_id, sum(quantity*price) as total_price from sales_data group by customer_id'''
mycursor.execute(query)
output=mycursor.fetchall()

customer_ids = []
total_prices = []

for i in output:
    print(i)
    customer_ids.append(i[0])
    total_prices.append(i[1])

plt.bar(customer_ids,total_prices,color='skyblue',label=True)
plt.xlabel('Customer id')
plt.ylabel('price ')
plt.title('Total Sales per Customer')
plt.tight_layout()
plt.show()
