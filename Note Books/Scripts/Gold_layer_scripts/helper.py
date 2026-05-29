def displayTables(tables,sparkSessionObj, dir):
    for table in tables:
        print(f"Printing table {table}: \n")
        sparkSessionObj.table(f"{dir}.{table}").head(5)
        print("\n")