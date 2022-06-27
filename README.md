
# The Pattern Mill - E-Commerce Web App.



![Mokup](/readme/images/ms4_mokup.png)

### Project Overview <hr>

Full Stack Frameworks with Django Project for Code Institute.

The goal of this project was to create a a full-stack site based around business logic used to control a centrally-owned dataset. The Pattern Mill is an e-commerce site which sells patterns which can be printed on anything from textiles to stationary or even canvas. Customers can purchase a pattern through Stripe after registering for an account and logging in. They can choose between personal use which is one time only or commercial use where they can use the pattern for commercial purposes.The admin can manage the site through the web app or through the Django admin site by adding, deleting products, updating price and commenting on each product.

[View Live Site Here](https://the-pattern-mill-ms4.herokuapp.com/)


## Contents

* [UX](#ux)
    * [Strategy](#strategy)
    * [Site User Goals](#site-user-goals)
    * [Site Owner Goals](#site-owner-goals)
    * [User requirements and expectations](#User-requirements-and-expectations)

* [DESIGN](#design)
    * [Design Choices](#design-choices)
    * [Colors](#colors)
    * [Fonts](#fonts)
    * [Structure](#structure)

* [WIREFRAMES](#wireframes)
    
#### Mobile

* [Home](#)
* [Get_started](#)
* [Sign_in](#)
* [Sign_up](#)
* [Add](#)
* [Member_page](#)
* [Trail_data](#)

#### Desktop

* [home](#)
* [browse_catalogue](#)
* [Sign_in](#)
* [Sign_up](#)
* [catagories_pages](#)
* [checkout](#)
* [profile](#)


* [TECHNOLOGIES USED](#technologies)

    * [Github](#github)
    * [Gitpod](#gitpod)
    * [Google Fonts](#google-fonts)
    * [Font Awesome](#font-awesome)
    * [Bootstrap CDN](#bootstrap)
    * [jQuery](#jquery)
    * [Popper.js](#popper.js)
    * [WAVE](#wave)
    * [W3 HTML](#w3-html)
    * [Jigsaw CSS](#jigsaw-css)
    * [Balsamic](#balsamic)
    * [HTML Beautifier](#html-beautyfier)
    * [django](#html-beautyfier)
    * [javascript](#html-beautyfier)

* [TESTING](#testing)

* [BUGS](#bugs)

* [DEPLOYMENT](#deployment)

* [CREDITS](#credits)

 
### UX <hr>

## Strategy  <hr>

The Pattern Mill is an online store where the customer can successfully purchase JPEG or PSD files of their chosen pattern and have it emailed directly to them. The customer can also request a hard copy or catalogue to be sent to their home or business address. Registered users get a record of their order history and the ability to comment on patterns. This means they can ask questions of the site owner or other customers who have purchased specific designs.

#### Site Owner Goals

As The Pattern Mill site owner:

* Design a site which represents the services offered and will appeal to the target market using appropriate colour schemes, imagery, typography and useful information.
* Ensure the site is easy to navigate and all information can be found by visitors within seconds.
* Increase website traffic from the target audience using tools such as google analytics, blogging and social media.
* Produce a site which is easily accessible on all sizes, mobile devices and browsers.
* A means to contact business owners directly for a more personal experience.

#### Site User Goals

As The Pattern Mill customer:

* As a potential customer, I would like to find all the info I need without complications.
* I want to easily navigate the site so that I can find content quickly with ease on any device.
* I want to be able to filter my product search by price, rating and categories.
* A quick search bar is imortant for me to help me find a pattern in the colour and style I want.
* I want to easily view the total of my purchases at any time and have the option to update or delete.
* I want to successfully register for an account and proceed to log in.
* I want to access to my order history.
* I do not want to re-enter my personal and delivery details for every order.
* I want to be able to contact the store of the website incase I have any issues or questons.
* I want to be able to comment and read comments below patterns and ask questions if needed.

#### User Requirements and expectations

As a user of The Pattern Mill site my requirements and expectations are:

* A fast loading time.
* A website which is clear and easy to navigate.
* Recognisable format, no surprises.
* A well designed, aesthetically pleasing user interface.
* The ability to make a decision based on site content.
* A means to contact business owners directly for a more personal experience.

## Scope <hr>

The site is designed with simplicity and ease of use in mind. Users can easily navigate the site without any distracting influences and can find the style, colour, design or category of pattern without complications. The nav bar and footer are repeated throughout every page to ensure users can navigate to whichever page they want or click onto the social media links on the footer to find more information or contact the site owner.

### Features

1. Content requirements
* Home page with browse our catalogue button to invite customers into the store to directly view all patterns.
* Navbar/About: Information about The Pattern Mill
* Navbar/Patterns: Dropdown with patterns filtered by price, rating, categories and the all patterns option.
* Navbar/Categories: Dropdown with patterns categorized by abstract, floral, nature, geometric and quirky.
* Navbar/Product Placement (to be implemented in the future): The ability to view prototypes of patterns printed on different mediums.
* Product details: Image, price, rating, description and comments.
* Shopping cart:
  * what products have been added to cart - quantity - total price and if there is a discount added
  * Total amount of the whole shopping cart and discount (if applicable).
* Account information:
  * My profile
  * My saved addresses
  * My order history

2. Functionality requirements
* User account:
  * Sign up / Log in / Log out with confirmation email sent.
  * Edit profile: personal information / delivery address
  * Order history
* Online shop:
  * Product filtering by categories
  * Product filtering by price
  * Product filtering by name (A-Z)
  * Product filtering by rating
  * Search for a product by name or description
  * Product showcase page with thumbnail images showing design name, designer, price, category and rating.
  * Product's details page with full image and more descriptions
* Shopping cart, create an order and payment:
  * View / Edit existing product's quantity / Delete existing product on shopping cart
  * Secured online payment with card through Stripe API
  * Order confirmation email
* Toast messages to inform users if their actions have succeeded or failed
* Admin and store management:
  * CRUD functionalities for product categories
  * CRUD functionalities for prices
  * CRUD functionalities for product descriptions and information
  * CRUD functionalities for users
  * CRUD functionalities for orders


## Structure <hr>

  
  ![](/readme/images/sitemap_ms4.png)

  The structure of the site .......

## The Skeleton Plane

### Wireframes

Since this is a big project, I have decided to put wireframes in separate file.

You can access them [here](/readme/wireframes/wireframes.md).

### Database Design

As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment

### User Model

The User model utilized for this project is the standard one provided by `django.contrib.auth.models`

### Profiles App

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|User | user |	OneToOneField 'User'| on_delete=models.CASCADE
|Default Phone Number |	default_phone_number | CharField | max_length=20, null=True, blank=True
|Default Street Address1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
|Default Street Address2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
|Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True
|Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
|Default Country | default_country | CountryField | blank_label='country', null=True, blank=True

### Products App

`Category` model

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|Name | name | CharField | max_length=254
|Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

`Product` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Category | category | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey
|SKU | sku | max_length=254, null=True, blank=True | CharField
|Name | name | default='', max_length=254 | CharField
|Description | content | blank=False | TextField
|Has_sizes| has_sizes | default='False', | blank=True | BooleanField
|Price | price | max_digits=6, decimal_places=2 | DecimalField
|Rating | rating | blank=True | DecimalField
|Image_url| image_url | max_length=1024, null=True, blank=True | UrlField
|Image| image| blank=False | ImageField


### Comment

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Post | post | pon_delete=models.CASCADE | ForeignKey
|Name | name | max_length=255  | CharField
|Article | article | blank=False  | TextField
|Date| date_added | auto_now_add=True | DateTimeField


### Checkout App

### Order

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order id | id | primary_key=True | AutoField
|User | user | User, on_delete=models.CASCADE, related_name="orders" | ForeignKey(User)
|Full name | full_name | max_length=50 | CharField
|Email | email | max_length=254, null=False, blank=False | EmailField
|Phone number | phone_number | max_length=20, blank=False | CharField
|Country | country | max_length=40, blank=False | CharField
|Postcode | postcode| max_length=40, blank=True | CharField
|Town or City | town_or_city | max_length=40, blank=False | CharField
|Street address 1 | street_address1 | max_length=40, blank=False | CharField
|Street address 2 | street_address2 | max_length=40, blank=False | CharField
|County | county | max_length=40, blank=False | CharField
|Date | date | default=timezone.now | DateField
|Delivery Cost| delivery_cost | (max_digits=6, decimal_places=2, null=False, default=0 | DecimalField
|Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
|Grand Total | grand_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
|Original Bag | original_bag | null=False, blank=False, default='' | TextField
|Stripe PID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField

### OrderLineItem

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order Line Item id | id | primary_key=True | AutoField
|Order | order | Order, null=False, blank=False, on_delete=models.CASCADE, | ForeignKey
|Product | product | Product, null=False, blank=False | ForeignKey
|Product Size | product_size | max_length=50, null=True, blank=True | CharField
|Quantity | quantity | blank=False | IntegerField
|Lineitem Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=Falsee | DecimalField


### DESIGN <hr>



#### DESIGN CHOICES




#### COLOURS




- ![#cf507b](https://via.placeholder.com/15/cf507b/000000?text=+) `#cf507b`
- ![#000000](https://via.placeholder.com/15/000000/ffffff?text=+) `#000000`
- ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff`


#### FONTS



#### IMAGES



### WIREFRAMES <hr>


#### Mobile



#### Desktop



### FEATURES <hr>

#### Feature 1: Home Page


### DATABASE <hr>


### TECHNOLOGIES USED <hr>

Languages used:

* HTML 5
* CSS
* Javascript
* JQuery
* JQuery

- [Gitpod](https://gitpod.io) 
    - Used **Gitpod** as my open source platform.
- [Github](https://github.com/) 
    - Used **Github** as my code hosting platform
- [Google Fonts](https://fonts.google.com/)
    - This project uses **Google fonts** to style the website fonts.
- [Materialize](https://www.https://materializecss.com/.com/)
    - This project uses **Bootstrap4** to simplify the structure of the website and make the website responsive
    - This project also uses BootstrapCDN to provide icons from [FontAwesome](https://www.bootstrapcdn.com/fontawesome/)

- [jQuery](https://jquery.com/)
    - This project uses **jQuery** to reference Javascript needed for the responsive navbar.
- [Popper.js](https://popper.js.org/)
    - **Popper.js** was used to reference Javascript needed for the responsive navbar.
- [WAVE](https://wave.webaim.org)
    - Used **WAVE** to evaluate my code to ensure the content is fully accessable to individuals with disabilities.
- [W3 HTML](https://validator.w3.org/)
    - Used **W3 HTMLs** for HTML code valuation
- [Jigsaw CSS](https://jigsaw.w3.org/css-validator/)
    - Used **Jigsaw CSS** to Validate CSS Code
- [Balsamic](https://balsamiq.com/)
    - Used **Balsamic** to create [WIREFRAMES](#wireframes)
- [PEP8 Online](http://pep8online.com/)
    - **PEP8 Online** For Python code valuation
- [JS Hint](https://jshint.com/)
    - **JS Hint** For Javascript code valuation


### TESTING <hr>

### Performance

Google Lighthouse was used to measure the speed and performance of the website. 

#### Lighthouse


### Accessibility

WAVE Web Accessibility Evaluation Tool was used to test the sites accessibility.

### Validation

Validation tools used:

- https://validator.w3.org/ :HTML Validation

- https://jigsaw.w3.org/css-validator/ : CSS Validation

- http://pep8online.com/ : Python Validation

- https://jshint.com/ : JS Validator


### Validation Results


### BUGS FOUND AND THEIR FIXES <hr>

    
### Deployment

## Project creation


### CHANGES TO IMPLEMENT AND INCLUDE<hr>

### CREDITS<hr>

#### Code

I relied heavily on code used in the Code Institutes tutorials to help me with this project, especially Code Institutes Boutique ADO project. I used these tutorials to guide me through the process of creating this site and all the functionality needed. I ammended the code to suit my own project.


#### Images

 
 ### ACKNOWLEDGEMENTS<hr><hr>
