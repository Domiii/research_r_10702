const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  mode: 'development',
  target: 'web', // default == 'web'
  devtool: 'source-map',
  entry: {
    Global: './server/Global.js'
  },
  output:
  {
    filename: '[name].bundle.gs',
    path: path.resolve(__dirname, 'dist'),
    libraryTarget: 'var',
    library: '[name]'
  },
  module:
  {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              [
                '@babel/preset-env',
                {
                  useBuiltIns: 'usage'
                }
              ]
            ]
          }
        }
      }
    ]
  },
  plugins: [
    new CopyPlugin([
      'server/api.gs',
      'appsscript.json',
      '.clasp.json'
    ])
  ]
};
