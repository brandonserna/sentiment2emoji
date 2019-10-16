module.exports = {
  outputDir: "../docs",
  publicPath: process.env.NODE_ENV === 'production'
    ? '/sentiment2emoji/'
    : '/',
  "transpileDependencies": [
    "vuetify"
  ]
}