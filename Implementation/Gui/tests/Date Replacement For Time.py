def check_date():
    #get date stored as SalesDate
    date_stored = get_date_stored()
    
    current_date = datetime.date.today()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day
    
    if current_day < 8:
        current_month = current_date.month
        last_month = current_month - 1
        next_month = current_month + 1
        no_days_last_month = calendar.monthrange(current_date.year, last_month)[1]
        days_to_minus = 7 - current_day
        previous_month = datetime.date(current_year, last_month, no_days_last_month)
        new_day = previous_month.day - days_to_minus
        new_date = datetime.date(current_year, last_month, new_day)

    else:
        new_date = datetime.date(current_year, current_month, (current_day - 7))

    new_date = new_date.strftime("%d-%m-%Y")
    print(new_date)
    
    if not date_stored:
        update_date(current_date)

    elif date_stored == new_date:
        #IF A WEEK HAS PASSED ADD WEEKLY SALES TO TOTAL SALES AND CHANGE WEEKLY SALES TO 0. STORE CURRENT DATE AS SALES DATE
        product_id_list = get_all_product_id()
        for product_id in product_id_list:
            total_sales = get_total_sales(product_id)
            for item in total_sales:
                total_sales_list.append(item)
            weekly_sales = get_current_week_sales(product_id)
            total_sales_list.append(weekly_sales)
            update_total_sales(total_sales_list, product_id)
