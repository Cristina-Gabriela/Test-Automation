(venv) cristina@cristina-Inspiron-15-3511:~/PycharmProjects/pythonProject$ behave behaveProject
ConfigError: No steps directory in '/home/cristina/PycharmProjects/pythonProject/behaveProject'
(venv) cristina@cristina-Inspiron-15-3511:~/PycharmProjects/pythonProject$ cd behaveProject
(venv) cristina@cristina-Inspiron-15-3511:~/PycharmProjects/pythonProject/behaveProject$ behave features


====== WebDriver manager ======
Current google-chrome version is 97.0.4692
Get LATEST chromedriver version for 97.0.4692 google-chrome
Driver [/home/cristina/.wdm/drivers/chromedriver/linux64/97.0.4692.71/chromedriver] found in cache
Feature: Login Google # features/Test3.feature:1
  As a user
  I want to log into Google
  So that I can access Google Meet
  @Smoke
  Scenario: Test 1                       # features/Test3.feature:8
    Given I have access to the internet  # None
    When User enters Diana               # None
    And User enters the password abc1234 # None
    Then Login successful                # None

  @Regression
  Scenario: Test 1                       # features/Test3.feature:15
    Given I have access to the internet  # None
    When User enters Andrei              # None
    And User enters the password def4567 # None
    Then Login successful                # None

  @Regression
  Scenario: Test 1                      # features/Test3.feature:22
    Given I have access to the internet # None
    When User enters Maria              # None
    And User enters the password dsk568 # None
    Then Login successful               # None

  @Smoke
  Scenario Outline: Test Login -- @1.1    # features/Test3.feature:36
    Given I have access to the internet   # None
    When User enters users "Diana "       # None
    And User enters the password "abc123" # None
    Then Login                            # None

  @Smoke
  Scenario Outline: Test Login -- @1.2    # features/Test3.feature:37
    Given I have access to the internet   # None
    When User enters users "Andrei "      # None
    And User enters the password "fds565" # None
    Then Login                            # None

  @Smoke
  Scenario Outline: Test Login -- @1.3    # features/Test3.feature:38
    Given I have access to the internet   # None
    When User enters users "Maria "       # None
    And User enters the password "hgf456" # None
    Then Login                            # None

  @Smoke
  Scenario Outline: Test Login -- @1.4    # features/Test3.feature:39
    Given I have access to the internet   # None
    When User enters users "DJBNK "       # None
    And User enters the password "10fg36" # None
    Then Login                            # None

  @Smoke
  Scenario Outline: Test Login -- @1.5    # features/Test3.feature:40
    Given I have access to the internet   # None
    When User enters users "Dfedr "       # None
    And User enters the password "143ghk" # None
    Then Login                            # None

  @Smoke
  Scenario Outline: Test Login -- @1.6    # features/Test3.feature:41
    Given I have access to the internet   # None
    When User enters users "Dafey "       # None
    And User enters the password "189fe3" # None
    Then Login                            # None

Feature: Test Autocomplete Fromy # features/Test4.feature:1

  Scenario: Check address field                               # features/Test4.feature:2
    Given I go to autocomplete test                           # None
    When I type an address                                    # None
    Then The actual result should be the same as the expected # None


Failing scenarios:
  features/Test3.feature:8  Test 1
  features/Test3.feature:15  Test 1
  features/Test3.feature:22  Test 1
  features/Test3.feature:36  Test Login -- @1.1
  features/Test3.feature:37  Test Login -- @1.2
  features/Test3.feature:38  Test Login -- @1.3
  features/Test3.feature:39  Test Login -- @1.4
  features/Test3.feature:40  Test Login -- @1.5
  features/Test3.feature:41  Test Login -- @1.6
  features/Test4.feature:2  Check address field

0 features passed, 2 failed, 0 skipped
0 scenarios passed, 10 failed, 0 skipped
0 steps passed, 0 failed, 0 skipped, 39 undefined
Took 0m0.000s

You can implement step definitions for undefined steps with these snippets:

@given(u'I have access to the internet')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have access to the internet')


@when(u'User enters Diana')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters Diana')


@when(u'User enters the password abc1234')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password abc1234')


@then(u'Login successful')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Login successful')


@when(u'User enters Andrei')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters Andrei')


@when(u'User enters the password def4567')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password def4567')


@when(u'User enters Maria')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters Maria')


@when(u'User enters the password dsk568')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password dsk568')


@when(u'User enters users "Diana "')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters users "Diana "')


@when(u'User enters the password "abc123"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password "abc123"')


@then(u'Login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Login')


@when(u'User enters users "Andrei "')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters users "Andrei "')


@when(u'User enters the password "fds565"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password "fds565"')


@when(u'User enters users "Maria "')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters users "Maria "')


@when(u'User enters the password "hgf456"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password "hgf456"')


@when(u'User enters users "DJBNK "')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters users "DJBNK "')


@when(u'User enters the password "10fg36"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password "10fg36"')


@when(u'User enters users "Dfedr "')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters users "Dfedr "')


@when(u'User enters the password "143ghk"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password "143ghk"')


@when(u'User enters users "Dafey "')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters users "Dafey "')


@when(u'User enters the password "189fe3"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters the password "189fe3"')


@given(u'I go to autocomplete test')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I go to autocomplete test')


@when(u'I type an address')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type an address')


@then(u'The actual result should be the same as the expected')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The actual result should be the same as the expected')

(venv) cristina@cristina-Inspiron-15-3511:~/PycharmProjects/pythonProject/behaveProject$ ^C
(venv) cristina@cristina-Inspiron-15-3511:~/PycharmProjects/pythonProject/behaveProject$

