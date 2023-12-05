'use strict';

module.exports = {
  rules: {
    'no-primitive-constructors': require('./no-primitive-constructors'),
    'no-to-warn-dev-within-to-throw': require('./no-to-warn-dev-within-to-throw'),
    'warning-args': require('./warning-args'),
    'no-production-logging': require('./no-production-logging'),
    'safe-string-coercion': require('./safe-string-coercion'),
  },
};
