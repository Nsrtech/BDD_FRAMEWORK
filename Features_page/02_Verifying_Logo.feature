Feature:OrangeHRM_Logo
  Background: Reusable_Code
    Given Launch Chrome Browser
    When Open OrangeHRM websites


  Scenario: Logo Checking
    Then Verify that the logo present on page
    And close browser

