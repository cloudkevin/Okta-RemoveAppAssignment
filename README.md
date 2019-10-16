# Okta-RemoveAppAssignment
Remove individual app assignments in Okta - originally created to be used when setting up the EA feature 'OU changes for Okta-mastered users'


When importing users from AD to Okta they are set to 'individual assignment' to AD. These users would not be able to be moved with the OU change feature. In order to fix this the users must be unassigned from AD, then reassigned via group assignment. Since this can only be done by manually unassigning the users, this script will find all users individually assigned to the given APP ID and remove that assignment. 

If using this as intended (with the Active Directory appId) turn off "Deactivate Users" to prevent suspensions.
