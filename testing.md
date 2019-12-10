## Testing

- [**User Stories**](#user-stories)
- [**Validation**](#validation)
- [**Pages**](#pages)
- [**Responsiveness**](#responsiveness)
 - [**Bugs**](#bugs)


### User Stories

See below for the current testing results of intended user stories:

As a seller I want the following:

1.  Clear clean design that is aesthetically pleasing.

    * Yes this is achieved

2.  Create an account and have my own dashboard, and then login at any time.

    * Yes this is achieved

3.  To upload a listing of a house to sell, also be able to edit, delete through the dashboard.

    * Yes achieved but with more features left to create (such as image upload and location API  and a preview)

4.  Upload images for the house listing

    * Not yet achieved

4.  Work on all sized screens (Responsive)

    * Yes achieved

5.  Simple Functionality

    * Yes achieved

As the agent I want the following:

1.  Approve any listing that comes through before the user can submit it to the manin listings page.

    * Not yet achieved 

2.  Recieve emails through the contact form and reply.

    * Its wired up but not actually going anywhere yet, want to do this with emailjs

3.  Have links to Social Media Pages

    * Not yet achieved

4.  Have the ability to charge Sellers for each listing

    * Not yet achieved 

As a potential customer I want the following:

5. Easily access the houses that are for sale and scroll through information and photos of them to then make contact if interested in purchasing.

    * Yes achievd but do want more info available when the listing is clicked on

### Validation

* Ran [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate the css file and also [W3C Markup Validation Service](https://validator.w3.org/) to validate the html markup.

### Pages

#### Landing Page

Biggest challenge on this page was ensuring the image was the right size and responsive for all sizes, eventually chose to remove it for small screens.  Tests included ensuring the two buttons were linked correctly and the navbar links were all working.

1. Go to home page
    i)  Click on `Terrie Homes` Logo
    i)  Click on `Home` Navbar link.

Toyed with the idea of just using the logo link but after researching best practises re-instated Home link in navbar.

2. Go to listing page
    i.)  Click on `Houses for sale` button.
    ii.)  Alternatively click on 'listings' in the navbar.

3.  Go to Sign In page
    i)  Click on `Sign In` in navbar.

4. Go to Register Page
    i) Click on `List your house` button.
    ii)  Alternatively click on 'Register' in the navbar.

5. Go to Contact Page
    i) Click on `Contact` in Navbar.


#### Listings Page

1.  Enquire about any of the listings:
    * Click on `enquire` button in the middle of callout.
    * Click on `contact` in navbar.

2.  View all listings from the database:
    *  Scroll down from main listings page


#### Sign In Page

Main challenges here was the design of the css login section it was referenced from a another coder (see credits.
Also the wiring up of the backend was a significant challenge and can also be credited to another tutorial (see credits).

1. Use a user name and password to sign in:
    * Click on `Username` placeholder and type in username.
    * Click on `Password` placeholder and type in password.

2. If user does not have username and password:
    * Click on `Register` in navbar or Click on `Register` Sign In box and it will direct to registration page.

3. If MongoDb cannot locate username or password it flashes up:
    * `Invalid! Please Try Again` in the center above the registration box.

#### Registration Page

Main challenges similar to Sign In Page refer above.

1. Create account:
    * Click on `Username` placeholder type in any chosen word (required)
    * Click on `Email` placeholder put in email address (required)
    * Click on `Password` placeholder put in any chosen password (required)
    * Click on `Confirm Password` put and confirm chosen password (required)

2.  If Username already exists it flashes up:
    * `Username Taken! Please Try Again!` in the center above the registration box. 

#### Contact Page

Original plans here was to utilise emailjs for the backend, however, it is currently only setup with a flash message acknowledging when a user has made contact.

1. To send mail:
    * Type in name in `name` box
    * Type in email in `email` box
    * Type in message in `message` box.
    * Click `submit` button
    * Once clicked message flashes up: `Thanks { name } we have received your message!`

### Responsiveness

All pages are responsive and this was an excellent exercise in realising how much time is saved when using bootsrap or similar css wireframes which make responsiveness much easier.  I found it very beneficial in learning how to do this with pure css but it was a challenge, and in hindsight, too much of a time sink given I wanted to implement more features within the time I had.  In saying this, the knowledge improvement in flexbox did make it a worthwhile, although I will be in embracing all css frameworks for 
my next project to expediate the overall process. 

Physically the pages were tested on a laptop, a desktop with large screens, a samsung i7 phone, a huawei p30 pro lite phone and an iphone X without issues.  Otherwise they all looked fine on the different sizes available in google developer tools.

### Bugs

Many of the time consuming bugs or issues arose from my less than proficient CSS skills, I did manage to get through most of them.  There is still one that exists, when the app is loaded and you go to the listing page, the address renders in a small size font.  However once you login and click back to the page, the fonts are ok again.  Not sure why it is doing this, there may be an issue with the duplication of the for loop in the backend but not sure.  It only seems to do it with the heroku app as well.