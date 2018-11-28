## Mark Disler - Submission #3

For Phase #3 of this project, I continued work on the Profile screen – adding buttons for starting a new argument and for editing your first and last name, as well as your bio.  I created a new form that has three fields – first name, last name, and bio.  Once submitted, it will update the User object and the Profile object with the new information.  I also added a url for redirection at edit_profile/ in order to get to the EditProfileView containing the form.

We had worked on authentication earlier in the semester, but I had worked on linking each User with a Profile object that gets created when a user makes an account.  Users are created with a random name (based on animals) to keep anonymity and if the user wants to, he/she can now change that name with the form that I made in this phase.  I have a list of animals and one is picked at random when the user is created.

Lastly, I populated the profile template with the first and last name, bio, and the recent arguments that the specific user has been involved in.
