# Team Master Hackers

## Overview
Our website allows users to sign up, log in, and view their profile. From there, they can create an argument with a desired topic, name, and description, or they can join an existing argument.
We have not implemented the page where the argument takes place, so redirects that would send users to the argument page instead redirect to the profile page.
We have also implemented a global chat page where people can discuss outside of arguments. This chat template will be the basis of the argument page once we create it.

## Team Members

Team Master Hackers and their GitHub Names:

Travis Bender ([travisbender](https://github.com/travisbender))  
Mark Disler ([markdisler](https://github.com/markdisler))  
Thomas Katz ([thomask156](https://github.com/thomask156))  
Preston Sheppard ([psheppard16](https://github.com/psheppard16))  
Seth Tinglof ([seth-tinglof](https://github.com/seth-tinglof))  

## Video Link
https://youtu.be/NmL1yaNTvbI

## Design Overview
#### Users and profiles:
When a user first signs up, we use the django auth app to create their user.
There is a post save signal connected to the user model that creates a profile for them automatically.
Users can then view their profile information at argue/profile/, which makes a get request to the ProfileView, 
which queries their profile based off of the logged in user, and then passes it to the pages/profile.html template.
Here, the user can view their profile information, such as their description, their name, and the arguments they are in.


#### Chat Messages and Chat Lobbies:
Each chat message has what you would expect: a message, a timestamp, and a user who wrote it.
But each message also have a foreign key to a ChatLobby. 
This is because we want several chat lobbies on our site, and this allows ChatMessages to be associated with a single lobby.
We currently interact with the ChatMessages through the global chat lobby page at argue/chat/.
When a user enters a message and presses submit, we make a post request to the ChatView, which creates a new ChatMessage and point it at the global ChatLobby.
When a user makes a get request to the ChatView, we display the template at pages/chat.html, which shows a list of all the ChatMessages pointing at the global ChatLobby.

#### Arguments, Topics, and Statuses:
Statuses and Topics simply contain a name field. These are used as options for the Argument model.
Arguments are the most complicated model on our site. Several fields are edited by the user when they make a post request to argue/create_argument/.
These fields are argument_name, topic, max_participants, and description. These fields are sent to a form which creates an argument instance.
We populate the status, last_updated, creator, and chat_lobby fields.
A post save signal which is connected to the Argument model then automatically adds the creator to the list of participants.
When a user then visits argue/argument_list/, a list of arguments including their newly created argument is displayed.

## Problems And Successes

Problems consisted of finding the best time for our team to meet and where that would be. 
Furthermore, there is a large difference in terms of expertise with django, and web development in general, among the group. 
While this is not necessarily a problem, a large part of the group had to spend some time learning the environment. 
There were plenty of successes: Preston took lead of the group and assigned everyone a model and view to work on, and was always eager to help someone out if they were stuck. 
We were all able to complete our pages and understand the webapp. Those who were less experienced now have a far greater grasp on django and more confidence going into the next leg of the project. 

In terms of improvement, there isn't much to be done. We could meet even earlier to work on the project, 
but as of now this isn't a striking issue. We have great vision as to what we want to accomplish and we might even look into adding more features before the project is complete.