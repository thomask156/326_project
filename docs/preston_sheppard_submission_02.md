I created the init.py script for our project. It generates users, their profiles, 
and creates chat messages in the global chat lobby for each of them.
It also creates an argument for each generated user and adds a few participants to each.
I made the init file into a django management command and added it to argue-app/management/commands/configure_argue.py.
This allows us to easily run the command from within the django app, and have access to many features that only run when the django server is running.

I created the inheritance structure for our templates so that each of our pages would extend the base page,
and I created a navbar and added it to the base.html template to allow for easy navigation around the site.
I streamlined the styling of each of the pages and unified the way static assets are loaded on each page.

I added the django auth module to our project, created a postsave to automatically create profiles when users are created,
added login validation to all of the necessary pages, and added form error displays which show when the user has submitted a form incorrectly.

I spent my remaining time helping other members of the group create the forms, views, templates, and models for their pages.