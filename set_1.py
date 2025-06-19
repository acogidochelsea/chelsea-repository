def savings(gross_pay, tax_rate, expenses):
    x = tax_rate*gross_pay
    take_home = int(gross_pay - x - expenses)
    return take_home

def material_waste(total_material, material_units, num_jobs, job_consumption):
    x = num_jobs*job_consumption
    y = str(total_material - x) + str(material_units)
    return y

def interest(principal, rate, periods):
    x = principal*(rate*periods)
    y = int(principal+x)
    return y