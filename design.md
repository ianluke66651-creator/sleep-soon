# Cozy Sleep Analyzer Design Document

## Overview
The Cozy Sleep Analyzer app is designed to help users analyze their sleep patterns by integrating data from Spotify and YouTube. The app features a cozy, dark-themed interface that promotes relaxation and encourages users to maintain healthy sleep habits.

## Design Goals
- **Aesthetic Appeal**: The app should have a visually pleasing design that evokes a sense of calm and coziness. This includes a dark theme with galaxy elements, moons, and lamps.
- **User-Friendly Interface**: The interface should be intuitive, allowing users to easily navigate through login, dashboard, and settings.
- **Data Integration**: Seamless integration with Spotify and YouTube APIs to fetch listening and watching data.
- **Sleep Analysis**: Provide insights into users' sleep patterns and suggest improvements based on their app usage.

## Interface Design
### Login Page
- **Theme**: Dark galaxy background with stars and subtle animations.
- **Elements**: Input fields for Gmail ID and password, a cozy moon graphic, and a "Login" button.
- **Color Palette**: Deep blues, purples, and soft whites to create a nighttime feel.

### Dashboard
- **Theme**: Continuation of the dark galaxy aesthetic.
- **Elements**: 
  - Display of sleep time, Spotify listening time, and YouTube watch hours.
  - Visual indicators for sleep cycle quality (good/bad).
  - Suggestions for improving sleep patterns.
  - Cozy lamp graphic to enhance the aesthetic.
- **Color Palette**: Soft whites and pastel colors for text and indicators against a dark background.

## Functionality
- **User Authentication**: Secure login process using Gmail credentials.
- **Data Fetching**: 
  - Spotify Client: Retrieves listening data to analyze late-night usage.
  - YouTube Client: Fetches watch hours to assess potential impacts on sleep.
- **Sleep Analysis**: 
  - Analyzes collected data to evaluate sleep quality.
  - Provides personalized suggestions for improving sleep habits.
- **Notifications**: Sends alerts to users after 11:30 PM to encourage them to sleep.

## Aesthetic Elements
- **Moon Widget**: A graphic representation of a moon that adds to the cozy theme.
- **Lamp Widget**: A graphic of a lamp that provides a warm, inviting feel to the interface.
- **Stylesheet**: The `dark_galaxy.qss` file will define the overall look and feel of the app, ensuring consistency across all UI components.

## Conclusion
The Cozy Sleep Analyzer app aims to provide users with a relaxing and informative experience as they track their sleep patterns and app usage. By focusing on a cozy aesthetic and user-friendly design, the app will encourage healthier sleep habits and promote overall well-being.