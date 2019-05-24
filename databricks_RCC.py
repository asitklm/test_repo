####added comment line#####

from datetime import datetime
dbutils.fs.ls("/mnt/FIONA/RDS/Ahold/Item_Cost/Ad_Wk")
#dbutils.fs.mount("/mnt/FIONA/RDS/Ahold/Item_Cost/Ad_Wk/20190131_stsh_cost_ad1.txt", "/mnt/")
now =datetime.now()

file_ =  open("/dbfs/mnt/FIONA/RDS/Ahold/Item_Cost/Ad_Wk/20190131_stsh_cost_ad1.txt", 'r')

counter = 0
for _ in file_:
    counter = counter + 1
    
end = datetime.now()
print("counter:")
print(counter)
print(str(end-now))

file.close()
