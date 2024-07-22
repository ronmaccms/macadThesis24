const path = require('path');

module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        '@components': path.resolve(__dirname, 'src/components'),
        'three': 'three/build/three.min.js'
      }
    }
  }
}

