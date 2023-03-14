# Testing
## Test Cases and Execution Report

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 

## Home Page testing

Home page: The home page provides the user with a clear understanding as to the purpose of the site. 
There is a clear call to action for the user to login or sign up at the top of the home page. 
The welcome message is clearly visible to the user when they first see the site, using any device.

![Home Page Screenshot](/assets/screenshots/homepage.png)

## Device responsiveness testing

Device responsivness: Each page of the site was tested on a range of relevant devices and checked against the purpose of the page. 

![Device Responsiveness Testing](/assets/screenshots/responsiveness.png)


### Testing Phase

#### Manual Testing

> Each user story was manually tested in line with intended functionality on both desktop & mobile.
> As this project was detailed by User Stories, manual testing was sufficient for all code, and met project requirements.
> If the expected outcome appears then a given test will be noted as a pass. If it does not then a fail is noted.

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create account | Pass |
| User can log into account| Pass|
|User can log out of account|Pass|

---

#### User Navigation Tests

| Test |Result  |
|--|--|
|User can navigate to Post Details | Pass |
|User can access menu items| Pass|
|SuperUser can access admin panel|Pass|

---

#### Account Security Tests

| Test |Result  |
|--|--|
|Non logged in user cannot add a post | Pass |
|Non logged in user cannot edit a post | Pass|
|Non superuser cannot access admin panel|Pass|

---

#### Vehicle Post Tests

| Test |Result  |
|--|--|
|User can post when all required fields are completed | Pass |
|User can post a published post when all required fields are completed | Pass |
|User can post a draft post when all required fields are completed | Pass |
|User tries to submit a post with empty form |Pass|
|User tries to submit form without a title | Pass|
|User can view their posts |Pass|
|User can edit the posts |Pass|
|Edit button does not present on confirmed bookings|Pass|
|Edit button does not present on declined bookings |Pass|
|User can delete a post|Pass|
|User presented with a further check when they click delete|Pass|
|User can like/unlike a post | Pass |
|User can comment on a post when all required fields are completed | Pass |

--- 

#### Account Tests

| Test |Result  |
|--|--|
|User cannot register username to the same as another user|Pass|
|User cannot register their email to the same as another user |Pass|
|User presented with correct date and time on a post|Pass|


#### Admin Tests

| Test |Result  |
|--|--|
|Admin can add posts to site|Pass|
|Admin can edit posts on site|Pass|
|Admin can delete posts on site|Pass|
|Posts admin change display correctly on main site when updated / added|Pass|

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 

---

## Google Lighthouse Testing

### Desktop

> index.html

![Google Lighthouse Index](/assets/testing/main-page-lighthouse.png)

> post_detail.html

![Google Lighthouse Profile](/assets/testing/detail-page-lighthouse.png)


## HTML W3 Validation

### index.html

![W3 Validation checker](/assets/testing/w3validation.png)
#### Result: No Errors

### post detail html

![W3 Validation checker](/assets/testing/w3validation-detail.png)
#### Result: No Errors

### CSS Validation

![w3 Jigsaw CSS checker](/assets/testing/cssvalidation.png)
#### Result: Pass - No Errors

### JSHint Validation

![w3 Jigsaw CSS checker](/assets/testing/jshintvalidation.png)
#### Result: Pass - No Errors - note about bootstrap expected.

### PyLint Validation

![CodeInst Python checker](/assets/testing/pythonvalidation.png)
#### Result: Pass - No Errors - and same across all files for pylint addin for Gitpod/VSCode.

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 
