# validate for requirements
def validate_string(str):
  if len(str) == 0 or str is None:
    return "invalid"
  elif str.startswith('B') and str[0].islower():
    return "invalid"
  elif str.startswith('B') == False:
    return "invalid"
  elif str.find('P', 5) != -1 and str[str.find('P', 4)].islower(): 
    return "invalid"
  elif str.find('P', 5) == -1:
    return "invalid"
  elif str.find('Q', 8) != -1 and str[str.find('Q', 8)].islower():
    return "invalid"
  elif str.find('Q', 8) == -1:
    return "invalid"
  elif str.find('D', 11) != -1 and str[str.find('D', 11)].islower():
    return "invalid"
  elif str.find('D', 11) == -1: 
    return "invalid"
  else:
    return "First Check Valid"

# get batch id: result should be similar to this ['1234', 'ABQ50D20230908B5678PXYQ30D20230909']
def get_batch_id(str):
  if len(str) != 0 and str.startswith('B') and str[0].isupper():
    b_prefix = str.split('B', 1)
    if b_prefix[1].find('P', 4) and b_prefix[1][b_prefix[1].find('P', 4)].isupper():
      b_prefix_result = b_prefix[1].split('P', 1) 
      if b_prefix_result[0].isdigit(): 
        return b_prefix_result 
      else:
        return 'invalid'
    else:
      return 'invalid'
  else:
    return 'invalid'

# get product code: result should be similar to this ['AB', '50D20230908B5678PXYQ30D20230909']
def get_product_code(str):
  if str.find('Q', 2) != -1 and str[str.find('Q', 2)].isupper():
        product_code_result = str.split('Q', 1)
        if product_code_result[0].upper() and product_code_result[0].isalpha() and len(product_code_result[0]) == 2:
          return product_code_result
        else:
          return "invalid"
  else:
    return "invalid"

# get quantity: result should be similar to this ['50', '20230908B5678PXYQ30D20230909']
def get_quantity(str):
  quantity_result = str.split('D', 1)
  if len(quantity_result[0]) - len(quantity_result[0].lstrip('0')) > 0:
    quantity_result[0] = quantity_result[0].lstrip('0')
    return quantity_result
  else:
    return quantity_result

# get date: result should be similar to this 20230908B5678PXYQ30D20230909
def get_date(str):
  if str.find('B', 8) != -1 and len(str[0:8]) == 8: 
    date_result = str.split('B', 8) 
    if date_result[0].isdigit(): 
      year_range = int(date_result[0][:4]) in range(2000, 2099)
      month_range = int(date_result[0][4:6]) in range(1, 12)
      date_range = int(date_result[0][6:8]) in range(1, 31)
      if year_range and month_range and date_range: 
        return str
      else:
        return 'invalid'
    else:
      return 'invalid'
  elif str.find('2', 0) != -1: 
    if str.isdigit(): 
      year_range = int(str[:4]) in range(2000, 2099) 
      month_range = int(str[4:6]) in range(1, 12) 
      date_range = int(str[6:8]) in range(1, 31) 
      if year_range and month_range and date_range: 
        return str
      else:
        return 'invalid'
    else:
      return 'invalid'
  else:
    return 'invalid'

# check if results are valid and assign
def assign_vals(s):
  if validate_string(s) == "First Check Valid": 
    batch_dict = {}
    new_str = ''
    if get_batch_id(s) != "invalid": 
        batch_id_result = get_batch_id(s)
    else:
      return "invalid"

    if get_product_code(batch_id_result[1]) != "invalid": 
      product_code_result = get_product_code(batch_id_result[1])
    else:
      return "invalid"

    if get_quantity(product_code_result[1]) != "invalid": 
      quantity_result = get_quantity(product_code_result[1])
    else:
      return "invalid"

    if get_date(quantity_result[1]) != "invalid": 
      date_result = get_date(quantity_result[1])
    else:
      return "invalid"

    batch_dict['Batch ID'] = batch_id_result[0]
    batch_dict['Product Code'] = product_code_result[0]
    batch_dict['Quantity'] = int(quantity_result[0])

    if len(date_result) > 8:
      batch_dict['Date'] = date_result[:8] 
      new_str = date_result[8:]
      return [batch_dict, new_str]
    else:
      batch_dict['Date'] = date_result
      return [batch_dict]
  else:
    return "invalid"

# validate and extract the log
def validate_and_extract_log(s):
  assign_vals_result = assign_vals(s) 
  if assign_vals_result == "invalid": 
    return assign_vals_result
  elif assign_vals_result != "invalid" and len(assign_vals_result) == 1:
    batches_info = []
    batches_info.append(assign_vals_result[0])
    return batches_info
  else: 
    batches_info = []
    batches_info.append(assign_vals_result[0])
    assign_vals_result = assign_vals(assign_vals_result[1])
    batches_info.append(assign_vals_result[0])
    return batches_info
  
# print(validate_and_extract_log("B1234PABQ50D20230908"))
# print(validate_and_extract_log("b1234PABQ50D20230908"))
# print(validate_and_extract_log("B1234P3BQ50D20230908"))
# print(validate_and_extract_log("B1234PABQ50D2023A908"))
# print(validate_and_extract_log("B1234PABQ50D20230908B5678PXYQ30D20230909"))
# print(validate_and_extract_log("B1234PABQ0050D20230908B5678PXYQ0030D20230909"))
