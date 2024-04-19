# Kiddie Corner


Welcome to Kiddie Corner, a dynamic Django-powered website designed for effortless toy shopping. Here, users can easily navigate through our extensive collection, tailored for different age groups, ensuring a seamless shopping experience for every visitorThis intuitive interface allows users to explore toys suitable for various ages with ease.

# Table of Contents
- [Planning and Design](#planning-and-design)
    - [Target-Audience](#target-audience)
    - [Project-Goalss](#project-goals)
    - [User Stories and Epics](#user-stories-and-epics)
    - [Wireframes](#wireframes)
    - [Database Schema](#Database-schema)
    - [Typography](#typography)
    - [Colour Pallete](#colour-pallete)
- [Features](#Features)
    - [Navigation Bar](#navigation-bar)
    - [Homepage](#homepage)
    - [Footer] (#footer)
- [Testing](#testing)
    - [lighthouse](#lighthouse)
- [Deployment](#dployment)
   - [Heroku Deployment](#heroku-deployment)
   - [ElephantSQL Database](#elephantsql-database)
   - [Forking the Repository](#forking-the-repository)
   - [Cloning The Repository](#cloning-the-repository)
- [Tecnologies used](#technologies-used)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

I have included testing details in a separate document called [testing](TESTING.md).

# Planning and desigtn
## Target Audience
- Parents and Guardians
- Family Members and Relatives
- Individuals passionate about toys, collectors, or hobbyists
- Teachers, daycare providers, and educational institutions looking for toys for classrooms or childcare settings.
- Individuals looking for gifts for children's birthdays, holidays, or special occasions

## Project Goals
To develop an innovative and user-friendly online toy store platform that caters to various age groups, offering a curated selection of toys, while providing seamless functionality for both customers and shop owners to browse, shop, and manage products efficiently

## User Stories and Epics

-  As a **site user** I want  **to navigate through landing page** so that **i can easily access various sections**

## Wireframes
[Home-page-desktop](./docs/wireframes/home-page-desktop.png).
<details>
  <summary>Homepage - Mobile (click to expand)</summary>

![Homepage - mobile-wireframe](/docs/wireframes/home-page-mobile.png)

</details>

## Database Schema


## Typography


## Colour Pallete


# Features
## Navigation Bar 
The navigation  bar designed with bootstrap adapts seamlessly to different screen sizes, ensuring a consistent user experience across desktops, tablets, and mobile devices.
The navbar contains the business logo which links back to the homepage when clicked. There is also a Search bar that allows users to query the 'products' database. There are three icon links in the upper right of the navbar that link to the user favourites, user account/account management, and shopping bag features.The Menu Contains links to the Home, About, All Products, shop byu age, and special offers pages.

![navigation-Desktop](/docs/features/navigation-bar-desktop.png)

At smaller screen widths, the nav bar collapses into a burger-style dropdown menu to enhance user experience on mobile and tablet devices.

![navigation-mobile](/docs/features/navigation-bar-mobile.png)

## Delivery Banner

The website features a prominent delivery banner positioned at the top of the header section. This banner encourages users to spend more than €50 to qualify for free delivery on their orders.

![delivery-banner](/docs/features/delivery-banner.png)

## Homepage

The home page features a main background image to catch users eye, with a button placed in the middle of the banner. Clicking this button takes user to the All Products page. Below that there is Highlighted Features and under that section there's a section about us with a small description of the page. Additionally, users can find age-specific links that lead to toys tailored for different age groups..


![Homepage-Desktop](/docs/features/dekstop-home-1.png)

![Homepage-Desktop](/docs/features/dekstop-home-2.png)

<details>
  <summary>Homepage - Mobile (click to expand)</summary>

![Homepage - mobile](/docs/features/mobile-home-1.png)
![Homepage - mobile](/docs/features/mobile-home-2.png)
![Homepage - mobile](/docs/features/mobile-home-3.png)
![Homepage - mobile](/docs/features/mobile-home-4.png)

</details>






## Footer

# Testing
## Lighthouse


### Lighthouse testing

[Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test:

* Performance
* Accessibility
* Best Practices
* SEO.

Below are the Lighthouse test results for all pages


<details>
  <summary>lighthouse-Testing-Home-Desktop (click to expand)</summary>

![Footer-Desktop](./docs/testing/lighthouse/home-page-desktop.png)

</details>


<details>
  <summary>lighthouse-Testing-Home-Mobile (click to expand)</summary>

![Footer-Desktop](./docs/testing/lighthouse/home-page-mobile.png)

</details>


## Deployment

### Heroku Deployment

The project was deployed using [Heroku](https://id.heroku.com/login).

After account setup, deployment steps are as follows:

1. Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
2. App name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
3. Navigate to the settings tab and click **Reveal config vars**  and add the config vars necessary for the project:                       
 `DATABASE_URL`           (insert your own ElephantSQL database URL ) 
 `DISABLE_COLLECTSTATIC`  1 (temporary) 
 `SECRET_KEY`             (random secret key )                                  
 
Also make sure you create Procfile and requirements.txt file.

4. Navigate to the **Deploy** section by clicking the "Deploy" tab in the navbar, Select **GitHub** as the deployment method and click **Connect to GitHub**.
5. Find the repository wehich you want to deploy and click on **connect**.
6. Find button **Deploy Branch** at the bottom of page.
7. After clicking **Deploy Branch** button it will take few minutes to deploy site and you will have ability to view it  clicking on **view** button.

###  ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To set up a database, please follow these steps:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on **Create New Instance**.
3. Enter a name for the instance.(project name)
4. Select **Tiny Turtle (Free)** free plan.
5. The "Tags" field can be left blank.
6. Click **Select Region**.
7. Select a data center near you.
8. Click **Review**, make sure that all details are correct and then click "Create instance".
9. Once created, click on the new database name, where you can view the database URL and Password.


### Cloning the Repository

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/tamariam/restaurant-Tamariam)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
  `git clone https://github.com/tamariam/restaurant-Tamariam`  then press Enterr.

### Forking the Repository

To create a copy of the repository for viewing and editing without affecting the original repository you can fork the repository through the following steps:

1. In my repository[github repository](https://github.com/tamariam/restaurant-Tamariam) click on the "fork" tab in the top right corner.
2. Then click **create fork**  and it will fork the repository in your github account.


# **Technologies used**

* Python
  * The packages installed for the is project can be found in [the requirements.txt](requirements.txt)
* Django
  * Django was used as the python framework in the project.
  * Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
* Heroku
  * Used to deploy the page and make it publicly available.
* Heroku PostgreSQL
  * Used for the database during development and in deployment.
* HTML
  * HTML was the base language used to layout the skeleton of all templates.
* CSS
  * Custom CSS used to style the page and make the appearance look a little more unique.
* Javascript
  * I have used JavaScript to automatically hide displayed messages after a few seconds.
* Bootstrap 5.0.1
  * Used to style HTML and CSS
* Font awesome
  * All icons throughout the page.

  # Credits

* [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes.
* [lucid.app](https://lucid.app/users/login#/login) was used to create ERD
* The site was developed using [gitpod](https://www.gitpod.io/).
* [GitHub](https://github.com/) was used to store my repository.
* Responsive screenshot made using [amiresponsive.com](https://ui.dev/amiresponsive)
* [Article on writing good user stories](https://www.industriallogic.com/blog/as-a-developer-is-not-a-user-story/)
* [coolers.co](https://coolors.co/603f3f-a0acca-e4b67c-de9f13-000000) was used to generate color scheme.
* [eightshapes-contast grid](https://contrast-grid.eightshapes.com/) to check contrast of colours.
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* Images:
  * for all images used for site  taken from [pixels.com](https://www.pexels.com/) 
* Multiple videos sourced from youtube :
    * [django-wednesdays](https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy)
    * [Learn Django - Class-Based Views series](https://youtu.be/ScteNE1jB4g)
* General references:
    * [Stack Overflow](https://stackoverflow.com/)
    * [Code Institute Learning Platform](https://codeinstitute.net/)
    * [Django Documentation](https://docs.djangoproject.com/en/3.2/)
    * [Bootstrap Documentation](https://getbootstrap.com/)


# Acknowledgements

This site was developed as a fourth portfolio project for the [Code Institute](https://codeinstitute.net/global/) course in Full Stack Software Development. I would like to thank the following for all of the support throughout the development phase.

* The Code Institute community, including Tutor Support, Student Care and the Slack Community.
* My mentor, [David Bowers](https://www.linkedin.com/in/dnlbowers/) for providing me with advice throughout the development process.