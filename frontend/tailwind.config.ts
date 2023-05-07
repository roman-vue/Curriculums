module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        app: {
          primary: "#343635",
          gray: {
            silver: "#737575",
            steel: "#737575",
            pearl: "#D7DBDA",
          },
          white: {
            smoky: "#EFF4F3",
          },
        },
      },
    },
  },
  plugins: [],
};
