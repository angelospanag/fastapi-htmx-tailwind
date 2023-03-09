/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.{html,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["night"],
  },
}