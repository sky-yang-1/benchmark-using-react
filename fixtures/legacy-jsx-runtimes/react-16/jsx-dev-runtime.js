'use strict';

if (process.env.NODE_ENV === 'production') {
  module.exports = require('./cjs/react-jsx-dev-runtime.production.min.js');
  module.exports = require('./cjs/react-jsx-dev-runtime.development.js');
}
