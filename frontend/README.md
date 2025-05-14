# AI Support Chat Frontend

Modern React-based frontend for the AI Support Chat application.

## Features

- 🎨 Modern UI with Material-UI components
- 🌙 Dark/Light theme support
- 📱 Fully responsive design
- ⚡ Real-time chat updates with WebSocket
- 🔒 JWT authentication
- 📝 Form validation with Yup
- 🎯 TypeScript for better development experience
- 🚀 Fast development with Vite
- 📦 State management with Redux Toolkit

## Tech Stack

- **Framework**: React 18
- **Language**: TypeScript
- **UI Library**: Material-UI (MUI)
- **State Management**: Redux Toolkit
- **Styling**: Styled Components
- **Real-time**: Socket.io-client
- **HTTP Client**: Axios
- **Form Handling**: React Hook Form
- **Validation**: Yup
- **Build Tool**: Vite

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
# or
yarn install
```

2. Create `.env` file:
```env
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
```

3. Start development server:
```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

## Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable components
│   │   ├── chat/           # Chat-related components
│   │   ├── auth/           # Authentication components
│   │   ├── layout/         # Layout components
│   │   └── common/         # Common UI components
│   ├── pages/              # Page components
│   │   ├── Chat.tsx        # Chat page
│   │   ├── Login.tsx       # Login page
│   │   └── Register.tsx    # Registration page
│   ├── store/              # Redux store
│   │   ├── slices/         # Redux slices
│   │   └── index.ts        # Store configuration
│   ├── services/           # API services
│   │   ├── api.ts          # Axios configuration
│   │   ├── auth.ts         # Authentication service
│   │   └── chat.ts         # Chat service
│   ├── hooks/              # Custom hooks
│   │   ├── useAuth.ts      # Authentication hook
│   │   └── useChat.ts      # Chat hook
│   ├── utils/              # Utility functions
│   │   ├── validation.ts   # Form validation schemas
│   │   └── helpers.ts      # Helper functions
│   ├── styles/             # Global styles
│   │   ├── theme.ts        # MUI theme configuration
│   │   └── global.ts       # Global styles
│   ├── types/              # TypeScript types
│   ├── App.tsx             # Root component
│   └── main.tsx            # Entry point
├── public/                 # Static files
├── index.html              # HTML template
├── package.json            # Dependencies
├── tsconfig.json           # TypeScript configuration
├── vite.config.ts          # Vite configuration
└── .env                    # Environment variables
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build

## Development Guidelines

### Component Structure
```typescript
// Example component structure
import { FC } from 'react';
import styled from 'styled-components';

interface Props {
  // Component props
}

const Component: FC<Props> = ({ prop1, prop2 }) => {
  return (
    <Container>
      {/* Component content */}
    </Container>
  );
};

const Container = styled.div`
  // Styled components styles
`;

export default Component;
```

### State Management
```typescript
// Example Redux slice
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface State {
  // State interface
}

const initialState: State = {
  // Initial state
};

const slice = createSlice({
  name: 'sliceName',
  initialState,
  reducers: {
    // Reducers
  },
});

export const { actions } = slice;
export default slice.reducer;
```

### API Integration
```typescript
// Example API service
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const service = {
  async getData() {
    const response = await api.get('/endpoint');
    return response.data;
  },
};
```

## Styling Guidelines

1. Use Material-UI components as the primary UI elements
2. Use styled-components for custom styling
3. Follow the theme configuration for consistent design
4. Use responsive design principles

## Best Practices

1. Use TypeScript for all new code
2. Write meaningful component and function names
3. Keep components small and focused
4. Use proper error handling
5. Implement proper loading states
6. Follow React hooks best practices
7. Use proper form validation
8. Implement proper error boundaries

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## License

[Your License Here] 