import datetime
from typing import List, Optional
from pydantic import BaseModel
#typical data format
order_json = {

    'item_id' :'123',
    'created_date':'2001-11-24 12:22',
    'pages_visited' : [1,2,'3'],
    'price':17.22
}

#how to create a class order
class Order(BaseModel):
    item_id:int
    created_date:Optional[datetime.datetime]
    pages_visited : List[int]
    price:float

o = Order(**order_json)
print(o)

#use pydantic that helps us create classesa