Feature : Order Transaction

  Scenario Outline: We are validating the Order is getting created sucessfully
    Given Place the new order using API and <username> & <password>
    And the user is on the landing page
    When I login into the portal with <username> and <password>
    And navigate to orders details page
    And Select the order
    Then Verify that the order message is created
    Examples:
      | username        | password |
      |puneet@puneet.com| Puneet123|