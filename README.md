# The Hiking Journal

=== Author ===

Jenna Waffensmith | https://github.com/jwaffensmith | https://www.linkedin.com/in/jennawaffensmith/


=== Overview ===

The Hiking Journal is a place for users to log all their hiking adventures. Why? With all the hikes in Washington State, the developer and her friends often forgot the hikes they conquered, the hikes they loved and the hikes that left them saying, "never again". Inspired by her friend’s diligent recordkeeping of their hikes on a spreadsheet to solve this very problem, the idea of building a digital hiking journal was born. 

=== Application Website ===

https://thehikingjournal.herokuapp.com/

=== Technologies ===

* Python
* Django
* SQL
* Postgresql
* DTL
* Javascript
* Sass
* CSS
* HTML
* Bulma
* Docker & fly.io

=== Installation ===
* Postgres
* Python environment (e.g. Anaconda )
* Install Django globally
* If using Anaconda, run command `conda activate djangoenv`
* Ensure postgres is running, e.g. `brew services start postgresql` 
* Create db in PostgresSQL named `hikeapp`
* Set up `.env` file. Use the .env.example file in the `hike_project` directory as a reference. 
* `pip install -r requirements.txt` in root directory to install dependencies (e.g. django_filters)
* Migrate models into db by running `python3 manage.py migrate` in root directory
* To run server, `python3 manage.py runserver`
* App should be running on `http://localhost:8000`

=== User Stories ===

    == Navbar ==
    * There is a fixed navbar at the top of each page with The Hiking Journal logo and name on the left. When a user is not authenticated, signup and login links are on the right, along with the About page link.
    * Once users are authenticated, the right-hand side of the navbar has links to the user's journal (profile page), site-wide search page and log out.

    == Landing Page ==
    * Footer displays developer’s name with links to GitHub and LinkedIn
    * Landing page displays a welcome message that directs users to login or register for an account with links to each page.

    == Auth ==
    * Registration page asks users for name, chosen username, chosen profile photo, first name, last name, email and password. Once data is validated, the user is authenticated and can access their profile and the feature of a site-wide search of hikes and other users.
    * Log in page has a sign-in form with the option to reset password. The reset password option will send the user an email from The Hiking Journal gmail account with a link to reset password if the user has an email in the database. 

    == Profile Page ==
    * On the user's profile page, the user sees any previously created posts. Posts are organized from newest to oldest.
    * A button to add a hike directs the user to the create hike page.
    * To create a hike, the user fills out a form with hike details and the option to add up to three photos. If they do not post a photo, a default photo will display.
    * Each post will display photos, name of hike, location of hike, post date, and any comments the user has added to the post. 
    * User can click on the post photo or “Review Hike” link to view the hike detail page with additional hike details. 
    * For any comments left by other users, the user can click “view Comment.” This link directs the user to the comment detail page where they have the option to delete the comment by clicking the “Delete” button. A modal pops up asking the user to confirm if they want to delete. 
    * User can update their account by clicking the "Update Account" button where they can update their username, name, location, email, avatar photo and password.
    * On the profile page, the user can click the “Search Your Hikes” link to filter their hikes. 

    == Sort Hikes Feature ==
    * On the hike sort page, user's can filter and search the posts they have created. They can filter by name, hike date range, hike rating, elevation gain, and length of hike.

    == Hike Detail Page ==
    * On the hike detail page, there is an “Edit” button that the user can click to edit the hike. A modal pops up with the hike edit form. 
    * On the hike detail page, there is a “Delete” button that the user can click to delete the hike. A modal pops up that confirms if the user wants to delete.

    == Site-wide Search Feature ==
    * A site-wide search link is located on the right-side of the navbar. This link directs the user to a search page for hikes and users. 
    * Users can search for other users’ hike posts by hike name or they can search for other user’s by their first name/last name or full name.
    * Results of the search will display in corresponding columns. Hikes will display under the hike’s column and users will display under the user’s column. 
    * Users can click on the corresponding photo cards to see the hike details page or click on the user to see their public profile. 

    == Viewing Other User's Profiles ==
    * On a user’s public profile, the user has an option to leave a comment on posts. 
    * User’s can view their previously left comments by clicking, “View Comment.” This link directs the user to the comment detail page.

    == Comment Detail Page ==
    * On the comment detail page, there is an “Edit” button that the user can click to edit the comment they created. A modal pops up with the comment edit form. 
    * On the comment detail page, there is a “Delete” button that the user can click to delete the comment. A modal pops up that confirms if the user wants to delete.

=== Wireframes ====

https://www.canva.com/design/DAEo6vE2LrE/view?utm_content=DAEo6vE2LrE&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink

=== Entity Relationship Diagram (ERD) ===

https://drive.google.com/file/d/10-D5nemBjS0S3v32-H5eQgxUAzv3XaDH/view?usp=sharing

=== Future Features ===

* Users can upload images
* Users can reply to other user's comments
* Distance fields added to hike model for elevation gain and hike length
* A map API to provide a visual map for hike locations

