/**
 * Testing configuration
 *
 * Setup:
 *  - test runner: karma
 *  - assertions: expect (https://github.com/mjackson/expect)
 */
const webpackConfig = require('./webpack.config');
const testGlob = '{{ cookiecutter.project_slug }}/static/{{ cookiecutter.project_slug }}/**/__tests__/**/*.js';
const srcGlob = '{{ cookiecutter.project_slug }}/static/{{ cookiecutter.project_slug }}/@(actions|components|containers|reducers)/**/*.js';


module.exports = function(config) {
  config.set({
    basePath: '',
    frameworks: ['mocha'],
    files: [
      testGlob,
      srcGlob,
    ],
    preprocessors: {
      // add webpack as a preprocessor
      [testGlob]: ['webpack', 'sourcemap'],
      [srcGlob]: ['webpack', 'sourcemap'],
    },
    webpack: webpackConfig,
    webpackMiddleware: {
      noInfo: true,
    },
    plugins: [
      'karma-webpack',
      'karma-sourcemap-loader',
      'karma-chrome-launcher',
      'karma-mocha',
      'karma-coverage',
    ],
    reporters: ['progress', 'coverage'],
    coverageReporter: {
      dir: '{{ cookiecutter.project_slug }}/static/{{ cookiecutter.project_slug }}/dist//reports/coverage',
      reporters: [
        {type: 'lcov', subdir: '.'},
        {type: 'json', subdir: '.'},
        {type: 'text-summary'},
      ],
    },
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['Chrome'],
    singleRun: true,
    concurrency: Infinity,
  });
};
