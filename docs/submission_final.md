# Team Master Hackers

## ChangeMyMind.Org

Fall 2018



## Overview

Our application serves as a meeting point of all those who want to pointlessly argue over the internet. Our users will login and immediately find a topic and a person to argue with through the power of the internet and our website combined. Users will have a ranking which will be a badge showing not only how argumentative they are but how often they "win" their arguments as well. Our application is innovative in the sense that we help remove these sorts of derailing conversations from other forums and aggregate them here.



## Team Members

Travis Bender, Mark Disler, Thomas Katz, Preston Sheppard, Seth Tinglof



## User Interface



## Data Model

![Data Model Below](C:\Users\Thomas\PycharmProjects\326_project\docs\data_model.png)

Above is our data model for our web application. Profile inherits user's attributes, which has a name, password and email field, and then profile adds on a bio and rank field. Arguments have the attributes such as their name, a description, last time it was updated, and max number of participants. It has relations to participants (profiles), the creator (profile), the chat lobby and the status and topic models. Status and topic both only have one attribute, these being their name, and arguments get these attributes from these two models. A chat message has fields for its writer,  the time it was sent, which lobby it was sent in and what the message was. Each chat message is only sent to one lobby, this being the chat lobby model. This model only has a name attribute and is used for "housing" groups of chat messages.

## URL Routes/Mappings



## Authentication/Authorization

Authentication and authorization were handled by django's native authentication support, which checks if the inputted username and password were in the database. Django also makes sure that people can't create a new account with an already existing name and with the use of the login decorator, users cannot access any page beyond the login screen unless they enter valid credentials. Every user has the ability to create an argument, chat in an argument and edit their profile. 

## Team Choice

For our final submission, we decided to add a functional friend activity panel which is viewable on the profile page. This involves creating a new model for friend activity and loading this list onto the profile page for each user. 



## Conclusion

Overall, our team was very efficient while working on this project. We always made sure that we finished our work ahead of schedule and that we met any requirements we set out for ourselves. Most of us learned a lot about django and its website building tools, and those who already knew a lot were able to pass their knowledge on. Difficulties included finding meeting times and learning about django, as well as setting up the virtual environment, which was a long process which had to be repeated if one were to make an error in setting it up or they needed to reset it for other reasons. Successes included everyone learning an ample amount about Django as well as models and forms provided by django, and how those worked in our database relations. Things we would have liked to know at the beginning of the semester included due dates of each project and the requirements. If these were set out beforehand, our group could have made sure we did enough work for the next leg of the project without worrying about any potential time constraints. It would also have been nice to know we were given a limited amount of time to come up with our website idea.  