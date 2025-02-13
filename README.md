# team-5



# Resources used:

https://github.com/aop4/heroku-django-REST-template


## Entity Relationship Diagram for Chat Application

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
        text bio
        string avatar_url
        string gender
        string sexual_orientation
        string country
        string city
        json other_details
        datetime created_at
        datetime updated_at
    }
    PrivateChatRoom {
        int room_id PK
        int user1_id FK
        int user2_id FK
        datetime created_at
    }    
    PrivateMessage {
        int message_id PK
        int user_id FK
        int room_id FK
        string message_text
        datetime sent_at
    }
    File {
        int file_id PK
        string file_name
        string file_type
        string file_url
        datetime uploaded_at
    }

    User ||--o{ UserProfile : has
    User ||--o{ PrivateMessage : sends
    PrivateChatRoom ||--o{ PrivateMessage : contains
    PrivateMessage ||--o{ File : may_have
   