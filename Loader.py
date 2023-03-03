import mysql.connector
import yaml

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Master@12345",
  database="eficaz_target"
)

mycursor = mydb.cursor() 

property_name = []
property_value = []
with open('eficazloader-deployment (1).yaml') as file:
    try:
        databaseConfig = yaml.safe_load(file)   
        env_variables =  databaseConfig['spec']['template']['spec']['containers'][0]['env']
        for key in env_variables:
          new_name = key['name']  
          property_name.append(new_name)
          # print(new_name)
          new_value = key['value']
          if(new_value == None):
            new_value = " "
          property_value.append(new_value)
          # print(new_value )
          # print("insert into eficaz_target.eficazproperties (id,created_by,created_on,datatype,name,type,updated_by,updated_on,value) values(21,'Admin','2023-02-06','1','"+ new_name +"','Parser','','','" + new_value+"')")
    except yaml.YAMLError as err:
        print(err)


# print(len(property_name))
# print(property_name)
# print(len(property_value))
# print(property_value)

# column_names = [name + ' VARCHAR(255)' for name in property_name]

# id = ['ID INT AUTO_INCREMENT primary key NOT NULL ']
# date = ['CREATED_AT DATE DEFAULT (CURDATE()) ']
# add_id_date = id + date

# columns_property = add_id_date + column_names
# print(columns_property)

# create_table = "CREATE TABLE loader_properties ({})".format(
#    " , ".join(columns_property)
# )

# mycursor.execute(create_table)

# sql = "INSERT INTO loader_properties ({}) VALUES ({})".format(
#     ", ".join(property_name),
#     ", ".join(["%s"] * len(property_value))
# )
# mycursor.execute(sql, property_value)

query = "INSERT INTO eficaz.properties (created_by,created_on, datatype, name, type, value) VALUES ('admin','20-02-2023','String', %s, 'Loader', %s)"
values = [(c, o) for c, o in zip(property_name, property_value)]

mycursor.executemany(query, values)
mydb.commit()

print("",mycursor.rowcount, "record inserted.")

mycursor.close()
