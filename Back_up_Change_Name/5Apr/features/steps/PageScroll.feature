Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Page Scroll Title
    Given the site formy
    When the person click on the Page Scroll
    And open a new page
    Then fill the <Full Name>, <Date>
    Examples:
      | Full Name        | Date       |
      | Asdfg Tmdskbf    | 14.03.2021 |
      | Asladns Rdksjbf  | 10.03.2020 |
      | Asdfgh Pdjbf     | 14.09.2014 |
      | Afdhfdgnk Aisf   | 23.10.1999 |
      | Sfdfndj Opreub   | 07.03.2014 |
      | Ajkndkj Kdsnfei  | 03.05.2020 |
      | Ydsdfdn Odofncfd | 09.12.2012 |
      | Fdsmkd Namedsn   | 17.10.2021 |
      | Fpopu Nbknln     | 18.12.1995 |