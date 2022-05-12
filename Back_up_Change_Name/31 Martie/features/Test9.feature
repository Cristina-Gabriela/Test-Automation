Feature:BDD
  As a Founder of a Social Media Application
  I want to see if it is accepted by the Open Source Community
  So that I will try first of all public the code and then to collect their opinions

  @Regression
  Scenario:Title Write Code Of Social Media Application
    Given One computer and the internet
    And The person will start to install pycharm
    When At the beginning of the project
    Then He/She try to install some useful python libraries
    And It is the moment to write the code
    And The code is run
    And He generate a report
    And The report is successful

  @Smoke
  Scenario: Title Public on Github
    Given Access at Github Local and Global
    And The Founder publish their code
    When All the code is uploaded
    Then The Open Source Community can verify the code
    And They can give the useful advices to the founder


  @Regression
  Scenario: Title Collect the opinions and ameliorate the python code
    Given Publicly the advices with the parts of code
    And The codes will be integrated
    When The entire code is successfully done
    Then The testers could automatically tested all the lines of code
    And The reports will arrived to the founder
