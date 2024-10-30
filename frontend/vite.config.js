import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173, // React frontend port
    proxy: {
      '/run-sequential': {
        target: 'http://localhost:9002',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/run-sequential/, ''),
      },
      '/run-multithreaded': {
        target: 'http://localhost:9001',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/run-multithreaded/, ''),
      },
    },
  },
});
