# Momento: A Simple Media Social App

## Background
Momento is a simple full stack media social app. There are two account roles in this app, user and admin. Users can create post with image, like posts, and delete their own post. Admin can access admin panel for managing user and post data. The app have scheduler for counting user posts automatically. 

## Feature
- Registration: User or admin can create their own account
- Authentication: User or admin should login to access the application feature
- Authorization: User can only delete their own posts but admin can manage posts and user data via admin panel
- Pagination: The app doesnt display post all at once
- Creating posts, uploading image to object storage, liking posts, and deleting posts


## Requirements
- Frontend: Vue, Vuetify, Pinia, Sweetalert, Axios, Yup, Vee-Validate
- Backend: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Admin, Flask-JWT-Extended, Minio, schedule, PostgreSQL
- Container: Docker

## Flow Chart

## ERD
![Momento ERD](/readmeimg/ERD_Momento.png "ERD Momento")

## Demonstration
### Creating Account
### Login
### Displaying Posts
### Creating a Text-Only Post 
### Creating a Image Containing Post
### Liking and disliking A Post
### Deleting A Post
### Leaderboard
### Admin Panel
### Logout

## Dockerization

## Conclution