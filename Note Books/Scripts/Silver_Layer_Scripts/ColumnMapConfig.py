#Mappings for column name changes

customer_location = {
    "CID":"Customer_id",
    "CNTRY":"Country"
}

customer_demographic_info = {
    "CID":"Customer_id",
    "B DATE":"Birth_Date",
    "GEN":"Gender"
}

customer_information = {
    "cst_id":"Customer_id",
    "cst_key":"Customer_key",
    "cst_firstname":"First_name",
    "cst_lastname":"Last_name",
    "cst_marital_status":"Marital_status",
    "cst_gndr":"Gender"
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

product_catagories = {
    "CAT":"Category",
    "SUBCAT":"Subcategory",
    "MAINTENANCE":"Maintenance"
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
    "cust_az12_csv":"Customer_demographic_info",
    "cust_info_csv":"Customer_information",
    "loc_a101_csv":"Customer_Location",
    "prd_info_csv":"Product_information",
    "px_cat_g1v2_csv":"Product_catagories",
    "sales_details_csv":"Sales_details"
}
   


