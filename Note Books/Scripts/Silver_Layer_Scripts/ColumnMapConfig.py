#Mappings for column name changes

Location_table = {
    "CID":"Customer id",
    "CNTRY":"Country"
}

Customer_demographic_info_table = {
    "CID":"Customer id",
    "B DATE":"Birth Date",
    "GEN":"Gender"
}

Customer_info_table = {
    "cst_id":"Customer id",
    "cst_key":"Customer key",
    "cst_firstname":"First name",
    "cst_lastname":"Last name",
    "cst_marital_status":"Marital status",
    "cst_gndr":"Gender"
}

Product_table = {
    "prd_id":"Product id",
    "prd_key":"Product key",
    "prd_nm":"Name",
    "prd_cost":"Cost",
    "prd_line":"Product line",
    "prd_start_dt":"Start date",
    "prd_end_dt":"End date"
}

Product_catagories_table = {
    "CAT":"Category",
    "SUBCAT":"Subcategory",
    "MAINTENANCE":"Maintenance"
}

Sales_details_table = {
    "sls_ord_num":"Order number",
    "sls_prd_key":"Product key",
    "sale_cust_id":"Customer id",
    "sls_order_dt":"Order date",
    "sls_ship_dt":"Ship date",
    "sls_due_dt":"Due date",
    "sls_sales":"Sales",
    "sls_quantity":"Quantity",
    "sls_price":"Price"
}

#Table Names in the Silver Layer

Table_names={
    "cust_az12_csv":"Customer demographic info",
    "cust_info_csv":"Customer information",
    "loc_a101_csv":"Customer Location",
    "prd_info_csv":"Product information",
    "px_cat_g1v2_csv":"Product catagories",
    "sales_details_csv":"Sales details"
}
   


