def deleteAll(myCatalog, mySchema, sparkObj):
    sparkObj.sql(f"USE CATALOG {myCatalog};")
    for table in sparkObj.catalog.listTables(mySchema):
        sparkObj.sql(f"DROP TABLE IF EXISTS {mySchema}.{table.name};")