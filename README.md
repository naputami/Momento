# Momento: A Simple Media Social App

## Background
Momento is a simple full stack media social app. There are two account roles in this app, member and admin. Users can create post with image, like posts, and delete their own post. User with admin role can access admin panel for managing user and post data. The app have scheduler for counting user posts automatically. 

## Feature
- Authentication: User can create account and login using registered account to access the application feature
- Authorization: Member can only delete their own posts, create, and like a post. Admin can manage posts and user data via admin panel
- Pagination: The app doesnt display post all at once
- Storing image in Minio bucket.


## Dependencies
- Frontend: Vue, Vuetify, Pinia, Sweetalert, Axios, Yup, Vee-Validate
- Backend: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Admin, Flask-JWT-Extended, Minio, schedule, PostgreSQL
- Container: Docker

## Flow Chart
![Momento Flow Chart](/readmeimg/momento_flowchart.png "Flow chart Momento")
## ERD
![Momento ERD](/readmeimg/ERD_Momento.png "ERD Momento")

## Demonstration
### Creating Account
![Test case register](/readmeimg/testcase_register.gif "Test case register")  
The app displays a registration form to the user, which includes for checking all input field is filled by the user. Email addresses must adhere to the standard email format, and passwords must contain a minimum of 8 characters, including a combination of letters, numbers, and special characters. Additionally, there is a check to ensure that the password entered in the 'password' field matches the one in the 'confirm password' field. The submitted data is sent to the database via the `/api/auth/signup` endpoint. The notification, whether indicating the success or failure of the registration, will be displayed to the user.
### Login
![Test case login](/readmeimg/testcase_login.gif "Test Case Login")  
The app displays a login form to the user, with input fields for username and password. The submitted data is sent to the database via the api/auth/login endpoint. If the login is successful, the Flask app returns an access token and refresh token, which are stored in the local storage. In case of a failed login attempt, a notification will be displayed to the user. If access token is expired, teh app automatically send request to `api/auth/refresh` to get new access token.
### Displaying Posts Using Pagination
![Test case pagination](/readmeimg/testcase_pagination.gif "Test case pagination")  
The app display 5 posts to user. If user click the pagination button, the app will send request to get another posts data.
### Creating a Text-Only Post 
![Test case text only post](/readmeimg/testcase_posttxt.gif "Test case text only post")  
When user click add new post button, the app will display a form for submitting new post. The app will sent POST request to `api/posts` then the new post data is saved to database. Next, the frontend will render new post data to be displayed. If adding task is failed, a notification will be displayed.
### Creating a Image Containing Post
![Test case post with image](/readmeimg/tescase_postimg.gif "Test case post image")  
When user click add new post button, the app will display a form for submitting new post. The app will sent POST request to `api/posts` then the new post data is saved to database. The image will be saved in Minio bucket. Next, the frontend will render new post data to be displayed. If adding task is failed, a notification will be displayed.
### Liking A Post
![Test case liking a post](/readmeimg/testcase_likepost.gif "Test case liking a post")  
Clicking like button will trigger the app to send POST request to `api/posts/post_id/like`. The endpoint contain query to increase a post's like number and the frontend will display the number. After like button is clicked, it will change to a dislike button. If the dislike button is clicked, the app will send POST request to `api/posts/post_id/dislike`and post's like number will decrease by 1. If the process failed, a notification will displayed to user. 
### Deleting A Post
![Test case deleting a post](/readmeimg/testcase_deletepost.gif "Test case deleting a post")  
Delete button is displayed only in post which created by logged user. Clicking delete post button will trigger the app to send DELETE request to `api/posts/posts_id` endpoint. The deleted project will not be displayed when the deletion process is success. All tasks associated with the deleted project will be removed as well. A window alert will be displayed when deletion process is failed.
### Leaderboard
![Test case leaderboard](/readmeimg/testcase_leaderboard.gif "Test case leaderboard")  
When user click leaderboard button, the app will send a GET request to `api/count_posts` and the browser will display data in table format.In case the fetching data failed, a window alert will be displayed to the user. The count posts data is automatically updated every 60 seconds. 
### Admin Panel
![Test case admin panel](/readmeimg/testcase_adminpanel.gif "Test case admin panel")  
If user login with account whose role is member, the button to admin panel will not be displayed.  
![Member app menu](/readmeimg/member_appmenu.png "Member App Menu")  
The button will be displayed if the logged user has role as admin. Admin can do CRUD post and user data on the admin panel.  
![Admin app menu](/readmeimg/admin_appmenu.png "Admin App Menu")
### Logout
![Test case logout](/readmeimg/testcase_logout.gif "Test case logout")  
When a user clicks the logout button, the app sends a POST request to `api/auth/logout`. The user's token is added to the blacklist_token table. If logout is success, all user data will be removed from local storage and the app state. In case the logout failed, a window alert will be displayed to the user.

## How To Run This App
1. clone this repository
```
git clone https://github.com/naputami/Momento.git
```
2. Create env file for this variable
```
JWT_SECRET_KEY
SQLALCHEMY_DATABASE_URI
SECRET_KEY
VUE_BASE_URL
VITE_API_BASE_URL
MINIO_BUCKET
POSTGRES_USER
POSTGRES_DB
POSTGRES_PASSWORD
```
3. Make sure that you have installed docker desktop and run this command
```
docker compose up
```
4. You can access the application via localhost:4173.
## Conclution
All of the application's features currently function as expected. However, there are areas that can be enhanced in the future, including:
1. Enhancing UI Design for improving intuitiveness and accessibility, especially for admin panel page.
2. Enhancing the notification system to make notifications more user-friendly.
3. Enhancing the database design to accommodate more detailed user and post data.
4. Improving code so the app can run faster when deployed with gunicorn.
5. Fixing networking in docker compose so each container can communicate smoothly.
6. Add loading indicator to indicate that a process is still in progress.
7. Using Minio in docker container so we can configure the bucket locally.
