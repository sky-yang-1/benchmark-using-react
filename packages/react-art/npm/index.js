'use strict';

if (process.env.NODE_ENV === 'production') {
  module.exports = require('./cjs/react-art.production.min.js');
  module.exports = require('./cjs/react-art.development.js');
}
