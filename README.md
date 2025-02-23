# HeartHub 🫶🏻

To Do (After finishing the project, add here an image of how the main page looks like)

# SUBMISSION

## **Deployment**
* The platform is deployed using Heruko, making it accessible globally without additional hosting costs.
* Continuous updates and improvements are made to enhance the user experience and security.

[Click this link to view the Website.]() .... To Do...


## **Criteria**

Our team addressed these applicable criteria:

- ✨ Project is Full-Stack
- ✨ Project must be based on reality, inspired by Dating Webpages.
- ✨ Basic Readme.md in place

# **🧑‍💻 About the Submission**


## **Intro**

Welcome to Heart Hub 🫶🏻 a dating web app built to connect people in a straightforward and reliable way. Inspired by the idea of “Love.exe – Coding connections in the digital age,” Heart Hub uses modern technology and smart matchmaking to help users find genuine relationships. We focus on creating a platform that’s user-friendly, safe, and accessible for everyone.


## **Goal**

Our goal is to redefine online dating by developing a service that emphasizes inclusion, safety, and simplicity. We aim to use innovative algorithms and clear design to ensure that every user has a smooth experience while finding meaningful connections in a secure digital space.

## User Stories


#### 1. Registration
**As a user**, I can sign up for the application so that I can start using the application.

**Acceptance Criteria:**
1. User signs up with valid email and strong password
2. User gets feedback on screen if signup is successful or not
3. User gets redirected to the Login page if signup is successful

#### 2. Sign In
**As a registered user**, I can log into the application so that I can access my account and use the features.

**Acceptance Criteria:**
1. User can enter email and password to login
2. User gets feedback if credentials are incorrect
3. User gets redirected to profile feed after successful login
4. User session is maintained until logout
5. User can request password reset if forgotten

#### 3. Log Out
**As a logged-in user**, I can log out of the application so that my account remains secure when I'm not using it.

**Acceptance Criteria:**
1. User can log out from any page in the application
2. User session is terminated upon logout
3. User is redirected to login page after logout
4. User cannot access protected routes after logging out

#### 4. Profile Feed
**As a logged-in user**, I can view a feed of profiles so that I can discover and connect with other users.

**Acceptance Criteria:**
1. User can view a list of other user profiles
2. Feed shows basic profile information (name, photo, status)
3. Feed updates automatically or can be manually refreshed
4. User can scroll through profiles with pagination
5. User can search/filter profiles based on criteria (gender, sexuallity, city, country)
6. User can like another profile
7. User can dislike another profile
8. User can use a special  filter that only shows users who liked their profile

#### 5. Profile Detail
**As a logged-in user**, I can view and edit my profile details so that I can maintain my information and customize my presence.

**Acceptance Criteria:**
1. User can view their complete profile information
2. User can edit their profile details (name, photo, bio, etc.)
3. User can see changes reflected immediately after saving
4. User gets feedback when profile updates are successful/unsuccessful
5. User can view other users' profiles in read-only mode

#### 6. Chat
**As a logged-in user**, I can chat with other users so that I can communicate and interact with them.

**Acceptance Criteria:**
1. User can start a new chat with another user
2. User can send and receive text messages in real-time
3. User gets notifications for new messages
4. User can see online/offline status of other users
5. Chat history is preserved between sessions
6. User can see when messages are read/delivered


## Postponed till next Iteration
The initial goal was to implement a live private messaging system using **Channels** and Websockets. The idea got discarded due to complexity, that would jeopardize the goal of dilivering before the dead line. 

This feature can be implemented in the next iteration, though. 

## UX 
### Colors
-  Incorporate a palette of four colors.
To Do .... 

### Typography
- font...... To Do

### Imagery
![Logo](./staticfiles/images/logo_2.png)

## Wireframes

![About](./frontend/src/assets/wireframes/About.png)

![About](./frontend/src/assets/wireframes/About.png)

![About](./frontend/src/assets/wireframes/About.png)

![Profile](./frontend/src/assets/wireframes/Profile.png)

![SignIn](./frontend/src/assets/wireframes/SignIn.png)

![SignUp](./frontend/src/assets/wireframes/SignUp.png)

## System Design

### Entity Relationship Diagram for Chat Application

This ERD represents a simplified model for a chat application with public and private chat rooms, user profiles, and file attachments.

```mermaid
erDiagram
    User {
        int user_id PK
        string username
        string email
        string password_hash
        datetime created_at
    }
    UserProfile {
        int profile_id PK
        int user_id FK
        string display_name
        date birth_date
        boolean is_online
        text bio
        string avatar_url
        string gender
        string sexual_orientation
        string country
        string city
        string contact
        string intrests
        json other_details
        datetime created_at
        datetime updated_at
    }
    Match {
        int match_id PK
        int user1_id FK
        int user2_id FK
        datetime matched_at
        boolean blocked
        int blocked_by FK
    }
    %% blocked_by: user_id of the user who initiated the block
    
    Likes {
        int like_id PK
        int source_profile_id FK
        int target_profile_id FK
        boolean read
        datetime liked_at
    }
    %% read : signifies whether or not the targeted user has read the notification

    Dislikes {
        int dislike_id PK
        int source_profile_id FK
        int target_profile_id FK
        datetime liked_at
    }


    User ||--o{ UserProfile : has
    UserProfile ||--o{ Likes : one_to_many
    UserProfile ||--o{ Dislikes : one_to_many
    UserProfile ||--o{ Match : many_to_many   
```


## **💻 Tech Stack**
This platform is built using modern web technologies to ensure accessibility, responsiveness, and ease of use:
* HTML: For structuring the content of the website.
* CSS: For styling and visual enhancements.
* React: To enable dynamic interactivity and functionality.
* Django REST Framework: Used for ... To Do.
* Bootstrap: A front-end framework to ensure a mobile-friendly and responsive layout.


## Features


## Testing 


## Validation

1. W3C Markup Validator ( [Results]() )
    - To Do ...
    
1. W3C CSS Validator ( [Results]() )
    - To Do ...

1. Jshint javascript validator ([Results]())
    - To Do ..


## Performance

The website performance was examined using the [Google Lighthouse](https://developers.google.com/web/tools/lighthouse/)

Click on [Results]() to view the performance.... To Do

## Credits

1. Resources used : 
    -  https://github.com/aop4/heroku-django-REST-template

# Team members

- **Many thanks to the team members for the hard work and cooperation.**

  - **Warren Smith** - [GitHub](https://github.com/Wxrren), [LinkedIn](https://www.linkedin.com/in/warren-smith-b43b20183/
  )
   Design/ Development / Documentation

  - **Nazek Altayeb** - [GitHub](https://github.com/Nazek-Altayeb), [LinkedIn](https://www.linkedin.com/in/nazek-a-altayeb/)
   Design/ Development / Documentation

  - **Dimitri** - [GitHub](https://github.com/dimitri-edel),
   Design/ Development / Documentation

  - **Laurie** - [GitHub](http://github.com/lmcrean),
   Design/ Development / Documentation

  - **Allan** - [GitHub](https://github.com/Allano256),
   Design/ Development / Documentation

   - **Hira** - [GitHub](https://github.com/hirakhan95),
   Design/ Development / Documentation



# Contribution


# Contact & Support
=======
