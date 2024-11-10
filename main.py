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