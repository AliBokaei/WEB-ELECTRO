## Web Design Project

![Web Design](Images/Template.png)

### Description

This repository contains the source code for a university web design project, aimed at developing a user-friendly, responsive website for a university department or organization. The project includes frontend development using HTML, CSS, and JavaScript, as well as backend functionality using Django.

---

## Features

- **Responsive design** for optimal display on various devices
- **User-friendly interface** with intuitive navigation
- Dynamic product pages with **tab switching** and **price updates**
- **Star rating** system for products
- Shopping cart with **add, view, and remove** item features
- Backend functionality for **user registration, login**, and **product management**

## Frontend Phase Objectives

The primary objective of this phase is to integrate **JavaScript functionalities** into the frontend, ensuring an interactive user experience. Key features to be implemented are:

1. **Login Button**:

   - When clicked, a **login popup** should appear.

2. **Register Button**:

   - From the login popup, clicking the register button should open a **registration popup**.

3. **Product Page Tabs**:

   - Clicking on the "Description", "Additional Information", and "Review" tabs should dynamically change the displayed content without reloading the page.

4. **Product Price Update**:

   - Changing the product color should dynamically update the product price without a page reload.

5. **Product Rating**:

   - Users can rate products with star icons. The submitted rating should be logged in the console.

6. **Add to Cart**:

   - Clicking the "Add to Cart" button increases the cart item count displayed on the cart icon at the top of the page.

7. **Shopping Cart**:

   - Clicking the cart icon opens the shopping cart, with two default items displayed.

8. **Remove Item from Cart**:
   - Clicking the delete icon should remove the respective item from the cart.

### Additional Requirements

- Implement these functionalities using **JavaScript**.
- Ensure **smooth user experience** with animations and transitions.
- Consider using a **state management library** for dynamic content changes.
- Implement **error handling** and **form validation** to ensure a robust application.

## Backend Functionality

The backend functionality includes designing and implementing models, forms, views, and database queries. Use **Django** or a **REST API** for the following requirements:

### Required Models

You are required to implement and design the following models. Additional models may be added based on your project requirements.

- **Product**
- **Discount Code**
- **Shopping Cart**
- **Category**

### View Implementation

- Design and implement views for user interaction and data retrieval (Django or REST API).
- Write appropriate queries to fetch, insert, or update data in the database.
- Ensure all models are connected to the **admin panel** for easy management.

### Key Requirements

- Users must be able to **register** with an email and password.
- Users must be able to **log in** using their email and password.
- Users should be able to browse the **home page** and **product pages** dynamically, without logging in.
- Product page updates should reflect real-time changes made through the admin panel.
- Admin should be able to modify **product information** (excluding reviews) in the admin panel.
- Only logged-in users should be able to add items to their cart.
- Admin should be able to customize **banners** on the homepage (the top image and the iPhone 13 banner from the Figma design).
- The banner button link should also update when the image is changed.

## How to Run the Project

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AliBokaei/WEB-ELECTRO.git
   ```

2. **Frontend**:

   - Open `index.html` in a browser to see the static site.

3. **Backend**:
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Django server:
     ```bash
     python manage.py runserver
     ```
