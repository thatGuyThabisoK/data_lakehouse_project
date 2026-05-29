def deleteAll(myCatalog, mySchema, sparkSessionObj):
    sparkSessionObj.sql(f"USE CATALOG {myCatalog};")
    for table in sparkSessionObj.catalog.listTables(mySchema):
        sparkSessionObj.sql(f"DROP TABLE IF EXISTS {mySchema}.{table.name};")
