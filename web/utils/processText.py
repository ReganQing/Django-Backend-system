import re
import Coversation
# text = "存储零件信息，名字是湿度传感器，id是211111，单价是45元，库存量是3675，计量单位是件，存储地址为仓库A"


name_pattern = r"名字是(\w+)"
id_pattern = r"id是(\d+)"
price_pattern = r"单价是(\d+)元"
quantity_pattern = r"库存量是(\d+)"
unit_pattern = r"计量单位是(\w+)"
address_pattern = r"存储地址为(\w+)"

name_match = re.search(name_pattern, text)
id_match = re.search(id_pattern, text)
price_match = re.search(price_pattern, text)
quantity_match = re.search(quantity_pattern, text)
unit_match = re.search(unit_pattern, text)
address_match = re.search(address_pattern, text)

if name_match:
    name = name_match.group(1)
    print("Name:", name)

if id_match:
    part_id = id_match.group(1)
    print("ID:", part_id)

if price_match:
    price = price_match.group(1)
    print("Price:", price)

if quantity_match:
    quantity = quantity_match.group(1)
    print("Quantity:", quantity)

if unit_match:
    unit = unit_match.group(1)
    print("Unit:", unit)

if address_match:
    address = address_match.group(1)
    print("Address:", address)
