## Summary
* [Responsiveness](#responsiveness)
* [Home](#home)
    * [Navigation](#navigation)
    * [Footer](#footer)
    * [Patterns](#patterns)
    * [Categories](#categories)
* [Products](#products)
* [Bag & Checkout](#cart-checkout)
* [Account](#account)
    * [Registration](#registration)
    * [Sign In](#sign-in)
    * [Profile](#profile)
    * [Comments](#comments)
    * [Orders](#orders)
    * [Log out](#log-out)

**Back to [Readme.md](/README.md)**

****

## Responsiveness

![responsivness](/readme/images/ms4_mokup.png)

This site was was tested on multiple browsers (Google Chrome, Mozzila Firefox and Safari), multiple mobile devices (Samsung Galaxy, Huawei, iPhone) and tablet device(iPad Air) and it shown responsivness and compatibility. Web-site is responsive for screens from 350px to 2k.

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Viewing on mobile device | Images adapted, no overflow | As Expected | Pass |
| Viewing on tablet device | Pages rendering properly, no distortion | As expected | Pass |
| Viewing on laptop device | All in order, no distortion | As expected | Pass |
| Viewing on desktop device up to 2k | All in order, no distortion | As expected | Pass |

## Home

### Navigation

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on The Pattern Mill | Opens "Home" page | As Expected | Pass |
| Clicking on `about us` link | Opens about page with info  | As expected | Pass |
| Clicking on `patterns` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `categories` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `product placement` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `my account` link | Opens dropdown tab with links| As expected | Pass |
| Clicking on `bag icon` link | Opens shopping bag page| As expected | Pass |

### Footer

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Facebook` icon | Opens Facebook website in new tab | As expected | Pass |
| Clicking on `Instagram` icon | Opens Instagram website in new tab | As expected | Pass |
| Clicking on `Twitter` icon | Opens Twitter website in new tab | As expected | Pass |

## Patterns

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `by price` button | Opens the product page filtered by price | As expected | Pass |
| Clicking on `by rating` button | Opens the product page filtered by rating | As expected | Pass |
| Clicking on `by category` button | Opens the product page filtered by category | As expected | Pass |
| Clicking on `all patterns` button | Opens the product page showing all patterns | As expected | Pass |

## Categories

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `abstract` button | Opens the product page filtered by abstract category | As expected | Pass |
| Clicking on `floral` button | Opens the product page filtered by floral category | As expected | Pass |
| Clicking on `nature` button | Opens the product page filtered by nature category | As expected | Pass |
| Clicking on `geometric` button | Opens the product page filtered by geometric category | As expected | Pass |
| Clicking on `quirky` button | Opens the product page filtered by quirky category | As expected | Pass |
| Clicking on `all patterns` button | Opens the product page filtered by all patterns category | As expected | Pass |

## Products 

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on sort button | Sort products by price, name, rating, category | As Expected | Pass
| Clicking on product | Show product details info on a new page | As Expected | Pass
| Selecting the number in input and clicking "Add" | Adds the selected quantity of the item to cart and then opens "Shop" page |As Expected | Pass
| Selecting the size dropdown | Selects the size, personal or commercial |As Expected | Pass
| Clicking on `keep shopping` button | reverses back to products | As Expected | Pass
| Clicking on `add to bag` button | opens breadcrumbs success with option to go to checkout | As Expected | Pass

## Bag & Checkout

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `secure checkout` button | opens bag with bag info | As Expected | Pass
| Clicking on `update` or `remove` buttons | updates bag | As Expected | Pass
| Clicking on `secure checkout` button | Opens "Chekout" page | As Expected | Pass
| Clicking on `complete order` button without filling the form | Redirects user to required field | As Expected | Pass
| Clicking on `complete order` button after filling out the form | Checks with Stripe if everything is ok and opens order detail page and success breadcrumb | As Expected | Pass
| Clicking on `adjust bag` button before orafter filling out the form | redirects to "bag" page" page | As Expected | Pass

### Registration

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Register button | Registers the user and redirects to confirm email address. If registration form is incomplete, shows Please fill out this field | As Expected | Pass

### Sign in

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Log In` with correct username and password | Directs user to the index page | As Expected | Pass |
| Clicking on `Log In` with Incorrect username and password | flash message to user showing incorrect username or password | As Expected | Pass |
| Clicking on Forgot password | Opens "Forgot password" page | As Expected | Pass

### Profile

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Edit profile button | Opens "Edit profile" page |As Expected | Pass
| Clicking on `Update` button | Saves changes to profile and redirects to "Profile" page | As Expected | Pass
| Clicking on `order number` link | Shows order detail page | As Expected | Pass

## Comments

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `add comment` | redirects to comment form | As Expected | Pass
| Clicking on `delete comment` | deletes comment and redirects to products | As Expected | Pass
| Clicking on `Submit` button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking on `Submit` | redirects to product page | As Expected | Pass
| Clicking on `Submit` | shows failure message if unable to sent | As Expected | Pass

### Orders

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on a `order history` | Shows user's previous orders with all information | As Expected | Pass

### Log Out

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `log Out` button | Logs out user and redirects to index page | As expected | Pass |


**Back to [Top](testing.md)**