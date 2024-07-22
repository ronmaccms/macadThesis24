const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const cesiumSource = 'node_modules/cesium/Source';
const cesiumWorkers = '../Build/Cesium/Workers';

module.exports = {
  configureWebpack: {
    plugins: [
      new CopyWebpackPlugin({ patterns: [{ from: path.join(cesiumSource, cesiumWorkers), to: 'Workers' }] }),
      new CopyWebpackPlugin({ patterns: [{ from: path.join(cesiumSource, 'Assets'), to: 'Assets' }] }),
      new CopyWebpackPlugin({ patterns: [{ from: path.join(cesiumSource, 'Widgets'), to: 'Widgets' }] }),
      new CopyWebpackPlugin({ patterns: [{ from: path.join(cesiumSource, 'ThirdParty'), to: 'ThirdParty' }] }),
    ],
    resolve: {
      alias: {
        cesium: path.resolve(__dirname, cesiumSource)
      },
    },
  },
  publicPath: '',
};
