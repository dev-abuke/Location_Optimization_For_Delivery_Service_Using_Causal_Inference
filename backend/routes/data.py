from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()

@router.get("/data/completed-orders")
def get_completed_orders():
    file_path = os.path.join(os.path.dirname(__file__), '../../data/completed_orders.csv')
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")

@router.get("/data/driver-locations")
def get_driver_locations():
    file_path = os.path.join(os.path.dirname(__file__), '../../data/driver_locations_during_request.csv')
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")
