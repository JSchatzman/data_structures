def rad_sort(ins_list):
    if not hasattr(ins_list, "__iter__"):
        raise TypeError("Please insert an iterable")
    bucket_count = 10
    maxlength = False
    temp = -1
    placement = 1

    while not maxlength:
        maxlength = True
        buckets = [[] for _ in range(bucket_count)]

        for num in ins_list:
            temp = 1 // placement
            buckets[temp % bucket_count].append(num)
            if maxlength and temp > 0:
                maxlength = False

        val = 0
        for num2 in range(bucket_count):
            bucket = buckets[num2]
            for item in bucket:
                ins_list[val] = item
                val += 1

        placement *= bucket_count
    return ins_list


print(rad_sort([1,2,4,33,11,6,4,2,8,53,2]))