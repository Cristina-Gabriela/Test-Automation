Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Complete Web Form Title
    Given the site formy
    When the person click on the Complete Web Form
    And open a new page
    Then he fill all blank spaces and click all buttons <First name>, <Last name>, <Job title>, <High School>, <College>, <Grad School>, <Male>, <Female>, <Prefer not to say>, <Years of experience>, <Date>, <Submit>
    Examples:
      | First name | Last name | Job title     | High School | College | Grad School | Male | Female | Prefer not to say | Years of experience | Date      | Submit |
      | Abc        | CJL       | IT Specialist | High School | College | Grad School | Male | Female | Prefer not to say | 5                   | 5.10.2020 |        |