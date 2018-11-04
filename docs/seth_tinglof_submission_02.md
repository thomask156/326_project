For this project my primary responsibility was to create the argument/lobby creation page. To do this, I needed
to create the argument, status, and topic data models. I had to work with my teammates to craft an argument model that
would be usable for every page across the application as well as work with Mark to create a relationship between
arguments and profiles and Thomas to make a relationship with arguments and chat lobbies. Preston also helped and
made some changes to this data model. We went through a few iterations for what data models we needed for arguments.
Initially, I was working on a "create lobby" page that would make a separate lobby and argument data model, but we
realized that it was unnecessary to separate these two concepts. We decided to change my page to "create argument"
then we combined these two data models into an argument data model, and I let Thomas handle the chat lobby data
model (which is different from the lobby data model that I originally intended).

I created the forms, both HTML forms and Python/Django form classes, to pull data from html template to create arguments 
in the database whenever someone uses the create argument page. I also made the create argument page display the topics
from the database in the topics drop down

I finished my page fairly quickly, so I also worked to help some of my group members with their pages. I helped maintain
the git repo and fixed some mistakes when one of my teamates made a bad commit (I had to quickly learn how to revert a
merge commit). I also solved some database migration issues that arose when two people committed data model changes
at the same time. Finally I took some responsibility for arranging our team's meeting and (hopefully) ensuring that
we upload everything we need.
