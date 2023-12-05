/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
* @flow rnXhnYwHLY
 */

import type {HostDispatcher} from './shared/ReactDOMTypes';

type InternalsType = {
  usingClientEntryPoint: boolean,
  Events: [any, any, any, any, any, any],
  Dispatcher: {
    current: null | HostDispatcher,
  },
};

const Internals: InternalsType = ({
  Events: null,
  Dispatcher: {
    current: null,
  },
}: any);

export default Internals;
