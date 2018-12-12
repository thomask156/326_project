# Team Master Hackers

## ChangeMyMind.Org

Fall 2018



## Overview

Our application serves as a meeting point of all those who want to pointlessly argue over the internet. Our users will login and immediately find a topic and a person to argue with through the power of the internet and our website combined. Users will have a ranking which will be a badge showing not only how argumentative they are but how often they "win" their arguments as well. Our application is innovative in the sense that we help remove these sorts of derailing conversations from other forums and aggregate them here.



## Team Members

Travis Bender, Mark Disler, Thomas Katz, Preston Sheppard, Seth Tinglof



## User Interface
The first view that our users will see when accessing our site is the login page
![alt text](https://github.com/thomask156/326_project/blob/master/docs/imgs/final%20page%20screenshots/login.png "Login Screen")
This is the page that allows new users to sign up and old users to login.

After logging in, users will be greeted with their profile page.
![alt text](https://github.com/thomask156/326_project/blob/master/docs/imgs/final%20page%20screenshots/profile_screen.png "Profile Screen")
The profile screen has a list of all the recent arguments that this user has created, and it has links to quickly access these arguments.There is also a button to edit the profile, and the sidebar displays all recent arguments.

Next we get onto the edit profile page.
![alt text](https://github.com/thomask156/326_project/blob/master/docs/imgs/final%20page%20screenshots/edit_profile.png "Edit Profile Screen")
This is the page that you see if you click the pencil icon to the right of your name on the profile screen. Here you can edit your first and last names or your bio. By default, your first name will be anonymous, and your last name will be some random animal, but you can change these if you do not wish to be aonymous during your arguments.

Next, we will look at creating an argument on the start argument page.
![alt text](https://github.com/thomask156/326_project/blob/master/docs/imgs/final%20page%20screenshots/create_argument.png "Start Argument Screen")
This page is fairly self explanitory. You can write an argument name and description in the appropriate fields. Then, you can select your topic and argument size from the dropdowns. Finally, hit start argument to create your argument.

Once an argument is created, it is visible in the join argument page.
![alt text](https://github.com/thomask156/326_project/blob/master/docs/imgs/final%20page%20screenshots/join_argument.png "Join Argument Screen")
On this screen, every argument that has been created is displayed, and you can click join on any of these arguments to enter that arguments chat.

Finally, the chat is where the arguments actually happen.
![alt text](https://github.com/thomask156/326_project/blob/master/docs/imgs/final%20page%20screenshots/chat.png "Chat Screen")
There is a global chat that you can access by clicking on "Chat" in the navbar, and every argument has a chat that you access by joining that argument. On this page, simply write a message and click submit to let everyone know what your opinions are. Every chat message includes the username of its poster and a timestamp for its creation.


## Data Model

![Data Model Below](https://github.com/thomask156/326_project/blob/master/docs/data_model.png)

Above is our data model for our web application. Profile inherits user's attributes, which has a name, password and email field, and then profile adds on a bio and rank field. Arguments have the attributes such as their name, a description, last time it was updated, and max number of participants. It has relations to participants (profiles), the creator (profile), the chat lobby and the status and topic models. Status and topic both only have one attribute, these being their name, and arguments get these attributes from these two models. A chat message has fields for its writer,  the time it was sent, which lobby it was sent in and what the message was. Each chat message is only sent to one lobby, this being the chat lobby model. This model only has a name attribute and is used for "housing" groups of chat messages.

## URL Routes/Mappings

| URL                                                          | Description                                |
| ------------------------------------------------------------ | ------------------------------------------ |
| url(r'^create_argument/', ArgumentCreateView,name='create_argument') | Used for creating argument                 |
| url(r'^argument_list/', ArgumentListView, name='argument_list') | Used for seeing all ongoing arguments      |
| url(r'^profile', ProfileView, name='profile')                | Used for reaching profile of specific user |
| path('chat/<int:chat_lobby_id>/', ChatLobbyView, name='chat_lobby') | Used for reaching specific chat lobby      |
| url(r'^global_chat/', GlobalChatView, name='global_chat')    | Used for reaching global chat page         |
| path('argument/<int:argument_id>/', ArgumentView, name='argument') | Used for going to specific argument        |
| url(r'^edit_profile/', EditProfileView, name='edit_profile') | Used for editing user's own profile        |
All routes above have the @login_required decorator, which means they cannot be accessed unless a user is logged in. The only page accessible by non-authenticated users is /auth/login/, which is where the user can create an account login with an existing one.



## Authentication/Authorization

Authentication and authorization were handled by django's native authentication support, which checks if the inputted username and password were in the database. Django also makes sure that people can't create a new account with an already existing name and with the use of the login decorator, users cannot access any page beyond the login screen unless they enter valid credentials. Every user has the ability to create an argument, chat in an argument and edit their profile. 

## Team Choice

For our final submission, we decided to add a functional friend activity panel which is viewable on the profile page. This involves creating a new model for friend activity and loading this list onto the profile page for each user. 



## Conclusion

Overall, our team was very efficient while working on this project. We always made sure that we finished our work ahead of schedule and that we met any requirements we set out for ourselves. Most of us learned a lot about django and its website building tools, and those who already knew a lot were able to pass their knowledge on. Difficulties included finding meeting times and learning about django, as well as setting up the virtual environment, which was a long process which had to be repeated if one were to make an error in setting it up or they needed to reset it for other reasons. Successes included everyone learning an ample amount about Django as well as models and forms provided by django, and how those worked in our database relations. Things we would have liked to know at the beginning of the semester included due dates of each project and the requirements. If these were set out beforehand, our group could have made sure we did enough work for the next leg of the project without worrying about any potential time constraints. It would also have been nice to know we were given a limited amount of time to come up with our website idea.  
