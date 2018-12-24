def duty_free(price, discount, holiday_cost):
  after_discount = (price*discount)/100
  total_bottles = holiday_cost/after_discount
  return int(total_bottles)
