# UX

To return to the main README click [here](/README.md)

- [UX](#ux)
    - [The Skeleton Plane](#the-skeleton-plane)
      - [Wireframe mock-ups](#wireframe-mock-ups)
  - [Home Page Wireframe](#home-page-wireframe)
  - [Post Detail Wireframe](#post-detail-wireframe)
  - [User Profile Page Wireframe](#user-profile-page-wireframe)
  - [Search Page Wireframe](#search-page-wireframe)
  - [Home Page](#home-page)
  - [Database](#database)
    - [Data Models](#data-models)
      - [User model](#user-model)
      - [Vehicle model](#vehicle-model)
      - [Comment model](#comment-model)

### The Skeleton Plane
#### Wireframe mock-ups

Home page: The home page provides the user with a clear understanding as to the purpose of the site. 
There is a clear call to action for the user to search for a vehicle post with the search bar at the top of the home page. 
I did not implement the search function or the user profile, as these were not required for the MVP PP4 criteria.
The welcome message is clearly visible to the user when they first see the site, using any device.

Initial public images were sourced from https://www.pexels.com/search/car/

## Home Page Wireframe
I did not implement the search function or the user profile, as these were not required for the MVP PP4 criteria.
To return to the main README click [here](/README.md)
* [Back to top of UX.md](#ux) 

![Home Page Wireframe](/assets/wireframes/homepage-wireframea.png)

## Post Detail Wireframe
I did not implement the search function or the user profile, as these were not required for the MVP PP4 criteria.
To return to the main README click [here](/README.md)
* [Back to top of UX.md](#ux) 

![Post Detail Wireframe](/assets/wireframes/homepage-wireframeb.png)

## User Profile Page Wireframe
I did not implement the search function or the user profile, as these were not required for the MVP PP4 criteria.
To return to the main README click [here](/README.md)
* [Back to top of UX.md](#ux) 

![User Profile Page Wireframe](/assets/wireframes/homepage-wireframec.png)

## Search Page Wireframe
I did not implement the search function or the user profile, as these were not required for the MVP PP4 criteria.
To return to the main README click [here](/README.md)
* [Back to top of UX.md](#ux) 

![Search Page Wireframe](/assets/wireframes/homepage-wireframed.png)

## Home Page
To return to the main README click [here](/README.md)
* [Back to top of UX.md](#ux) 

![Home Page](/assets/screenshots/homepage.png)

## Database

To return to the main README click [here](/README.md)
* [Back to top of UX.md](#ux) 

I used PostgreSQL relational database management system for this app.
The model diagram below visually represents the structure of a PostgreSQL database, including tables, columns, relationships, and constraints, that is actually stored in the database itself.

![database model diagram](/assets/docs/databasemodel.png)

### Data Models

#### User model
User model as part of the Django allauth library contains basic information about authenticated user and contains folowing fields: username, password,email

#### Vehicle model

- Vehicle model is model used for each vehicle post uploaded by the user. 
- It has foreign key to the User model to associate each post with the author who created it.
- Using foreign keys to establish these relationships model it is associated with valid users in the system. 
- The model has the following fields:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| title        | title      | CharField| max_length=200, unique=True  |
| creator        | creator       |ForeignKey   | User, on_delete=models.CASCADE  |
| category| category  | ForeignKey   | LearningCategory, on_delete=models.PROTECT, null=True     |
|  slug   | slug   | SlugField   | max_length=100, unique=True  |
| body       | body     |TextField |      |
|  featured_image     | featured_image      | CloudinaryField  | 'image', default='placeholder'   |
|  created_on     | created_on      | DateTimeField   | auto_now_add=True    |
|  updated_on     | updated_on      | DateTimeField   | auto_now_add=True    |
| youtube_link        | youtube_link     | URLField| max_length=200  |

#### Comment model

- Comment model is used for any user comment on a Vehicle post. 
- There are 2 foreign keys one associated to a user and the other to post fields of this model are:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| author         |  author          | ForeignKey | User, on_delete=models.CASCADE   |
| created        | created       | DateTimeField    | auto_now_add=True   |
| post| post   | ForeignKey   | Post, on_delete=models.CASCADE, related_name='comments'     |
| content    | content    | TextField    | max_length=500   |
| status       | status      |BooleanField | max_length=255, default=True     |

