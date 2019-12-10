<div align="center">
  <img src="https://i.ibb.co/n7fhZ2y/Terrie-Homes.png" href="https://terrie-homes.herokuapp.com/" target="_blank" rel="noopener" alt="Terrie Homes Logo" aria-label="Terrie Homes Logo" />
</div>
<div align="center">
    <img src="https://i.ibb.co/W6297nY/responsive-terrie-homes-pic.png" href="http://family-hub-nl.herokuapp.com" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>
<br>

<div align="center">  

[Terrie Homes](https://terrie-homes.herokuapp.com/) is an app designed to help people sell their house online, help potential buyers access listings and help an agent easily facilitate the sales. 
<br>

[Launch the app!](https://terrie-homes.herokuapp.com/)
</div>



## Table of Contents
1. [**UX**](#ux)
    - [**Developer Goals**](#developer-goals)
    - [**User Stories**](#user-stories)
    - [**Stakeholders**](#stakeholders)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Remaining Features to Create**](#remaining-features-to-create)

3. [**Applied Technologies**](#appplied-technologies)
    - [**Libraries**](#libraries)
    - [**Languages**](#languages)

4. [**Testing**](#testing)
    

5. [**Deployment**](#deployment)
    - [**Running Locally**](#running-locally)
    - [**Heroku Deployment**](#heroku-deployment)

6. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Code**](#code)

7. [**Reflections**](#reflections)


## UX

### Developer Goals

The primary purpose of this page was to create a professional clean site that connects successfully to mongodb without the use of a css framework in order to strengthen my pure css knowledge and skills.

### Stakeholders

There are three stakeholders - The Agent(website owner) - The Seller - The Buyer

### User Stories

As a seller I want the following:

1.  Clear clean design that is aesthetically pleasing

2.  Create an account and have my own dashboard, and then login at any time.

3.  To upload a listing of a house to sell, also be able to edit, delete through the dashboard.

4.  Upload images for the house listing

4.  Work on all sized screens (Responsive)

5.  Simple Functionality


As the agent I want the following:

1.  Approve any listing that comes through before the user can submit it to the manin listings page.

2.  Recieve emails through the contact form and reply.

3.  Have links to Social Media Pages

4.  Have the ability to charge Sellers for each listing

As a otential customer I want the following:

5. Easily access the houses that are for sale and scroll through information and photos of them to then make contact if interested in purchasing.

### Design

**Fonts**

Primary font chosen was **Montserrat** to give a jungle feel to the game and ensure a fun theme is created.

Secondary font was **Esteban** which contrasts well with the primary choice of font but also allows a clearer 

**Images**

Minimal use of images to match the minimalistic professional design style.  Image for the house when a user uploads a listing is just a test image.

**Colour Scheme**

Again, selected to create a professional simple and clean finish.


### Wireframes

[Figma](https://www.figma.com/files/recent) was used to create the wireframes. 

[Desktop-Design](https://www.figma.com/file/bOf1wSzsj5LzE6vDAgHGVa/Terrie-Homes?node-id=0%3A1) can be viewed here.
[Mobile-Design](https://www.figma.com/file/bOf1wSzsj5LzE6vDAgHGVa/Terrie-Homes?node-id=69%3A1) can be viewed here.

## Features

### Current Features

1.  Ability to sign up to an account and login.

2.  Ability to add a house listing through a user assigned dashboard.

3.  Able to select different pages using the navbar, which responsively adjusts into dropdown menu.

4.  Employs basic CRUD functionality as user can create, read, update and delete their listing.

5.  User can simulatenously create their listing in their dashboard and list it on a global listing page. (i.e. it adds on both pages).  Currently once any user adds a listing it gets sent across to the listing page underneath the main callout


### Remaining Features to Create

There is much to finish on this site. I consider this to be a first stage of approximately a three stage development process.  The basic design is in place however a more features needed for it to align with the user stories listed above.

1. Add more features to the dashboard including an images upload section and a location API such as google to pinpoint location and a preview page before submitting for approval.

2.  Add a payment section for the user to process payment of their listing.

3. Add a carousel to the listings page (rather than a background image) which scrolls through sample listings.  Also wire up a separate 'enquire' button for the bottom of each listing when it is added.

4. A new page for the buyer to get more information about each listing when they click on that particular property on the listings page, such as more images of it, the location and higer detail of any other miscellaneous relevant information.

4. Implement the best back end and front end process for the user uploading and image and then iterating through the database and then rendering it automatically on the  listing page once approved by admin.  The user in the market for a house should have the ability to click on the listing and get as much information as possible through a separate screen/link/route, such as flicking through the images which the selling user has submitted.

5. Rather than flash text implement modals to let the user know invalid logins and duplicated usernames on registration. Currently uses flash through flask which does not hit the intended final standard.

6. Create Social Media Pages and links

7. Wire up EmailJS for contact form.

8. Add much more content to the listings page. I plan to add the following:

* A carousel of sample listings beneath the main callout (rather than a background image)
* Add relevant photos for the each individual listing, which can be seen when scrolling down beyond the callout to bring up more information and images.
* Change the design so that half the page is callout and the listings can be seen as soon as you link to it.

## Applied Technologies

The following technologies were used to construct the site:

### Tools

* [Gitpod](https://https://www.gitpod.io/) - a lightweight but powerful cloud based editor linked through Github. 
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database for this project.
* [Git](https://git-scm.com/about) to handle version control.
* [GitHub](https://github.com/) to store and share all project code remotely. 
* [Am I Responsive](http://ami.responsivedesign.is/) to create the image in this readme file.
* [imgbb](https://imgbb.com/) to host the logo for this readme file.
* [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.

### Libraries
 
* [Google Fonts](https://fonts.google.com/) - used to style the website fonts.
* [FontAwesome](https://fontawesome.com/) - CDN for Icons.
* [GitHub](https://github.com/) to store and share all project code remotely.
* [PyMongo](https://api.mongodb.com/python/current/) to facilitate communication between Python and MongoDB.
* [Flask](https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages.
* [Jinja](http://jinja.pocoo.org/docs/2.10/) a web template engine to simplify displaying data from the backend.


### Languages

* HTML - Created a file called `index.html`
* CSS - Created a file called `style.css`
* Javascript - Created a file called `app.js`
* Python - Created a file called `run.py` and `env.py`

## Testing

Testing information can be found in separate [testing.md](testing.md) file

## Deployment

### Running locally

To run this project on your own IDE locally follow the instructions below:

Ensure you have the following tools: 
- An IDE (such as VS Code or Atom)

Install the following
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) with an up and running account

### Instructions
1. Save a copy of the github repository located at https://github.com/lesreddy/Terrie-Homes 
    * click the "download zip" button at the top of the page and extracting the zip file to your chosen folder.
    * If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/lesreddy/Terrie-Homes
```

2. Open a terminal session in the unzip folder or change directory to the correct location.

3. Use a virtual environment  the Python interpreter, to use Pythons built in virtual environment enter the command:
```
python -m .venv venv
```  

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_The above commands may differ depending on your operating system, please check the [Python Documentation](https://docs.python.org/3/) for more info_

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `Terrie-Homes`, with 2 collections called `for_sale` and `users`.

8. You can now run the application with the command
```
python run.py
```

## Heroku Deployment

1. Firstly, clone the github repository https://github.com/lesreddy/Terrie-Homes and open it up in your chosen IDE.

2. Sign up to a new Heroku account and create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the `New` button in your dashboard. Give it a name and set the region to Europe.

3. From your newly created app in heroku click on `settings` from the menu and locate your `Heroku Git Url`. Copy it to clipboard.

4. From the terminal in your IDE type in `heroku login` and ensure to login to heroku, you may have to hit any key and then click on the link or hit `Ctrl C` to do so.

5. From the terinal paste in your `Heroku Git Url` and type `git remote add heroku` before it such as the example here and hit enter, this will link your git repository to heroku:
```
git remote add heroku https://git.heroku.com/your_app_name.git
```
6. From the terminal of your workspace Create a `requirements.txt` file using the terminal command
```
pip freeze > requirements.txt
```

7. Create a `Procfile` with the terminal command:
```
 echo web: python run.py > Procfile
 ```

8. Start a web process from your terminal by typing:
```
heroku ps:scale web=1
```

9. Commit your files git using '`git add .` and then `git commit -m` then from the terminal type `git push heroku master`, which will push your repository to heroku.

10.  Open up heroku newly created heroku app and then in the dashboard click `settings` and then click the `Reveal Config Vars` button

11. Set the following config vars:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000

12. In the heroku dashboard, click `Open App` Box

13. The site is now successfully deployed.

## Credits 
 
### Media

* Images were taken from [Pexels](https://www.pexels.com/).  
* [Tinypng](https://tinypng.com/) was used to compress images from high res state to maintain quality.
* [Affinity Photo](https://affinity.serif.com/en-gb/photo/) was also used to re-size images down for implementing onto [ImgBB](https://imgbb.com) for this readme file.

## Code 

* Code for navbar was referenced from [DevEd](https://www.youtube.com/watch?v=gXkqy0b4M5g)
* Code for Sign Up form was referenced from [Julio Codes](https://www.youtube.com/watch?v=UhvVsc2sM4s)
* Code for login page was referenced from [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE&t=5s)


## Reflections

I realise this site is far from finished but I have very much enjoyed my first venture something close to a full stack site.  On reflection, probably not the wisest call to strengthen my CSS but I am definitely much stronger with it after this project (along with all the other technologies used) but for the next project I think I will implement the bootsrap wireframe to complete the rest of the features in a much faster timeframe and a much more complete result.  Overall happy to successfully create my first site that links to a database successfully.
