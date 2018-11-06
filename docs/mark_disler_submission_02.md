For Phase #2 of this project, I worked on the Profile screen which is the intended to be the main landing page after you log in.  The profile screen has a profile picture, your name, a bio, any trophies you've earned, and a list of all arguments you've participated in.  I wrote the template which will insert all of that information based on the Profile context.  I wrote views.ProfileView which gets all of the arguments that a person is tied to and then creates a context with that user, their profile, and all of their arguments and then renders the template.  

In addition, I wrote the Profile model which stores the bio, your rank and a one-to-one relationship with the User – as each User should have a profile tied with that account.  I also wrote the Argument model (which was later added to by other people working on other things).  It has a few attributes like name, last_updated, and max_participants, and also has a lot of relationships with other model entities that other people created.

Lastly, I created the data model diagram in Xcode's modeling interface for the submission.  It has a list of all the attributes for each model entity and all of the relationships that exist in our data model. 





