# Contents 

# Ex Planta 
![Website mock ups]()
The live site can be viewed [here]

# UX
## Strategy
### Project Goals 
The goal of this project is to build a full-stack site that allows users to manage a common dataset using CRUD functionality. 

Ex Planta is a speciality vegan recipe website. The websites aim is to encourage users to upload, save and edit recipes to build a destination for people who live by vegan or plant-based values. The secondary aim is create a revenue stream by promoting a vegan cookbook linking to an external sales site. 

### User Stories 
First time user goals: 
- As a first time user, i want to understand the purpose of the website easily from the homepage
- As a first time user, i want to see enticing recipes that inspire me to recreate them
- As a first time user, i want to establish the benefits of registering and creating an account 
- As a first time user, i want to be able to register and login quickly and eaisly using simple but safe forms

Returning user goals:
- As a returning user, i want to easily log in to my account 
- As a returning user, i want to be able to veiw full recipes including the ingredients list and method
- As a returning user, i want to be able to search recipes by name
- As a returning user, i want to be able to save recipes i like to easily locate at a later date 
- As a returning user, i want to be able to upload recipes to the site for others to create 
- As a returning user, i want to be able to edit & delete recipes i have previously added

Admin user goals:
- As an admin user, i need to be able to edit or delete any recipe which i feel arent suitable for the website 


# Structure
## Features
Features differ for two different types of users, as a new user without an account i can:
- Veiw the homepage 
- view the recipe page
- view recipe cards but not the detail including ingredients and method, this is to encourage users to sign up to the site 
- view the login page
- view the register page

As a logged in account user, i can view all that a new user can as well as: 
- view a log out page 
- view a user profile page 
- view a full recipe including method and ingredients using the recipe card button 
- Full use of CRUD functionality;
    - Create a recipe using the add recipe page 
    - Read a full recipe card including all the details 
    - Delete one of my recipes on the profile page
    - Edit one of my recipes on the profile page  

### Home Page
- The homepage features a carousel of recipes, created by admin only to ensure it only features appropriate and complete recipes for site user. A button is also featured on the carousel which directs to the recipe page. 
- An "About us section" along with a call to action button linking to an external page where a user can buy the cook book. This supports the secondary project goal. 
- A "whats new" feature, a small snippet of recipes the user can expect to see with a button to direct to the main recipe page. 

### Login & Register pages 
- The login and register pages follow the same design and format to align the pages. 
- The login page features a link below the login button to direct users to the register page should they find themselves on the wrong section, vice versa on the register page. 
- The register page features a "passoword" and "confirm password" feild, this is to ensure the user doesnt enter an incorrect password and lock themselves out of their account in future. 

### Recipe Page
- The recipe page features a search and find function at the top of the page. 
    - There is a search bar allowing users to search the page for recipes by recipe name
    - alongside the search bar there is a dropdown options list for the user to search recipes by category, "breakfast, lunch or dinner"
- The recipe page then features all the recipe cards listed, the recipe cards contain some key details like an image of the recipe, the recipe name, how many it serves, the time it takes to cook and a difficulty level. There is then a button on each card which directs to a full recipe page, with further details including, method, ingredients, prep time, cuisine type and a gluten free indicator. 
- The recipe cards will act the same as the cards on the home page, a registered logged in user will be able to view the full card, however, a non registered user will be encouraged to log in before being able to view the full recipe. 

### Add Recipe Page
- A logged in user will see an add recipe page, this page allows a user to add a recipe to the database to be viewed on the site. On this page there are all the fields needed to complete a full recipe card. This page contains a number of features:
    - A drop down to select the recipe category
    - A switch to signal if the recipe is gluten free or not
    - Both the method and ingredient files are listed as an array and each ingredient/method can be added or removed using the interactive add/remove buttons
    - An add image link

### Profile edit & delete recipe
- The profile page is available to a logged in user, they are first met with a small table showing the username and the number of uploaded recipes. 
- Underneath this there is then an option for the user to delete their profile should they need to, on clicking this there is added security of a pop up modal to confirm the user wishes to continue with this action
- The recipes the user has uploaded are then listed below, on the recipe cards there are two extra buttons "delete recipe" and "edit recipe". 
- On the user pressing delete recipe, similar to the delete profile a pop up modal appears to confirm the users actionsm should they go ahead the recipe is then deleted from the database
- The second button is to edit a recipe the user has uploaded. On clicking this the user is directed to a new edit recipe page, this is set up similar to the "add recipe" page, however the recipe details of that being edited are auto completed in the fields for ease of use. Once a recipe is edited the databse is updated with the new details. 

# Design 

# Skeleton
## Wireframes
My wireframes were created using [Balsamiq](https://balsamiq.com) wireframes and are detailed below:
- Mobile 
- Tablet
- [Desktop](https://olivergray03.github.io/MS3/wireframes/ExPlantaDesktopwireframes.pdf)

# Technology Used
Languages
- HTML
- CSS
- JavaScript
- Python

Libraries & Integrations
- Flask
- Jinja
- Materialize
- Font Awesome
- Google Fonts
- JQuery

Database
- MongoDB

Version control
- Git 
- Git Hub

Wireframes 
- Balsamiq

Other
- Heroku
- Google Dev Tools
- Responsinator
- Chrome lighthouse
- W3C Jigsaw

# Testing
## Testing User Stories

## Testing Performance

## Testing Functionality

## Further Testing

# Code Validation

# Deployment
## GitHub Pages

This project was deployed to Github pages using the following steps:

1. Log into Github 
2. Select the OliverGray03/ms3 respository
3. Click the settings tab at the top of the repository
4. Scroll to the "GitHub Pages" section of the page
5. Under "Source", click the dropdown called "None" and select "Master Branch"
6. The page will automatically refresh
7. The project has now been deployed. Scroll back to the GitHub pages section and click on the link above the source heading to view the live site.

## Forking the GitHub repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log into Github 
2. Select the OliverGray03/ms3 respository.
3. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button
4. You should now have a copy of the original repository in your GitHub account

## Making a clone to run locally

1. Log into GitHub
2. Select the OliverGray03/ms3  respository
3. Under the repository name, click "Clone or download"
4. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link
5. Open Git Bash
6. Change the current working directory to the location where you want the cloned directory to be made
7. Type "git clone", and then paste the URL you copied in Step 3

## Heroku App

# Credits
- My mentor Antonio Rodriguez who has provided me with guidance and support through the project
## Code
- Code Institutes task manager app walkthrough project for the basis behind CRUD functionality
## Media
- The image used for both the register and login page was sourced from [Vanesa Conunaese on Unsplash](https://unsplash.com/photos/JXow53j6AtE)
- The image used on the hompage was sourced from [Ella Olsson on Unsplash](https://unsplash.com/photos/2IxTgsgFi-s)

