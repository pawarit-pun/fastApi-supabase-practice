import base64
import json

from fastapi import FastAPI , HTTPException, Request
from configs.config import db_env
from db.supabase import supabase

app = FastAPI()


@app.get("/products")
def get_products():
    
    res = supabase.table("products").select("*").execute()
    return res.data

#Lots + Sales

@app.get("/data/datasv1")
def get_datas():
    
    lots = supabase.table("inventory_lots").select("lot_id, product_id, received_date, expiration_date, initial_quantity, " \
    "current_quantity, unit_cost, location_aisle, location_shelf, current_selling_price").execute()

    sales_history = supabase.table("sales_history").select("*").execute()

    #need to modify (reference_date)
    average_daily_sales = supabase.table("daily_sales_velocity").select("product_id, avg_daily_sales_7d, avg_daily_sales_30d, avg_daily_sales_regular_30d, reference_date").execute()
    return {"inventory_lots": lots.data, "sales_history": sales_history.data, "average_dialy_sales": average_daily_sales}