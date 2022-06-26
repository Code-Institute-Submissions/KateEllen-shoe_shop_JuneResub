<h1> Funky Feet </h1>

**View a live version of the site [here](https://funky-feet.herokuapp.com/).**

This project has been created for educational purposes.

It is an E-Commerce site for a fictional company 'Funky Feet' which offers a variety of ladies shoes for sale.

![Responsive]()
___

## Table of Contents



## User Experience 

## Project Goals

The goal of this project is to create E*Commerce store for a ladies shoe shop. 
This project is for educational purposes only.

### Importance and Feasibility chart

| Opportunity/Problem                                                    | Importance | Viability/Feasibility |
| :--------------------------------------------------------------------- | :--------: | :-------------------: |
| 1. Users are able to register an account and login                     |     5      |           5           |
| 2. Users can add, edit and remove items from their shopping bag        |     5      |           5           |
| 3. Users are notified of their actions while interacting with the site |     5      |           4           |
| 4. Users can search for products by keyworkds                          |     4      |           4           |
| 5. Users can sign up to the newsletter                                 |     3      |           4           |

## User Stories

### User Goals

* As a **User**, I want to easily understand the purpose of the site when navigating on it.
* As a **User**, I want to be able to intuitively navigate the entire site in an easy way.
* As a **User**, I want to be able to have the same functionalities on different devices (mobile, tablet and PC).
* As a **User**, I want to be able to see what items are available for purchase on the site.
* As a **User**, I want to know the prices of the items.
* As a **User**, I want to be able to sign up for an account and receive a confirmation email.
* As a **User**, I want to be able to sign up for the newsletter.


### Registered User goals

* As a **Registered User**, I want to be able to easily login and logout of my account.
* As a **Registered User**, I want to be able to easily add and remove items in my shopping bag.
* As a **Registered User**, I want to be able to easily purchase items on my shopping bag.
* As a **Registered User**, I want to receive a purchase confirmation email.
* As a **Registered User**, I want to be able to easily update my contact and delivery information.
* As a **Registered User**, I want to be able to view my previous orders.


### Site Owner/Superuser goals

* As a **Site Owner/Superuser**, I want to be able to add new products.
* As a **Site Owner/Superuser**, I want to be able to edit and delete products.
* As a **Site Owner/Superuser**, I want to be able to access the admin section of the site to view orders made, the items they contain and the delivery information.
* As a **Site Owner/Superuser**, I want to be able to access the admin section of the site to view users registered. 


## Site Structure

The aim of the site is offer an easy to navigate and accesible uer experience.
The different elements on the site (header/footer/nav links) remain the same across the site but will be displayed differently from mobile to other devices. The header will always contain a link to the products page and different links based on whether a user is logged in or a super*user.

### Other links:
* User not logged in: 
    * Register
    * Login

* Logged in:
    * My Profile
    * Shopping Bag
    * Logout

    * **Only as superuser** 
        * Admin (dropdown)
            * My profile
            * Explore management
            * Product management

### Wireframes 

The wireframes of the site can be found in the following links: 

* ![Homepage](https://github.com/KateEllen/shoe_shop/blob/main/media/home-wireframe.png)
* ![All products](https://github.com/KateEllen/shoe_shop/blob/main/media/all-products-wireframe.png)
* ![Product detail](https://github.com/KateEllen/shoe_shop/blob/main/media/product-detail-wireframe.png)
* ![Profile](https://github.com/KateEllen/shoe_shop/blob/main/media/profile-wireframe.png)
* ![Bag](https://github.com/KateEllen/shoe_shop/blob/main/media/bag-wireframe.png)
* ![Checkout](https://github.com/KateEllen/shoe_shop/blob/main/media/checkout-wireframe.png)

The final result is slightly different as during the development stage the way things were displayed was not as user friendly as expected. 

## Styling

### Colours

The palette of colors for the site is simple, the main colors are black and white. I added a pop of yellow to catch the eye. 

![Color-palette](https://github.com/KateEllen/shoe_shop/blob/main/media/colour-scheme.png)

# Features

## Existing Features 

### Features in all apps
* Toast Messages, which are pop up messages appear. The toast messages will notify the user when an action has been successful or unsuccessful. These messages can be dismissed by the user by clicking the x button.
![Footer](https://github.com/KateEllen/shoe_shop/blob/main/media/order-success.png)

* Navbar 
  * Contains the site name, My Account dropdown, Shopping bag, Search bar, all shoes, boots, heels, trainers, flats and special offers.
  * My Profile and Logout links. Logged in superusers will also find the Manage Products.
  * The Basket link will take users to their shopping basket page. 
  * The search function allows users to input keywords that filter the content to meet the inputed criteria.

* Funky Feet Logo 
  * A clickable link that brings you back to the homepage.

![Nav and Logo](https://github.com/KateEllen/shoe_shop/blob/main/media/nav-and-logo.png)

### Footer 
  * Subscribe, so the users can sign up for the NewsLetter.
  * Facebook link. 
  ![Footer](https://github.com/KateEllen/shoe_shop/blob/main/media/footer.png)

### Features on the Home Page
* Home Image 
  * An image that shows to the user what the site is about.
![Home page](https://github.com/KateEllen/shoe_shop/blob/main/media/homepage.png)

### Features on the Sign Up Page 
* Sign Up Form 
  * A very simply form, with instructions on how to register for the site. The text is clear and legible.
  * Has form control that will tell the user if any fields haven't been filled out correctly whilst ensuring the form doesn't get sent without the required information.
  * It includes the following fields:
    *  Email field
    *  Confirm email
    *  Username
    *  Password
    *  Confirm password fields. 
    *  Link to redirect users who have already registered in the site.

* Sign Up Button 
  * This button generates and sends a verification email link, to the email address provided. 
  * This will allow the user to have accesible that information in their personal area. 

    ![Sign Up](https://github.com/KateEllen/shoe_shop/blob/main/media/sign-up.png)

### Features on the Sign In Page 
* Sign In Form 
  * Another easy Form, with instructions on how to log into the site. 
  * Form control.
  * Includes a username and password field, with a link at the top to direct users who haven't registered to the Sign Up page.
  * Within the form there is also a remember me tick box which will save your login information for future visits.

* Home Button 
  * Button to return to the home page.

* Sign In Button 
  *  Authenticates the user and return to the home page.

* Unique Email Required. 
  * ![Unique Email](https://github.com/KateEllen/shoe_shop/blob/main/media/unique-email.png)

* Forgotten Password Link 
  * Users can reset their password if they've forgotten it. An email containing a link that directs users to simple instructions on how to reset their password. 
    ![Sign In](https://github.com/KateEllen/shoe_shop/blob/main/media/login.png)

### Features on All Products
* Page Title 
  * Helps the user to make sure they are on the correct page.

* Sort By Dropdown 
  * Sort All Products by price (high/low) or alphabetically.

* Edit/Delete links 
  * (Superusers Only) Access to the Edit/Delete links allowing them to delete products and directing them to the Edit page to edit the different products.
      ![All products](https://github.com/KateEllen/shoe_shop/blob/main/media/product-example.png)


### Features on the Products Information Page
* Image 
  * Image of the selected product. 

* Product Information 
  * Name
  * Price
  * Category
  * Description
  * Size selector
  * Quantity selector
![Product Information](https://github.com/KateEllen/shoe_shop/blob/main/media/product-info.png)

### Features on the Profile Page  

* Delivery Information Form 
  * This form shows the user's default delivery information. 
  * There are required fields that need to be filled/updated before being able to save it.
  * The information from this form will automatically be taken from the order form when the user is buying something if they have filled out the checkout form and clicking the tick box 'Save this delivery information to my profile'.

* Form Fields 
  * The input fields are: 
    * Phone Number
    * Street Address 1
    * Street Address 2
    * Town or City
    * County
    * Postcode
    * Country dropdown to make easier for the user to find their country.

  * The form has instructions in how to be completed and also has form validation 

* Update Information Button 
  * If the users want to update their delivery information, fill out the fields in the form above with the required information and click this button to save the updated information to their profile.

* Order History 
  * This section provides users with their personal order history, including date, time, items ordered, order number, etc.
  * The most recent order will be displayed at the top.

  ![Profile](https://github.com/KateEllen/shoe_shop/blob/main/media/my-profile.png)


### Features on the Shopping Bag
* List of Added Items
  *  The list contains:
     *  Product Info section
     *  Image
     *  Product name 
     *  SKU 
     *  Total price section 
     *  Quantity function with -/+ buttons to adjust the amount of items that the user wants to buy, in case they want to add more items.

* Basket Total 
  *  This is the total items the user will have in their shopping bag. 

* Delivery  
  * Delivery charge the user will be charged if they don't reach the $80 to get a free delivery.

* Grand Total  
  * The sum of the total of all the items in the bag and delivery charge. This is the total amount the users will be charged in their cards. 

![Product Information](https://github.com/KateEllen/shoe_shop/blob/main/media/product-info.png)

### Features on the Checkout Page 
* Payment form 
  * Follow same structures and form validation. 
  * If the user have ordered before the information will be populated as well.

* Save Information Tickbox 
  * If the user ticks their information will be saved for thenext time.
  * If a field needs to be updated the user can enter the information in the checkout form and it will override the data on the profile page if the user select 'Save this delivery information to my profile'.

* Payment Form Field 
  * This box will require users their card information (card number, month/year, cvc and zip code). To test you must use stripe default test card.

* Adjust Bag Button 
  * Redirect the users back to the Shopping Bag page.

* Complete Order Button 
  * The order for the user is processed. 
  * Generates a confirmation email that is sent to the email address provided in the checkout form.

* Card Charge Warning 
* Reminder for the users to tell them that their card will be charged with the stated amount.

![Checkout](https://github.com/KateEllen/shoe_shop/blob/main/media/checkout.png)

### Features on the Subscription feature
** Please note that email from site (Funky Feet) may end up in spam folder **

* The user can subscribe to the page.
* The user have an input box and a button to subscribe.
* The user will be receiving an email in their inbox.

### Comments 

### Blog

### Add Post (superuser only)

### Delete Post (superuser only)

## Future features 
* Returns
* Product rating
* Live chat

# Testing

The full testing performed can be found [here](./TESTING.md)


# Deployment 
## Heroku Deployment
It's required to have an [AWS](https://aws.amazon.com/s3/) account and a [S3 bucket](https://aws.amazon.com/s3/) to hold all the static files for this project.

1. Open and login to [Heroku](https://id.heroku.com/login)

2. Add all of your Config Vars. Such as keys for AWS, Stripe, Secret Key, Database URL and Email keys. 

3. In your local terminal type "heroku login"

4. Use git to clone your repository's sorce code to your local machine. You can do this by typing "heroku git:clone -a (REPO NAME) then cd (REPO NAME) into yout terminal.

5. Now make some changes to the code you just clined and deploy them to Heorku using Git. You can do this by typing "git add ." followed by "git commit -m 'commit message' " then you will finally type "git push heroku main" to deploy to Heorku. This is all done in your local terminal. 

6. When your app is deployed successfully. Click _Open App_ in to top right hand corner of Heroku to open app in a new tab in the browser.

## Entity Relationship Diagram


## Database Choice
I used postgres as the database because the data is relational and heroku serves this up realitvely easily with no cost.The models used to construct the site are outlined below:

# E-commerce Business Model


## Facebook Business Page

## Newsletter Signup


## SEO Strategy

### Keywords
### Description
### Title
### Relevant Content
### Sitemap

### Robots.txt


# Credits

## Content 
* Products info and pictures - [Office](https://www.office.co.uk/)
* Wireframes - [Balsamiq](https://balsamiq.com/wireframes/)

## Media 
Images - [Office](https://www.office.co.uk/)
Facebook cover photo - [Canva](https://www.canva.com/)
* [Font-Awesome](https://fontawesome.com/)


## Acknowledgements

### I received inspiration for this project from:
* [Boutique Ado](https://github.com/ckz8780/ci-fsf-hello-django/tree/c13b414fd2e87a54b4f2788ceffec55be4ade925)
* [Office](https://www.office.co.uk/)
* [StackOverflow](https://stackoverflow.com/)
* [Coolors](https://coolors.co/)


### I received advice and support from
* [Niall Maher](https://www.linkedin.com/in/nialljoemaher/?originalSubdomain=ie)
* Code Institute [Slack Community](code-institute-room.slack.com)
* My mentor Malia was a huge help in this project as always. She constantly steered me in the right direction and helped me with my many questions on queries. 


