# Automatic testing of code to see if it is functional.

# Queue Test
print("----QUEUE TEST----")
pass_count = 0
fail_count = 0
import classes.queue
print()
print("MAKE QUEUE: \t\t",end = "")
try:
    # Testing if you can make queue
    que = classes.queue.queue()
    print("PASS")
    pass_count += 1

    # Testing if origonal length is 0
    print("QUEUE LENGTH NEW: \t",end = "")
    if que.len() == 0:
        print("PASS")
        pass_count += 1
    else:
        print("FAIL")
        fail_count += 1

    # No data should be present and queue initialisation
    print("QUEUE DATA NEW: \t",end = "")
    if not que.isdata():
        print("PASS")
        pass_count += 1
    else:
        print("FAIL")
        fail_count += 1

    # Test Enqueue data
    print("QUEUE ENQUE: \t\t",end = "")
    que.enqueue("test")
    print("PASS")
    pass_count += 1

    # Testing if origonal length is 1 after enqueue
    print("QUEUE LENGTH DATA: \t",end = "")
    if que.len() == 1:
        print("PASS")
        pass_count += 1
    else:
        print("FAIL")
        fail_count += 1

    # Should have data now
    print("QUEUE DATA: \t\t",end = "")
    if que.isdata():
        print("PASS")
        pass_count += 1
    else:
        print("FAIL")
        fail_count += 1

    # Test Dequeue
    print("QUEUE DEQUE DATA: \t",end = "")
    if que.dequeue() == "test":
        print("PASS")
        pass_count += 1
    else:
        print("FAIL")
        fail_count += 1

    # Test Dequeue
    print("QUEUE DEQUE NULL: \t",end = "")
    if que.dequeue() == None:
        print("PASS")
        pass_count += 1
    else:
        print("FAIL")
        fail_count += 1
except Exception as e:
    print("FAIL: " + str(e))
    fail_count += 1
print(f"PASS COUNT: \t\t{pass_count}")
print(f"FAIL COUNT: \t\t{fail_count}")
print("------------")
