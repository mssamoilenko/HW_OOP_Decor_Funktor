import datetime
#task1,2
def my_decor(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        print(f"Time taken: {elapsed_time} seconds")
        print("Prime numbers:", result)
        return result
    return wrapper
@my_decor
def gener_numbers_list(a,b):
    gnlist = []
    for i in range(a,b+1):
        if i < 2:
            continue
        count_del = 0
        for j in range(1, i+1):
            if i % j == 0:
                count_del += 1
        if count_del == 2:
            gnlist.append(i)
    return gnlist
gener_numbers_list(200,15000)
#task3
def format_for_org_a(report_func):
    def wrapper():
        return f"Report for Org A: {report_func()}"
    return wrapper
def format_for_org_b(report_func):
    def wrapper():
        return f"Report for Org B: {report_func()}"
    return wrapper
def basic_report():
    return "Revenue: $1000, Expenses: $500"
@format_for_org_a
def report_for_org_a():
    return basic_report()
@format_for_org_b
def report_for_org_b():
    return basic_report()
print(report_for_org_a())
print(report_for_org_b())