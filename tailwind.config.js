const colors = require('tailwindcss/colors')
const colrs= require('tailwindcss/colors')
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors:{
        ...colors,
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
] }