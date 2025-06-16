import { defineConfig } from 'vite'

export default defineConfig({
  base: '/autism-resources-by-state/',
  build: {
    target: 'esnext', /*browsers can handle the latest ES features*/
    outDir: 'build' // Optional — only if you want `build` instead of `dist`
  },
});