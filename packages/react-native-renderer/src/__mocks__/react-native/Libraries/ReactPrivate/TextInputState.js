/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * LICENSE file in the root directory of this source tree.
 */

'use strict';

// Mock of the Native Hooks
// TODO: Should this move into the components themselves? E.g. focusable

const TextInputState = {
  blurTextInput: jest.fn(),
  focusTextInput: jest.fn(),
};

module.exports = TextInputState;
