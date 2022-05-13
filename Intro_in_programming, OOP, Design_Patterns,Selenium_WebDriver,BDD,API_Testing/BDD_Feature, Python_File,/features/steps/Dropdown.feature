Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Dropdown Title
    Given the site formy
    When the person click on the Dropdown
    And open a new page
    Then click on the button Dropdown button and select (click) on each <option>
    Examples:
      | option                       |
      | Autocomplete                 |
      | Buttons                      |
      | Checkbox                     |
      | Datepicker                   |
      | Dropdown                     |
      | Enable and Disabled elements |
      | File Upload                  |
      | File Download                |
      | Key and Mouse Press          |
      | Modal                        |
      | Page Scroll                  |
      | Radio Button                 |
      | Switch Window                |
      | Complete Web Form            |
