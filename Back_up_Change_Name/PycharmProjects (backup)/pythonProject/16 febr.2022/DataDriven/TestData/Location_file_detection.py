import pathlib

if __name__ == '__main__':
    location = pathlib.Path(__file__).parent.parent.parent.resolve()
    print(location)
    location_file = pathlib.Path(__file__).parent.parent.resolve()
    print(location_file)
    location_main_file = pathlib.Path(__file__).parent.resolve()
    print(location_main_file)
    location_specified_file = pathlib.Path(__file__).resolve()
    print(location_specified_file)

call_1 = "Do you have a new job? / Immediately, I will have a new job in IT."
open_call_1 = open(location_specified_file, 'w')
open_call_1.write(call_1)
open_call_1.close()

read_open_call_1 = open(location_specified_file)
call_1 = read_open_call_1.read()
print(call_1)
