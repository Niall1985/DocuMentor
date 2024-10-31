# DocuMentor

This React-based frontend application interacts with backend APIs to fetch content through both multithreaded and sequential processing modes. It provides users with the ability to input data, which is processed by backend services, and returns the results. The frontend parses and displays the output while providing a loading indication during the fetching process.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Components](#components)
- [Context Management](#context-management)
- [Backend Requirements](#backend-requirements)
- [Known Issues](#known-issues)
- [Contributing](#contributing)

## Features

- **Multithreaded Processing**: Makes an API call to a backend endpoint designed for multithreaded processing.
- **Sequential Processing**: Makes a separate API call to a backend endpoint that processes data sequentially.
- **Loading Indicators**: Provides feedback when data is being fetched.
- **Conditional Rendering**: Displays either "No relevant content found." or the fetched content based on results.
- **Reusable Components**: Uses modular components for ease of maintenance and extension.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Start the application:

   ```bash
   npm start
   ```

## Usage

1. **Input Data**: Enter the required data in the frontend input fields.
2. **Fetch Data with Threads**: Click the "With Threads" button to fetch data via the multithreaded backend API.
3. **Fetch Data Sequentially**: Click the "Without Threads" button to fetch data through the sequential backend API.
4. **View Results**: Processed results are displayed in the frontend. If no relevant content is found, a default message is shown.

## File Structure

```
src/
├── Context/
│   └── InfoContext.js        # Manages global state for fetched data
├── hooks/
│   └── useInfo.js            # Custom hook for fetching data
├── components/
│   ├── WithThread.js         # Component for multithreaded results
│   ├── WithoutThread.js      # Component for sequential results
│   └── Content.js            # Reusable component for displaying content
├── App.js                    # Main application component
└── index.js                  # Entry point for React application
```

## Components

### `WithThread.js`

- **Description**: Displays results from the multithreaded API.
- **Functionality**: Uses `textThread` from `InfoContext` and checks for relevant content. Shows "No relevant content found." if no content is available.

### `WithoutThread.js`

- **Description**: Displays results from the sequential API.
- **Functionality**: Uses `noThread` from `InfoContext` and processes data similarly to `WithThread.js`.

### `Content.js`

- **Description**: Renders individual content items, handling conditional content display.

## Context Management

`InfoContext.js` provides a global state for the application, holding data returned from API calls, including `textThread` (for multithreaded data) and `noThread` (for sequential data). 

## Backend Requirements

- **Multithreaded Endpoint**: `http://localhost:9001/run-multithreaded?input=your_input` - Expected to handle data using multithreading.
- **Sequential Endpoint**: `http://localhost:9002/run-sequential?input=your_input` - Expected to handle data sequentially.

The backend should return text content as plain text, as the frontend uses string processing to extract relevant data.

## Known Issues

- **Initial "No relevant content found" Message**: This message displays by default until data is returned. It will disappear once content is available in `textThread` or `noThread`.
- **Error Handling**: API error messages are displayed as toast notifications.

## Contributing

Contributions are welcome! Please fork this repository, make changes, and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a pull request
