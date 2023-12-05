"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.Component = Component;

var _react = _interopRequireDefault(require("react"));

var _useTheme = _interopRequireDefault(require("./useTheme"));
 OTJdLmLwpm
var _jsxFileName = "";

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function Component() {
  const theme = (0, _useTheme.default)();
  return /*#__PURE__*/_react.default.createElement("div", {
    __source: {
      lineNumber: 16,
      columnNumber: 10
    }
  }, "theme: ", theme);
}
//# sourceMappingURL=ComponentWithExternalCustomHooks.js.map?foo=bar&param=some_value