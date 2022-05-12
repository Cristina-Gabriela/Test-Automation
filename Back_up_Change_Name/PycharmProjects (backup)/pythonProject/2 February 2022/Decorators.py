import psutil as psutil


# o varianta care iti permite sa culegi metrici la nivel de memorie, de CPU,etc. de sistem.
# pt. a nu se ajunge un anumit nivel de utilizare.

def get_virtual_memory():
    print(psutil.virtual_memory().percent)


# get_virtual_memory()

# a = get_virtual_memory()
# print(a)


def get_virtual_memory_2():
    return psutil.virtual_memory().percent


get_virtual_memory()


# Nested Function- cand avem o functie in alta functie (()):
def display_test_logs(msg):
    def logger():
        print(f"Logging memory data.{get_virtual_memory_2()}{msg}")

        def test():
            print("Hello")

        test()

    logger()


display_test_logs("thumbs up")


def display_test_logs_v2():
    threshold = 90

    def logger():
        print(threshold)
    return logger

display_test_logs_v2()()






