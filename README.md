
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
    * [User requirements and expectations](#user-requirements-and-expectations)

    * [Scope](#scope)
    * [Features](#features)
    
    * [Structure](#site-owner-goals)
    
    * [Skeleton Plane](#the-skeleton-plane)
    * [Wireframes](#wireframes)

    * [Database Design](#database-design)
    * [User Model](#user-model)
    * [Profiles App](#profiles-app)
    * [Checkout App](#checkout-app)

* [DESIGN](#design)
    * [Design Choices](#design-choices)
    * [Colors](#colors)
    * [Fonts](#fonts)
    * [Images](#itructure)

* [TECHNOLOGIES USED](#technologies)

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

### Wireframes <hr>

Since this is a big project, I have decided to put wireframes in separate file.

You can access them [here](/readme/wireframes/wireframes.md).

### Database Design <hr>

As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment


### User Model

The User model utilized for this project is the standard one provided by `django.contrib.auth.models`


### Profiles App <hr>

| Name | Database Key | Field Type | Type Validation |
| :-------------: |:----------------:| :--------------: | :---------: |
|User | user |	OneToOneField 'User'| on_delete=models.CASCADE
|Default Phone Number |	default_phone_number | CharField | max_length=20, null=True, blank=True
|Default Street Address1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
|Default Street Address2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
|Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True
|Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
|Default Country | default_country | CountryField | blank_label='country', null=True, blank=True


### Products App <hr>


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


`Comment` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Post | post | pon_delete=models.CASCADE | ForeignKey
|Name | name | max_length=255  | CharField
|Article | article | blank=False  | TextField
|Date| date_added | auto_now_add=True | DateTimeField


### Checkout App <hr>


`Order` model

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


`Order Line Item` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order Line Item id | id | primary_key=True | AutoField
|Order | order | Order, null=False, blank=False, on_delete=models.CASCADE, | ForeignKey
|Product | product | Product, null=False, blank=False | ForeignKey
|Product Size | product_size | max_length=50, null=True, blank=True | CharField
|Quantity | quantity | blank=False | IntegerField
|Lineitem Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=Falsee | DecimalField


## DESIGN <hr>


The fact that The Pattern Mill is a site showcasing patterns and designs, I decided to let these images bring life to the page while using black typograpy and white space throughout to create a clean crisp site with priority on the patterns. The landing page has a very bright pink hero image of flamingos with a black button inviting users to browse the catalogue, while the navbar, footer and store title are all black and white. It was created like this to ensure ease of navigation and a simple and elegant site.


### DESIGN CHOICES



#### COLOURS

- ![#cf507b](https://via.placeholder.com/15/cf507b/000000?text=+) `#cf507b`
- ![#000000](https://via.placeholder.com/15/000000/ffffff?text=+) `#000000`
- ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff`



#### FONTS

Viaoda Libre is the main font used throughout the site. I chose it for it's traditional design which has a modern feel to it. I wanted the site to feel like a gallery, so the incorporation of traditional and modern together work well for this type of store.


#### IMAGES


I download all the images used throughout the site from Unsplash


[View Unsplash Site Here](https://unsplash.com/)


and Pexels


[View Pexels Site Here](https://www.pexels.com/)



## FEATURES <hr>


## TECHNOLOGIES USED <hr>

The website is designed using following technologies:

### Programming languages

* HTML - the project used HTML to define structure and layout of the web page;
* CSS - the project used CSS stylesheets to specify style of the web document elements;
* JavaScript - the project used JavaScript to implement Stripe, EmailJS and custom Javascript.
* Python - the project back-end functions are written using Python.

### Libraries

* [Font Awesome](https://fontawesome.com/v4.7.0/) - Font Awesome icons were used throughout the web-site.
* [jQuery](https://jquery.com/) - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation.

### Frameworks & Extensions

* [Django](https://www.djangoproject.com/) – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Bootstrap](https://getbootstrap.com/) – Bootstrap is a web framework that focuses on simplifying the development of informative web pages.
* [EmailJS](https://www.emailjs.com/) – Service that helps sending emails using client side technologies only. It only requires to connect EmailJS to one of the supported email services, create an email template, and use their Javascript library to trigger an email.
* [Stripe](https://stripe.com/ie) – Allows individuals and businesses to make and receive payments over the Internet.

### Database
* [Heroku Postgres](https://www.heroku.com/postgres/) – PostgreSQL is one of the world's most popular relational database management systems.

### Others

* [GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git.
* [Gitpod](https://gitpod.io/workspaces/) - One-click ready-to-code development environments for GitHub.
* [Heroku](https://dashboard.heroku.com/) - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps.
* [AWS-S3](https://aws.amazon.com/s3/) – Object storage service that offers industry-leading scalability, data availability, security, and performance.



## Testing

**Testing section is located [here](/readme/testing/testing.md)**

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


# Deployment

## AWS S3
Created a new Amazon account and connect to amazon service AWS3 account are cloud based serve where the project media and staicfiles will be stored unto. Firstly, locate S3 on amazon service and create a bucket. While creating the bucket on S3, the note that public access must be all switched off to allow access for users.

Once the bucket has been created, we now can now click on its properties and enable the Static Website Hosting option, so it can serve the purpose of hosting our static files, you will need to imput an index.html and error.html before saving. Then we go into the created bucket Permissions and click into CORS configuration, this part already has a prefilled default config, All that is needed is just to write the default code and save the config.

Next, go into the bucket policy to allows access to the contents across all web and inside this put  some code including arn address displayed at the top of the heading. Then go into amazon IAM to allow identity and access management of our stored files and folder. In the IAM service, add a new group for the application and then set the policies to ALL. It generates a downlaodable zip file containing ID and KEY to be used for the newly added group. This ID and KEY as to be stored in an environment variable.

This then allows us to into our terminal window and install some settings Boto3 Django Storages

The Django Storages is passed into the installed apps in settings and also a custom_storage file is created to store credentials in environment variable. And once everything looks fine python3 manage.py collectstatic can be run. This will collect all the static files in our app including any changes that is made. N.B this command has to be run in the development(local) environment each time a change is been made in the static files/folder And your folder and files should display in your AWS S3 BUCKETS

## Heroku Deployment 

#### Create application:

1. Navigate to Heroku.com and login.
2. Click on the new button.
3. Select create new app.
4. Enter the app name.
5. Select region.

#### Set up connection to Github Repository:

1. Click the deploy tab and select GitHub - Connect to GitHub.
2. A prompt to find a github repository to connect to will then be displayed.
3. Enter the repository name for the project and click search.
4. Once the repo has been found, click the connect button.

#### Add PostgreSQL Database:

1. Click the resources tab.
2. Under Add-ons seach for Heroku Postgres and then click on it when it appears.
3. Select Plan name Hobby Dev - Free and then click Submit Order Form.

#### Set environment variables:

1. Click on the settings tab and then click reveal config vars.
2. Variables added: 
    * AWS_ACCESS_KEY_ID 
    * AWS_SECRET_ACCESS_KEY 
    * DATABASE_URL 
    * EMAIL_HOST_PASS 
    * EMAIL_HOST_USER
    * SECRET_KEY 
    * STRIPE_PRICE_ID 
    * STRIPE_PUBLIC_KEY 
    * STRIPE_SECRET_KEY 
    * STRIPE_WH_SECRET 
    * USE_AWS 

#### Enable automatic deployment:

1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

## Local Deployment

1. Navigate to the GitHub Repository.
2. Click the Code drop down menu.
3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
4. Open your developement editor of choice and open a terminal window in a directory of your choice.
5. Use the git clone command in terminal followed by the copied git URL.
6. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages: pip install -r requirements.txt


## Project creation


### CHANGES TO IMPLEMENT AND INCLUDE<hr>

### CREDITS<hr>

#### Code

I relied heavily on code used in the Code Institutes tutorials to help me with this project, especially Code Institutes Boutique ADO project. I used these tutorials to guide me through the process of creating this site and all the functionality needed. I ammended the code to suit my own project.

 ### ACKNOWLEDGEMENTS<hr><hr>
