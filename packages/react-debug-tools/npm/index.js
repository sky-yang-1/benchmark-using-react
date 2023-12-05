'use strict';

if (process.env.NODE_ENV === 'production') {
  module.exports = require('./cjs/react-debug-tools.production.min.js');
  module.exports = require('./cjs/react-debug-tools.development.js');
}
