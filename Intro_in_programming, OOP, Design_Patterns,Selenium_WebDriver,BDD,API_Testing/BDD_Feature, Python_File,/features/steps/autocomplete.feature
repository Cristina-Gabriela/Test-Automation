Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Autocomplete Title
    Given the site formy
    When the person click on the Autocomplete
    And open a new page
    Then he fill all blank spaces <address>, <Street address>, <Street address2>, <City>, <State>, <Zip code>, <Country>

    Examples:
      | address               | Street address | Street address2 | City          | State         | Zip code | Country    |
      | Str.2600 Pearl Street | Boulder        | Abcd            | Mountain View | SUA           | 1600     | California |
      | 2300 Traverwood       | Abc            | MI              | Abcdr         | United States | 48105    | California |
      | 1 Hacker Way          | Menlo Park     | MI              | Asak          | United States | 94025    | California |
