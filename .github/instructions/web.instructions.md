{
  "applyTo": "web/src/**/*.{ts,tsx}"
}

- React 18 + TypeScript strict mode; never use any types
- Use TanStack Query v5 (useQuery, useMutation) for all server state
- Axios instance in services/api.ts; base URL from env
- Only functional components; never use class components
- Custom hooks in hooks/; prefix with use (e.g., useTodos)
- Service functions in services/: plain async, return typed data
- All interfaces/types in types/; never define types inline in components
- Access Vite env vars via import.meta.env.VITE_*
- camelCase for variables/functions; PascalCase for components/types
- Organize by pages/, components/, hooks/, services/, types/, utils/
- All code: type hints, docstrings, inline comments for complex logic
- Use explicit imports; avoid wildcard imports
- Keep functions/components short, focused, single-responsibility
- Validate all API data with Zod
- vitest + React Testing Library for all tests
- Mock server/API in tests; never hit real endpoints
- Never commit .env or secrets files
