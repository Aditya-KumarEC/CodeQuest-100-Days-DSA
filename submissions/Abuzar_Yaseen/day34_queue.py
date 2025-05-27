def queue_num(enqueue_list,remove_count):
    queue = []
    for items in enqueue_list:
        queue.append(items)
    for _ in range(remove_count):
        if queue:
            queue.pop(0)

    print("Remaining Queue: ",*queue)

item = list(map(int,input("Enqueue: ").split()))
count = int(input("Dequeue: "))
queue_num(item,count)