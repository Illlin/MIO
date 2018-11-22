# Automatic testing of code to see if it is functional.

# Format text to be read easily
def print_test(text,success):
    print("{0:<20}: {1}".format(text,success))

def test(class_name,tests):
    print("--------"+class_name+"--------")
    # Notes for future reference
    """
    [
        ["NAME", function, input, output],
        ["NAME", function, input, output],
    ]
    """
    pass_count = 0
    fail_count = 0

    for test_case in tests:
        test_name = test_case[0]
        test_input, test_output = test_case[2], test_case[3]
        try:
            # Run Function
            output = test_case[1](*test_input)
            if output == test_output:
                print_test(test_name, "PASS")
                pass_count += 1
            else:
                print_test(test_name, "FAIL: " + str(type(output)) +": "+ str(output))
                fail_count += 1
        except Exception as error:
            print_test(test_name,"FAIL " + str(error))
            fail_count += 1
    print_test("PASS COUNT", str(pass_count))
    print_test("FAIL COUNT", str(fail_count))
    print("----------------")


#New Queue test:
import classes.queue
que = classes.queue.Queue()
test(
    "QUEUE",
    [
    #   NAME                    FUNCTION            INPUT       OUTPUT
        ["QUEUE LENGTH NEW",    que.len,            (),         0],
        ["QUEUE DATA NEW",      que.isdata,         (),         False],
        ["QUEUE ENQUE",         que.enqueue,        ("test",),  None],
        ["QUEUE LENGTH DATA",   que.len,            (),         1],
        ["QUEUE DATA",          que.isdata,         (),         True],
        ["QUEUE DEQUEUE NEW",   que.dequeue,        (),         "test"],
        ["QUEUE DEQUEUE NONE",  que.dequeue,        (),         None],
    ]
)

import classes.json_file
import os
file = "test.json"

# Make sure file is not there
if os.path.isfile(file):
    os.remove(file)

json = classes.json_file.Json_file(file)
test(
    "JSON",
    [
    #   NAME                    FUNCTION                INPUT               OUTPUT
        ["ADD DATA",            json.set_data,          ("test","check"),   None],
        ["GET DATA",            json.get_data,          ("test",),          "check"],
        ["WRITE FILE",          json.write_to_file,     (),                 None],
        ["READ FILE",           json.load_from_file,    (),                 None],
        ["VALIDATE READ",       json.get_data,          ("test",),          "check"],
    ]
)
# Clear output of file:
if os.path.isfile(file):
    os.remove(file)
    