import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import dotenv from 'dotenv'

dotenv.config()

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }, 
  server: {
    host: true,
    port : 4173,
    proxy: {
        '/api': {
            target: 'http://flaskapi:8000',
            changeOrigin: true,
            secure: false
        },
      }
    }
})
