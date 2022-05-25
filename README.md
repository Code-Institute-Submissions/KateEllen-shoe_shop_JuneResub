<h1> Funky Feet </h1>

**View a live version of the site [here]().**

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
* As a **Registered User**, I want to be able to leave a review.
* As a **Registered User**, I want to be able to midify my review.

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

* [Homepage]()
* [All products]()
* [Product detail]()
* [Profile]()
* [Bag]()
* [Checkout]()

The final result is slightly different as during the development stage the way things were displayed was not as user friendly as expected. 

## Styling

### Colours

The palette of colors for the site is simple, the main colors are black and white. I added a pop of yellow to catch the eye. 

![Color-palette]()

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
      ![Sign In](https://github.com/KateEllen/shoe_shop/blob/main/media/product-example.png)


### Features on the Products Information Page



### Features on the Review Page 



### Features on the Profile Page  





### Features on the Shopping Bag


### Features on the Checkout Page 





### Features on the Subscription feature






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


