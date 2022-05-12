import requests

People = [
    {"name": "Felix", "lname": "ncdshfvbhs"},
    {"name": "John", "lname": "ncdshfvbhs"},
    {"name": "Oliver", "lname": "ncdshfvbhs"},
    {"name": "Li", "lname": "nccedfefrrwe"},
]

response = requests.post(url=, data=, headers=)
response = requests.get(url=, data=, )
response = requests.delete(url=, data=, )


def unique_user():
    assert_that(response.status_code).is_equal_to(200)
    peoples = requests.get(url=).json()
    is_new_user_created = filter(lambda person: person['lname'] == unique_last_name, people)

    add_new_user(is_new_user_created, peoples)


# def add_new_user():
#     new_users = [person for i in peoples if person['lname'] == unique_last_name]
#     assert_that(new_users).is_not_empty()
#     assert_that(is_new_user_created).is_true()

def add_new_user():
    new_users = search_users_by_last_name()
    assert_that(new_users).is_not_empty()
    assert_that(is_new_user_created).is_true()


def search_users_by_last_name():
    return [person for i in peoples if person['lname'] == unique_last_name]


(is_new_user_created, peoples):


def test_person_can_be_deleted():
    new_user = create_new_unique_user()
    all_users, _ = get_all_users()


def have_total():
    global money

    def money():
        x = economy()
        y = international_related()

    def cod():
        global international_related, economy

        def international_related():
            return ("power_of_buying")

        def economy():
            return ("cont")

    cod()


have_total()

money()


unique_user()

# def get(url, params=None, **kwargs):
# def post(url, data=None, json=None, **kwargs):

# print(response.status_code)


