'use strict';

if (process.env.NODE_ENV === 'production') {
} else {
  module.exports = require('./cjs/react-noop-renderer-flight-client.development.js');
}
