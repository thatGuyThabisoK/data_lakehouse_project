#Mappings for column name changes

product_catagories = {
    "ID":"Product_id",
    "CAT":"Category",
    "SUBCAT":"Subcategory",
    "MAINTENANCE":"Maintenance"
}

customer_location = {
    "CID":"Customer_id",
    "CNTRY":"Country"
}

customer_demographic_info = {
    "CID":"Customer_id",
    "B DATE":"Birth_date",
    "GEN":"Gender"
}

customer_information = {
    "cst_id":"Customer_id",
    "cst_key":"Customer_key",
    "cst_firstname":"First_name",
    "cst_lastname":"Last_name",
    "cst_marital_status":"Marital_status",
    "cst_gndr":"Gender",
    "cst_create_date":"Create_date"
}

product_information = {
    "prd_id":"Product_id",
    "prd_key":"Product_key",
    "prd_nm":"Name",
    "prd_cost":"Cost",
    "prd_line":"Product_line",
    "prd_start_dt":"Start_date",
    "prd_end_dt":"End_date"
}

sales_details = {
    "sls_ord_num":"Order_number",
    "sls_prd_key":"Product_key",
    "sale_cust_id":"Customer_id",
    "sls_order_dt":"Order_date",
    "sls_ship_dt":"Ship_date",
    "sls_due_dt":"Due_date",
    "sls_sales":"Sales",
    "sls_quantity":"Quantity",
    "sls_price":"Price"
}

#Table Names in the Silver Layer

table_names={
    "cust_az12":"customer_demographic_info",
    "cust_info":"customer_information",
    "loc_a101":"customer_Location",
    "prd_info":"product_information",
    "px_cat_g1v2":"product_catagories",
    "sales_details":"sales_details"
}
   


