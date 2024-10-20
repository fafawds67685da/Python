import pandas as p
a={"sunjects":["Maths","CTS"],
   "dev":[5,10],
   "yash":[10,20]}
b=p.DataFrame(a)
b.to_csv(r"C:/Users/Hp/OneDrive/Desktop/abc.csv",index=False)
