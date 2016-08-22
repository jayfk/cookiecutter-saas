import webpack from 'webpack';
import ForceCaseSensitivityPlugin from 'force-case-sensitivity-webpack-plugin';
import BundleTracker from 'webpack-bundle-tracker';
import baseConfig from './webpack.base.config.js';


module.exports = (opts) => {

  const config = baseConfig(opts);

  return {
    ...config,
    output: {
      ...config.output,
      publicPath: 'http://0.0.0.0:8080/bundles/',
    },
    plugins: [
      ...config.plugins,
      // local bundle stats file
      new BundleTracker({filename: './webpack-stats.json'}),
      new ForceCaseSensitivityPlugin(),  // OSX wont check but other unix os will
      new webpack.NoErrorsPlugin(),
    ],
  };
};
